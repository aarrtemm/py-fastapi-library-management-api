from models import DBAuthor, DBBook
from schemas import AuthorCreate, BookCreate
from sqlalchemy.orm import Session


def get_all_authors(db: Session):
    return db.query(DBAuthor).all()


def create_author(db: Session, author: AuthorCreate):
    db_author = DBAuthor(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def get_author_by_name(db: Session, name: str):
    return (db.query(DBAuthor).filter(
        DBAuthor.name == name
    ).first())


def get_author_by_id(db: Session, pk: int):
    return (db.query(DBAuthor).filter(
        DBAuthor.id == pk
    )).first()


def get_all_books(db: Session):
    return db.query(DBBook).all()


def create_book(db: Session, book: BookCreate):
    db_author = DBBook(**book.dict())

    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_book_by_title(db: Session, title: str):
    return (db.query(DBBook).filter(
        DBBook.title == title
    ).first())


def get_book_by_author_id(db: Session, pk: int):
    return(db.query(DBBook).filter(
        DBBook.author_id == pk
    ))