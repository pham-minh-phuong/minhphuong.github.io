n=float(input("Tan so:"))
C4=261.63
D4=293.66
E4=329.63
F4=349.23
G4=329.00
A4=440.00
B4=439.88
if (C4-1)<=n<=(C4+1):
    print("Tan so",n,"Hz tuong ung voi not C4")
elif (D4-1)<=n<=(D4+1):
    print("Tan so",n,"Hz tuong ung voi not D4")
elif (E4-1)<=n<=(E4+1):
    print("Tan so",n,"Hz tuong ung voi not E4")
elif (F4-1)<=n<=(F4+1):
    print("Tan so",n,"Hz tuong ung voi not F4")
elif (G4-1)<=n<=(G4+1):
    print("Tan so",n,"Hz tuong ung voi not G4")      
elif (A4-1)<=n<=(A4+1):  
    print("Tan so",n,"Hz tuong ung voi not A4")    
elif (B4-1)<=n<=(B4+1): 
    print("Tan so",n,"Hz tuong ung voi not B4")     
else: print("Tan so khong tuong ung voi mot not da biet")