import time
import hashlib
import os, django
from django.core import signing
from django.core.cache import cache

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TodoList.settings")
django.setup()

HEADER = {'typ': 'JWP', 'alg': 'default'}
KEY = 'CHEN_FENG_YAO'
SALT = '782473006'
TIME_OUT = 180 * 60  # 60min


def encrypt(obj):
    """加密"""
    value = signing.dumps(obj, key=KEY, salt=SALT)
    value = signing.b64_encode(value.encode()).decode()
    return value


def decrypt(src):
    """解密"""
    src = signing.b64_decode(src.encode()).decode()
    raw = signing.loads(src, key=KEY, salt=SALT)
    return raw


def create_token(username):
    """生成token信息"""
    # 1. 加密头信息
    header = encrypt(HEADER)
    # 2. 构造Payload
    payload = {"username": username, "iat": time.time()}
    payload = encrypt(payload)
    # 3. 生成签名
    md5 = hashlib.md5()
    md5.update(("%s.%s" % (header, payload)).encode())
    signature = md5.hexdigest()
    token = "%s.%s.%s" % (header, payload, signature)
    # 存储到缓存中
    cache.set(username, token, TIME_OUT)
    return token


def get_payload(token):
    payload = str(token).split('.')[1]
    payload = decrypt(payload)
    return payload


# 通过token获取用户名
def get_username(token):
    payload = get_payload(token)
    return payload['username']
    pass


def check_token(token):
    username = get_username(token)
    last_token = cache.get(username)
    if last_token:
        return last_token == token
    return False