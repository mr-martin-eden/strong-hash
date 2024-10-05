def shift_letter(letter, shift):
    alfabe = 'abcçdefgğhıijklmnoöpqrsştuüvwxyz'
    if letter in alfabe:
        index = alfabe.index(letter)
        return alfabe[(index + shift) % len(alfabe)]
    else:
        return letter

def encrypt_message(message):
    shifted_message = ''
    for char in message.lower():
        if char.isalpha():
            shifted_message += shift_letter(char, 6) 
        else:
            shifted_message += char
  
    caesar_encrypted = ''
    for char in shifted_message:
        if char.isalpha():
            caesar_encrypted += shift_letter(char, 3) 
        else:
            caesar_encrypted += char

    return shifted_message, caesar_encrypted  

def string_to_hex(text):
    hex_output = text.encode('utf-8').hex()
    return hex_output

message = input("""

  ██████ ▄▄▄█████▓ ██▀███   ▒█████   ███▄    █   ▄████     ██░ ██  ▄▄▄        ██████  ██░ ██ 
▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▒   ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒
░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░
  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░▓█  ██▓   ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ 
▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░░▒▓███▀▒   ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓
▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▒   ▒     ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ░   ░     ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒     ░   ░ ░ ░ ░   ░     ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░
      ░              ░         ░ ░           ░       ░     ░  ░  ░      ░  ░      ░   ░  ░  ░
                                                                                             

Şifrelenecek mesajı girin: """)

shifted_message, caesar_shift = encrypt_message(message)

hex_shifted = string_to_hex(shifted_message)
hex_caesar = string_to_hex(caesar_shift)

print(f"6 harf ileri şifreleme: {shifted_message} -> Caesar şifrelemesi : {caesar_shift} -> Hex: {hex_caesar}")
