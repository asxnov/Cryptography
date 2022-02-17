def encrypt(rows, plaintext):
    assert len(plaintext) % rows == 0
    n = len(plaintext)
    columns = n // rows
    ciphertext = ['-'] * n
    for i in range(n):
        row = i // columns
        col = i % columns
        ciphertext[col * rows + row] = plaintext[i]
    return "".join(ciphertext)

def decrypt(rows, ciphertext):
    assert len(ciphertext) % rows == 0
    return encrypt(len(ciphertext) // rows, ciphertext)

print(encrypt(7,'asanov erbolat'))
print(decrypt(7,'aao roasnveblt'))

print(encrypt(2,'kaznusib'))
print(decrypt(2,'kuaszinb'))
