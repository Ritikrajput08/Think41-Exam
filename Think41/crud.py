from sqlalchemy.orm import Session
from app import models,schemas
def create_board(db:session,board:schemas.BoardCreate)

    db_board=model.board()
    db.add()
    db.commit()
    db.refresh()
    return db_board