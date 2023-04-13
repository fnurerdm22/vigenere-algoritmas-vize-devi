def encrypt(plaintext, key):
    try:
        plaintext = plaintext.upper()
        key = key.upper()
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext
    except:
        print("Tekrar Kontrol Ediniz.")

def decrypt(cipher, key):
    try:
        cipher = cipher.upper()
        key = key.upper()
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        cipher_int = [ord(i) for i in cipher]
        plaintext = ''
        for i in range(len(cipher_int)):
            value = (cipher_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext
    except:
        print("Tekrar kontrol ediniz.")

if __name__ == "__main__":
    plain = input("Şifrelenecek Metin :")
    key = input("Anahtar :")
    print(encrypt(plain,key))
    print("== decrypt edilmiş hali ==")
    print(decrypt(encrypt(plain,key),key))
