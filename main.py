import random

FRASE = "CUERNO AZULADO"
KEY = ""

for i in FRASE:
    KEY += str(random.randint(0, 1))

CIFRADO = ""
for i in range(len(FRASE)):
    CIFRADO += chr(ord(FRASE[i]) ^ ord(KEY[i]))

DESCIFRADO = ""
for i in range(len(CIFRADO)):
    DESCIFRADO += chr(ord(CIFRADO[i]) ^ ord(KEY[i]))

print("KEY:", KEY)
print("CIFRADO:", CIFRADO)
print("DESCIFRADO:", DESCIFRADO)
