A = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' * 2  

def f(text, l, k):
    l *= len(text) // len(l) + 1 
    text = text.upper()
    return ''.join([A[A.index(j) + int(l[i]) * k] for i, j in enumerate(text)])

def encrypt(message, key):
    return f(message, key, 1)

def decrypt(ciphertext, key):
    return f(ciphertext, key, -1)

key = input('Ключ: ')
message = input('Текст: ')
ciphertext = input('Шифртекст: ')

print()

print('Шифровка - ', encrypt(message, key))  
print('Дешифровка - ',decrypt(ciphertext, key))
