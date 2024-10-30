from pydantic import BaseModel, ConfigDict


class BaseDTO(BaseModel):
    model_config = ConfigDict(extra='ignore')


class BaseRequestDTO(BaseDTO):
    pass


class BaseResponseDTO(BaseDTO):
    pass
