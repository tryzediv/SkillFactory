from pydantic import BaseModel, constr


class AuthRequestModel(BaseModel):
    username: constr(strict=True)
    password: constr(strict=True)


class AuthResponse(BaseModel):
    token: str
