import random
from decimal import Decimal

decimal = random.randint(0, 99999)
offset = random.randint(0,2)
seed = float(str(offset) + "." + str(decimal))
message = "Hello world"

def _encode(message, seed):
    text = ""
    for char in message:
        text += str(ord(char))

    print("Text going in:", text)
    print(text, "*", seed)
    final = Decimal(int(text)*seed)
    print("Encoded text:", final)
    return final

def _decode(message, seed):
    print(message, "/", seed)
    text = Decimal(float(message)/float(seed))
    print("Decoded text:", text)

#print(seed)

text_encoded = _encode(message, seed)
_decode(text_encoded, seed)
        
    

    
