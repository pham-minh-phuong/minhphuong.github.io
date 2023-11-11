A4 = 440.00 
B4 = 493.88
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00

a = input("Enter a note name (A, B, C, D, E, F, G): ")
x = int(input("Enter the octave (1, 2, 3, 4):"))

if a == "A":
    frequency = A4 / (2 ** (4 - x))

if a == "B":
    frequency = B4 / (2 ** (4 - x))

if a == "C":
    frequency = C4 / (2 ** (4 - x))

if a == "D":
    frequency = D4 / (2 ** (4 - x))

if a == "E":
    frequency = E4 / (2 ** (4 - x))

if a == "F":
    frequency = F4 / (2 ** (4 - x))

if a == "G":
    frequency = G4 / (2 ** (4 - x))

print("The frequency of", a, "is", frequency)
