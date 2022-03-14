def encrypt(key, msg):
    ciphertext = ''
    int1 = int(len(msg) / len(key))
    num_block = int1
    for j in range(0, num_block, 1):
        for i in range(0, len(key), 1):
            ciphertext += chr(ord(key[i]) ^ ord(msg[j * len(key) + i]))
    for i in range(0, len(msg) - num_block * len(key), 1):
        ciphertext += chr(ord(key[i]) ^ ord(msg[num_block * len(key) + i]))
    return ciphertext


def decrypt(key, ctext):
    text = ''
    num_block = int(len(ctext) / len(key))
    for j in range(0, num_block, 1):
        for i in range(0, len(key), 1):
            text += chr(ord(key[i]) ^ ord(ctext[j * len(key) + i]))
    for i in range(0, len(ctext) - num_block * len(key), 1):
        text += chr(ord(key[i]) ^ ord(ctext[num_block * len(key) + i]))
    return text
