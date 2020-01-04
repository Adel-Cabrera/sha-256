import hashlib
import random
import string

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

while True:
  str=randomString(10)
  hs = hashlib.sha256(str.encode('utf-8')).hexdigest()
  if "b00da" in hs:
    print(hs)
    print(str)
    break
