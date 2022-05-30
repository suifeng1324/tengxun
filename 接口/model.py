# author:yangleiw
# createdate:2022/5/16

from pydantic import BaseModel


class Item(BaseModel):
    a: int
    b: int


class LoginInfo(BaseModel):
    username: str
    password: str
