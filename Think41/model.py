from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from app.databases import Base
class Board(Base):
    _tablename_="boards"
    id=Column()
    Str_id=Column()
    name=Column(String)
    columns=relationship("Column",back_populates="boards")


class Board(Base):
    _tablename_="boards"
    id=Column()
    Str_id=Column()
    name=Column(String)
    board_id=Column(Integer)
    order_on_board=()

