
from fastapi import APIRouter, HTTPException, Query, Response, status

from app.data import BOOKS
from app.models import BookCreate, BookUpdate, BookOut

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookOut])
def get_books(
    q: str | None = None,
    author: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
):
    result = BOOKS

    if q:
        keyword = q.lower()
        result = [
            book for book in result
            if keyword in book["title"].lower()
            or keyword in book["author"].lower()
            or keyword in book["isbn"]
        ]

    if author:
        result = [
            book for book in result
            if author.lower() in book["author"].lower()
        ]

    return result[skip:skip + limit]


@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@router.post("/", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    if any(item["isbn"] == book.isbn for item in BOOKS):
        raise HTTPException(status_code=409, detail="ISBN already exists")

    new_book = book.model_dump()
    new_book["id"] = max((item["id"] for item in BOOKS), default=0) + 1
    BOOKS.append(new_book)
    return new_book


@router.put("/{book_id}", response_model=BookOut)
def replace_book(book_id: int, book: BookCreate):
    for index, item in enumerate(BOOKS):
        if item["id"] == book_id:
            if any(
                other["isbn"] == book.isbn and other["id"] != book_id
                for other in BOOKS
            ):
                raise HTTPException(status_code=409, detail="ISBN already exists")

            updated = book.model_dump()
            updated["id"] = book_id
            BOOKS[index] = updated
            return updated

    raise HTTPException(status_code=404, detail="Book not found")


@router.patch("/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookUpdate):
    for item in BOOKS:
        if item["id"] == book_id:
            changes = book.model_dump(exclude_unset=True)

            if "isbn" in changes and any(
                other["isbn"] == changes["isbn"] and other["id"] != book_id
                for other in BOOKS
            ):
                raise HTTPException(status_code=409, detail="ISBN already exists")

            item.update(changes)
            return item

    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for index, item in enumerate(BOOKS):
        if item["id"] == book_id:
            BOOKS.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail="Book not found")
