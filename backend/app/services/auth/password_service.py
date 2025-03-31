from backend.app.abstractions.services import IPasswordService

class PasswordService(IPasswordService):
    def hash_password(self, password: str) -> str:
        from backend.core.security import get_password_hash
        return get_password_hash(password)

    def verify_password(self, plain: str, hashed: str) -> bool:
        from backend.core.security import verify_password
        return verify_password(plain, hashed)
