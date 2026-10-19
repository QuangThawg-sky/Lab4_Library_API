
from pydantic import BaseModel, Field, field_validator


class BookBase(BaseModel):
    isbn: str = Field(
        ...,
        min_length=13,
        max_length=13,
        description="ISBN gồm đúng 13 chữ số"
    )
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    year: int = Field(..., ge=1900, le=2100)
    quantity: int = Field(default=1, ge=0)

    @field_validator("isbn")
    @classmethod
    def validate_isbn(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError("ISBN phải gồm đúng 13 chữ số")
        return value


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    isbn: str | None = Field(default=None, min_length=13, max_length=13)
    title: str | None = Field(default=None, min_length=1, max_length=200)
    author: str | None = Field(default=None, min_length=1, max_length=100)
    year: int | None = Field(default=None, ge=1900, le=2100)
    quantity: int | None = Field(default=None, ge=0)

    @field_validator("isbn")
    @classmethod
    def validate_isbn(cls, value: str | None) -> str | None:
        if value is not None and not value.isdigit():
            raise ValueError("ISBN phải gồm đúng 13 chữ số")
        return value


class BookOut(BookBase):
    id: int
