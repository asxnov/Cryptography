class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c)+key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c)-key)
        return decrypted_message

message="Asanov Erbolat SIB 18 3A"

g=10 	#alice_public	
a=2		#alice_private

p=541   	#bob_public 
b=3 	    #bob_private

Alice = DH_Endpoint(g, p, a)
Bob = DH_Endpoint(g, p, b)

A = Alice.generate_partial_key()
print('A -', A)

B = Bob.generate_partial_key()
print('B -', B)

SecretKeyA = Alice.generate_full_key(B)
print('SecretKeyA -', SecretKeyA)

SecretKeyB = Bob.generate_full_key(A)
print('SecretKeyB -', SecretKeyB)

bob_encrypted = Bob.encrypt_message(message)
print('cipher Bob -', bob_encrypted)

alice_decrypt = Alice.decrypt_message(bob_encrypted)
print('source text -', alice_decrypt)