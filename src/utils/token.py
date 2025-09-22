def tokenize(text: str):
    return list(text)

def detokenize(tokens: list[str]):

    return "".join(tokens)

def tokenToInteger(token: str):

    return ord(token)

def integerToToken(integer: int):

    return chr(integer)

def encode_text(text: str):

    return " ".join(str(ord(c)) for c in text)

def decode_text(encoded: str):

    return "".join(chr(int(x)) for x in encoded.split())
