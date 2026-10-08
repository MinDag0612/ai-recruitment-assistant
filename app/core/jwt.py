from uuid import UUID

from jose import jwt

from app.core.config import settings


class JWTHandler:
    ALGORITHM = "HS256"

    @staticmethod
    def encode(user_id: UUID) -> str:
        payload = {
            "id": str(user_id),
        }
        print(settings.jwt_secret_key)

        return jwt.encode(
            payload,
            settings.jwt_secret_key,
            algorithm=JWTHandler.ALGORITHM,
        )

    @staticmethod
    def decode(token: str) -> UUID:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[JWTHandler.ALGORITHM],
        )

        return UUID(payload["id"])


