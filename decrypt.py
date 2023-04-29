import base64
from Crypto.Cipher import AES as _AES

key = 'ckjrTheKey!@##@!'.encode()
iv = '9NONwyJtHesysWpN'.encode()


def aes_decrypt(content: str):
    cipher = _AES.new(key, _AES.MODE_CBC, iv)
    content = base64.b64decode(content)
    return (cipher.decrypt(content).decode('utf-8')).replace('\n', '')


enc_data = 'W51vhiETxqCek4Br1toFoabBFASRO5c/afMRJ5xhkPeDMBjRmlSJFGgQDvv/3PZJnJDOKy2m7Pt4+y71Gr6rq+HmUXIydJidE4a4g1ptcpEW5i300LqDwdzX2jCqtQr93xDGcRVoY6DiUlxxT1CGnw=='

print(aes_decrypt(enc_data))
