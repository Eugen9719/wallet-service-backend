from backend.app.models.payment import Payment
from backend.app.models.schemas import PaymentCreate, PaymentUpdate
from backend.app.repositories.base_repositories import AsyncBaseRepository, QueryMixin


class PaymentRepository(AsyncBaseRepository[Payment, PaymentCreate, PaymentUpdate], QueryMixin):
    def __init__(self):
        super().__init__(Payment)