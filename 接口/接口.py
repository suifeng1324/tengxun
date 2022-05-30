# author:yangleiw
# createdate:2022/5/16

from typing import Optional

import uvicorn
# 当下绝大部分的接口是HTTP
# 少部分接口是RPC
from fastapi import FastAPI, HTTPException, Depends

from libs import create_token, get_user
from model import Item
from model import LoginInfo

app = FastAPI()

_data = {
    'user': {
        "username": "zhangsan",
        "password": "123123"
    }
}


@app.get("/")
def index():
    return {"msg": "hello world"}


def add(a, b):
    return a + b


@app.get("/add_by_get")  # 接口地址
def add_get(a: int, b: int):  # 接口
    """
    提供了一个接口
    当客户端 请求接口地址：/add_by_get
    就会执行本函数，调用add函数，实现远程调用
    :return:
    """
    c = add(a, b)
    return {"c": c}


@app.post("/add_by_post")
def add_post(item: Item, user: str = Depends(get_user)):  # 参数应该是一个对象，什么样的对象？Item这样的对象
    c = add(item.a, item.b)
    return {"c": c}


@app.get("/items/{item_id)")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/login")
def login(loginfo: LoginInfo):  #
    username1 = loginfo.username
    password1 = loginfo.password
    if loginfo.username != _data['user']['username']:
        # 返回用户名错误
        raise HTTPException(status_code=400, detail="用户名错误！！！")

    if loginfo.password != _data['user']['password']:
        # 返回密码错误
        raise HTTPException(status_code=400, detail="密码错误！！！")

    return {"token": create_token(loginfo.username)}


if __name__ == '__main__':
    uvicorn.run(app='接口:app', host="127.0.0.1", port=8002, reload=True, debug=True)
