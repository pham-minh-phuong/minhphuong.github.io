a = int(input("Enter the day (1-31):"))
b = input("Enter the month: ")
if a == 1 and b == "January":
    c = "New Year's Day"
elif a == 1 and b == "July":
    c = "Canada Day"
elif a == 25 and b == "December":
    c = "Christmas Day"
else:
    print("The entered month and day do not correspond to a fixed-date holiday.")
    exit()
print("The entered date corresponds to", c)
