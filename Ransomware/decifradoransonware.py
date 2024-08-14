
# DecifradoRansonware:

#######################################################

from cryptography.fernet import Fernet

import os

#######################################################

def cargar_key():
    return open('key.key', 'rb').read()
	
def decifrar(items, key):
    f = Fernet(key)
    for item in items:
        # Leo el archivo
        with open(item, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.decrypt(file_data)

        # Escribo el archivo
        with open(item, 'wb') as file: 
            file.write(encrypted_data)	


if __name__ = '__main__':
	path_to_encrypt = 'f:/CifradoDecifradoDatos/'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '\\' + item for item in items]
	
	key = cargar_key()
	decifrar(full_path, key)