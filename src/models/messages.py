from src.core.database import Base


class Chat(Base):
    __tablename__ = "chats"


class Message(Base):
    __tablename__ = "messages"
