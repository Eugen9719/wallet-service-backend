from decimal import Decimal
from fastapi import APIRouter, HTTPException, status
from backend.app.dependencies.repositories import user_repo, payment_repo, account_repo
from backend.app.dependencies.services import account_service
from backend.app.models import Payment

from backend.app.models.schemas import WebhookRequest
from backend.app.services.helpers import verify_signature

from backend.core.db import TransactionSessionDep

webhook_router = APIRouter()


@webhook_router.post("/process-payment-webhook")
async def process_payment_webhook(
        webhook_data: WebhookRequest,
        db: TransactionSessionDep
):
    # 1. Проверка подписи
    if not verify_signature(webhook_data):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid signature"
        )

    # 2. Проверка существования транзакции
    existing_payment = await payment_repo.exist(db, transaction_id=webhook_data.transaction_id)
    if existing_payment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Транзакция с id={webhook_data.transaction_id} уже создана"
        )

    # 3. Проверка/создание счета
    account = await account_repo.get(db, id=webhook_data.account_id)
    if account:
        if account.user_id != webhook_data.user_id:
            raise HTTPException(
                status_code=400,
                detail="Счет принадлежит другому пользователю "
            )
    if not account:
        user_exists = await user_repo.get_or_404(db, id=webhook_data.user_id)
        account = await account_service.create_account(db, current_user=user_exists)

    # 4. Создаем платеж
    await payment_repo.create(db, schema=Payment(
        transaction_id=webhook_data.transaction_id,
        account_id=account.id,
        amount=webhook_data.amount,
    ))

    # 5. Обновляем баланс счета
    account.balance += Decimal(str(webhook_data.amount))
    account_repo.save_db(db, account)
    return {"status": "success", "new_balance": account.balance}
