a=int(input("AB="))
b=int(input("BC="))
c=int(input("CA="))
if a==b==c:
    print("ABC là tam giác đều")
elif a==b!=c or a!=b==c or a!=c==b:
    print("ABC là tam giác cân")
else:   
    print("ABC là tam giác thường")