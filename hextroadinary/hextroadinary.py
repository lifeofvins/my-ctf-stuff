# Meet ROXy, a coder obsessed with being exclusively the worlds best hacker.
# She specializes in short cryptic hard to decipher secret codes.
# The below hex values for example, she did something with them
# to generate a secret code, can you figure out what? 
# Your answer should start with 0x.
# 0xc4115 0x4cf8

hex_number1 = 0x0c4115
hex_number2 = 0x4cf8

text = hex(hex_number1 ^ hex_number2)

print(text)