a=int(input("Nhập số cạnh:"))
if a==3:
    a="hình tam giác"
elif a==4:
    a="Hình vuông"
elif a==5:
    a="Hình ngũ giác"
elif a==6:
    a="Hình lục giác "
elif a==7:
    a="Hình thất giác "
elif a==8:
    a="Hình bát giác"
elif a==9:
    a="Hình cửu giác"
elif a==10:
    a="Hình thập giác" 
else: 
    print("không đủ điều kiện để tạo thành hình")
    exit()
print("Đây là ",a)