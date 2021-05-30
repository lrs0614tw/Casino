import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from urllib.parse import urlencode
from Crypto.Util.Padding import pad
uid='a'
iv = b"VFNSJQXI0P6IZ7UC"
key = b"HQR9NSTXMCY7R463"
uid = "CHECKOK_" + uid
bi_data = uid.encode("UTF-8")
cipher = AES.new(key, AES.MODE_CBC, iv)
encode_uid = base64.b64encode(cipher.encrypt(pad(bi_data, AES.block_size))).decode()
url = "https://casino.oakrange.io/heysongScratch?"
p_url = urlencode(dict(uid=encode_uid))
print("game_check OK: ", url + p_url)