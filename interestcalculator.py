#simple calulator app to caluclate interest (HARAM)

#balance
b = float(input("How much money do you have in your bank account? "))
#interest
i = float(input("How much interest do you receive in %? "))
#duration
d = int(input("how many years do you wish to keep this account? "))

# % to decimal
i /= 100

#final balance 
final = b + ((b * i) * d)

print("Your balance after", d,"years is", final, "dollars")