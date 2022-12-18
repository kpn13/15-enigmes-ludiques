with open("./data/Enigme1.txt", "r") as f:
    ascii_string = f.read()

ascii_codes = ascii_string.split(" ")

decoded_string = "".join(chr(int(code)) for code in ascii_codes)

print(decoded_string)