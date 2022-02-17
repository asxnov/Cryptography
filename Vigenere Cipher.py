crypt = input("[Ш]ифровка|[Д]ешифровка: ").upper()
if crypt not in ['Ш','Д']:
	print("Ошибка"); raise SystemExit
text = input("Текст: ").upper()
KD = input("Ключ: ").upper()

def EncryptDecrypt(mode, message, key):
	key *= len(message) // len(key) + 1
	finalMessage = ""
	for i, j in enumerate(message):
		if mode in ['Ш','ш']:
		    temp = ord(j) + ord(key[i])
		else:
		    temp = ord(j) - ord(key[i])
		finalMessage += chr(temp % 26 + ord('A'))
	return finalMessage
    
print("Шифртекст: ",EncryptDecrypt(crypt, text, KD))
