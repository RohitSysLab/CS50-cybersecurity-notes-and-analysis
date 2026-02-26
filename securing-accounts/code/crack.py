
import string

letters = string.ascii_letters

for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                guess = a + b + c + d
                print(guess)
