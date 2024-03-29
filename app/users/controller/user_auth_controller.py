# It inherits from the HTTPBearer class and overrides the __call__ method
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.users.services import decode_jwt


class JWTBearer(HTTPBearer):
    def __init__(self, role: str, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.role = role

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            payload = self.verify_jwt(credentials.credentials)
            if not payload.get("valid"):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            if payload.get("role") != self.role:
                raise HTTPException(
                    status_code=403,
                    detail="User with provided role is not permitted to access this " "route.",
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwt_token: str) -> dict:
        is_token_valid: bool = False
        try:
            payload = decode_jwt(jwt_token)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return {"valid": is_token_valid, "role": payload["role"]}
