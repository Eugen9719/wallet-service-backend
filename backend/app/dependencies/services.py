from backend.app.dependencies.repositories import user_repo

from backend.app.services.auth.authentication import UserAuthentication
from backend.app.services.auth.password_service import PasswordService
from backend.app.services.auth.permission import PermissionService
from backend.app.services.auth.registration_service import RegistrationService
from backend.app.services.auth.user_service import UserService

password_service = PasswordService()
permission_service = PermissionService()

user_auth = UserAuthentication(password_service, user_repo)
registration_service = RegistrationService(user_repo, password_service, permission_service)
user_service = UserService(user_repo, permission_service, password_service)
