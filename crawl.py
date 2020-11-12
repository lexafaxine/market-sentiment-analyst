# coding utf-8#

from Crypto.Cipher import AES
import requests
import base64
import json
import random
import datetime
import time

# pre-process

# ====================================================================================#

# define the encryption
class EncryptDate:
    def __init__(self, key):
        self.key = key
        self.length = AES.block_size
        self.aes = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        Fill the function so that the bytecode length of the encrypted data is an integer multiple of block_size
        """
        count = len(text.encode("utf8"))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # encryption function
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # decryption function
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


# ===============================================================#

# get the secret key
def timestamp() -> str:
    t = int(time.time())
    return str(t)


def encryption_data():
    t = timestamp()
    text = json.dumps({
        "appId": "1",
        "timestamp": t,
        "serverCode": "0"
    }, separators=(',', ':'))
    return text


def get_sign(encryptor: EncryptDate):
    text = encryption_data()
    res = encryptor.encrypt(text).replace("\\", "_").replace("/", "_").replace("\\", "-").replace("+", "-")
    return res


# ====================================================================================#

# make HTTP requests

# get the text of the page
def get_post(encryptor: EncryptDate, post_date: datetime.date):
    post_list = []
    payload = {}
    page_num = 20
    for i in range(1, page_num):
        url = "https://gate.8btc.com/w1/news/list?num=20&cat_id=4481&page=" + str(i)+\
              '&post_date='+str(post_date)+\
              '&end_date='+str(post_date)

        headers = {
            "Content-Type": "application/json",
            "from": "web",
            "Source-Site": "8btc",
            "authorization": json.dumps({"secretKeyVersion": 1, "sign": get_sign(encryptor)}),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

        r = requests.get(url=url, headers=headers, data=payload)
        print(r)

        if r.status_code != 200:
            return post_list

        else:
            text = r.json()
            if len(text['list']) == 0:
                print('crawl ending at'+str(i)+'th page')
                break
            else:
                for x in text['list']:
                    post_list.append(x)
        sleep_time = random.randint(5, 15)
        time.sleep(sleep_time)
        print("sleep",sleep_time,"seconds")
    return post_list


if __name__ == '__main__':
    key = 'WTAHAPPYACTIVITY'
    eg = EncryptDate(key)
    r = get_post(eg, 2000)
    print(r)
