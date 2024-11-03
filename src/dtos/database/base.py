from pydantic import BaseModel, ConfigDict


class BaseDTO(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)


class BaseRequestDTO(BaseDTO):
    pass


class BaseResponseDTO(BaseDTO):
    pass


class ItemsRequestDTO(BaseRequestDTO):
    offset: int = 0
    limit: int = 10
