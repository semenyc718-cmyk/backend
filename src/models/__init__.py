from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .movies import Movie

__all__ = ["Base", "Movie"]