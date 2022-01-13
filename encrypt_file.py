from cipher import io
from cipher import ciphertypes
from cipher.ciphertypes import caesar, vinegar, substitution
# from cipher import io

import yaml

ciphertype = {
    "c" : caesar,
    "v" : vinegar,
    "s" : substitution
}

def main():
    with open("encrypt_config.yml") as f:
        configs = yaml.full_load(f)
    
    text = io.turn_into_string(configs['file_in'])
    
    encrypt_type = configs['encrypt_type']
    args = configs['encrypt_args']
    if encrypt_type == "c":
        encrypted_text = caesar.encrypt(text, args['num'])
    elif encrypt_type == "v":
        encrypted_text = vinegar.encrypt(text, args['key'])
    elif encrypt_type == "s":
        encrypted_text = substitution.encrypt(text, args['key'])
    else:
        print("incorrect encrypt_type:", encrypt_type)
        quit()
    print('Encrypted text:')
    print(encrypted_text)

    with open(configs['file_out'],'w') as f:
        f.write(encrypted_text)


if __name__ == "__main__":
    main()