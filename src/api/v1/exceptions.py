from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        detail: str = "Not found",
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code=status_code, detail=detail)


class UnauthorizedException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: str = "Unauthorized",
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code=status_code, detail=detail)


class NoRightsException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_403_FORBIDDEN,
        detail: str = "Forbidden",
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code=status_code, detail=detail)


class InvalidRequestException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail: str = "Invalid request",
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code=status_code, detail=detail)


class CustomException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(status_code=status_code, detail=detail)
