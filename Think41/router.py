from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.order_on_board import session
from app import crud, schemas
from app.databases import SessionLocal,engine

Base.metadata,create_all(bind=engine)
router = APIRouter()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()