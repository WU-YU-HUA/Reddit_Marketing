import base64

def encrypt(input: str):
    return base64.b64encode(input.encode("utf-8")).decode('utf-8')
