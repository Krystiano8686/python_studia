# ZAD2

import sys
print("Podaj dwie liczby: ")
a = sys.stdin.readline()
b = sys.stdin.readline()
a = float(a)
b = float(b)
c = a * b
sys.stdout.write(f"Wynik Twojego mnozenia wynosi: {c}")
