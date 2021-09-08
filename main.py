import jwt
import hashlib

def checkIfJWT(input: str) -> bool:
    try:
        headers = jwt.get_unverified_header(input)
        if headers["typ"] == "JWT":
            return True
        else:
            return False
    except:
        return False

def getHashString(input: str) -> str:
    hashObject = hashlib.sha256(input.encode("UTF-8"))
    return hashObject.hexdigest()

def convertToken(input: str) -> str:
    if (checkIfJWT(input) == True):
        return getHashString(input)
    else:
        return input;

def convertTokens(input: list[str]) -> list[str]:
    return list(map(lambda x : convertToken(x), input))
