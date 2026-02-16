#how long will Ali need to save 20k if he has 10k in his account and he accumilates 5% interest per year
from math import log
userInput = input("do you want to use pre-assigned values?(y/n) ")

primaryValue = 10000.000
finalValue = 20000.000
interest = 0.050

if userInput == "n":
  primaryValue = float(input("how much do Ali have in the bank? "))
  finalValue = float(input("how much does Ali need to buy the car? "))
  interest = (float(input("how much does interest does Ali recieve yearly from the bank?(in %) ")))/100

print(f"Ali has {primaryValue: .3f} OMR\nHe needs {finalValue: .3f} OMR to buy the car\nthe bank offers {interest * 100: .1f}% interest")

years = log(finalValue/primaryValue)/log(1+interest)
#print("Ali needs %.2f years to buy the car" %years)

#f string version
print(f"Ali needs {years: .3f} years to buy the car ")
