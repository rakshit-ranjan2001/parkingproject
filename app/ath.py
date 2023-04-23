import jwt
import time
import datetime
import app.db as db

jwt_scrt='05771537f681d23f084151b46a340468'
jwt_algo="HS256"
fmt="%Y-%m-%d-%H-%M"
e={"token":"none"}

def enc(payload:dict):
    return jwt.encode(payload,jwt_scrt, algorithm=jwt_algo)

def dec(payload:str):
    return jwt.decode(payload,jwt_scrt,algorithms=[jwt_algo])

def is_auth(token:any):
    if token == "none" or token is None:
        return False
    tm = datetime.datetime.strptime(dec(token)["expiry"], fmt)
    if datetime.datetime.now()<tm:
        return True
    else:
        return False

def crt(email:str):
    exp=datetime.datetime.now() + datetime.timedelta(minutes=60)
    dic={
        "email": email,
        "expiry": exp.strftime(fmt)
    }
    return enc(dic)

def rd(token):
    dic = dec(token)
    return dic["email"]

def is_ath(token:str) -> dict:
    if token is None:
        return e
    elif token == 'none':
        return e
    tm = datetime.datetime.strptime(dec(token)["expiry"], fmt)
    if datetime.datetime.now()<=tm:
        return db.getuser(rd(token))
    else:
        return e