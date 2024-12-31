from abc import abstractmethod, ABC


class DAO(ABC):
    @abstractmethod
    async def get_album_by_id(self, **kwargs) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    async def get_album_existance(self, **kwargs) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_popular_albums(self, **kwargs) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    async def count_albums(self) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get_artist_id_by_user_id(self, **kwargs) -> int | None:
        raise NotImplementedError

    @abstractmethod
    async def create_album(self, **kwargs) -> int:
        raise NotImplementedError

    @abstractmethod
    async def update_album(self, **kwargs) -> int:
        raise NotImplementedError

    @abstractmethod
    async def delete_album(self, **kwargs) -> None:
        raise NotImplementedError
