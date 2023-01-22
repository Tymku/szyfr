# CONSTs:
PREFIX = "[>] "
O_RESPONSES = [
    "E aby ZASZYFROWAĆ tekst\n[>] D aby DESZYFROWAĆ tekst\n[>] C aby ZAMKNĄĆ program",

]
N_RESPONSES = [
    "Wpisz o ile chcesz przesunąć:",
]
   
ALPHABET_LENGTH = 26
CAPITAL = set(range(65, 91))
SMALL = set(range(97, 123))

o = str()
while o != "Z":
# DECLARE & RESET VARs:
    o = str()
    tries = int()
    characterIDs = list()
    tekst1 = str()

# USER INPUT:
    while o not in ["D","E","C"]:
        o = input(PREFIX + O_RESPONSES[tries] + "\n").upper()
        if tries < len(O_RESPONSES) - 1: tries += 1    
    if o == "C": break;
    tries = 0

    tekst = input(PREFIX + "Wpisz tekst do zaszyfrowania:\n")
    n = int()

    while not n:
        try: 
            n = int(input(PREFIX + N_RESPONSES[tries] + "\n"))
        except ValueError: 
            if tries < len(N_RESPONSES) - 1: tries += 1
    tries = 0

    if n > ALPHABET_LENGTH or n < -ALPHABET_LENGTH: n -= (n // 26)*26
    if o == "D": n *= -1 
    

# ENCRYPTION/DECRYPTION:
    for character in tekst:
        number = ord(character)

        encryptedNumber = int() 
        overflowNumber = int(ALPHABET_LENGTH * n/abs(n))

        if number not in [*CAPITAL,*SMALL]: encryptedNumber = number
        elif {number,number+n}.issubset(CAPITAL) or {number,number+n}.issubset(SMALL): encryptedNumber = number + n
        else: encryptedNumber = number + n - overflowNumber

        tekst1 += chr(encryptedNumber)

    print(PREFIX + tekst1 + "\n=-=-=")