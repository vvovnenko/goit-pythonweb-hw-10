from fastapi import APIRouter, Depends, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.schemas.usesrs import User
from src.service.auth import get_current_user


router = APIRouter(prefix="/users", tags=["users"])
limiter = Limiter(key_func=get_remote_address)


@router.get("/me", response_model=User, description="Limited by 5 requests per minute")
@limiter.limit("5 per minute")
async def me(request: Request, user: User = Depends(get_current_user)):
    return user
