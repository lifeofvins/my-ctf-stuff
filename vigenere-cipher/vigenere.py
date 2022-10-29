# The vignere cipher is a method of encrypting alphabetic text
# by using a series of interwoven Caesar ciphers based
# on the letters of a keyword.
# I’m not sure what this means, but it was left lying around: blorpy
# gwox{RgqssihYspOntqpxs}

keys = {0: 1, 1: 11, 2: 14, 3: 17, 4: 15, 5: 24}
enc = "gwox{RgqssihYspOntqpxs}"
dec = ""
i = 0
for letter in enc:
    dec += chr((ord(letter) - keys[i % 6]))
    i += 1
print(dec)
print("CTFlearn{" + dec + "}")
print("CTFlearn{" + dec[4:] + "}")
