from pydantic import BaseModel, ConfigDict


class BaseDTO(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)


class BaseRequestDTO(BaseDTO):
    pass


class BaseResponseDTO(BaseDTO):
    pass
