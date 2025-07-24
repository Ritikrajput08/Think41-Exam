from pydantic import BaseModel
from typing import List, Optional

class BoardBase(BaseModel)
    str_id:str_id
    name:str_id
class BoardCreate(BoardBase)
    pass
 class ColumnBase(BaseModel)
    str_id:str_id
    name:str_id
class ColumnCreate(ColumnBase)
    board_id:int