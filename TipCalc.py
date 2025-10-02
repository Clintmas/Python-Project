print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
splitbill=bill/people
print("Each person should pay :", splitbill + (tip * splitbill/100))
print("Total tip is ", bill*tip/100)
print("Total tip payed by each person :", (bill*tip/100)/people)
print("Total bill is:",people*(splitbill + (tip * splitbill/100)))