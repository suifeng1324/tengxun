# author:yangleiw
# createdate:2022/5/16
import datetime

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

KEY = "P@ssword123"  # 随机内容，做完加密的key
TOKEN_EXPIRE = 60 * 24 * 7  # token有效期一周


def create_token(username: str):
    """
    根据用户信息，生成token
    :param username: 
    :return: 
    """

    d = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE)
    }

    encoded = jwt.encode(d, KEY, algorithm='HS256')

    return encoded


def get_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/login"))):
    """
    根据token，解析用户信息
    :return:
    """
    try:
        d = jwt.decode(token, KEY, algorithms='HS256')
        # 1. 判断是否过期
        # 2. 判断用户名是否存在
        username = d.get("username", "-1")
    except(jwt.JWTError,):
        raise HTTPException(status_code=403, detail="TOKEN鉴权失败！！！")

    if username == "-1":
        raise HTTPException(status_code=400, detail="用户名错误！！！")
    return username
