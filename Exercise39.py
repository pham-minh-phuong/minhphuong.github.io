n=int(input("Muc decibel:"))
if (n==130):
    print("Tieng on bua khoan")
elif (n==106):
    print("Tieng on may cat co dung gas") 
elif (n==70):
    print("Dong ho bao thuc")
elif (n==40):
    print("Can phong im ang")
elif (n>130):
    print("Lon hon tieng on bua khoan")
elif (n<40):
    print("Nho hon tieng on can phong")
elif (n<130) and (n>106):
    print("Tieng on nam giua tieng on bua khoan va tieng on may cat co dung gas")
elif (n<106) and (n>70):
    print("Tieng on nam giua tieng on may cat co dung gas va dong ho bao thuc")   
elif (n<70) and (n>40):
    print("Tieng on nam giua dong ho bao thuc va can phong im ang")
