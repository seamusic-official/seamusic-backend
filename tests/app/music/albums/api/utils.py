from pydantic import BaseModel, ConfigDict


# from src.domain.auth.users.core.service import BaseService


class CurrentUser(BaseModel):
    id: int
    model_config = ConfigDict(extra='ignore')


async def get_current_user() -> CurrentUser:
    return CurrentUser(id=1)
