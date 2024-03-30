print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

#calculations
tip_percentage = tip / 100
bill_with_tip = (bill * tip_percentage) + bill
bill_per_person = bill_with_tip / people
bill_with_two_decimal = round(bill_per_person, 2)

#result
print(f"Each person should pay: ${bill_with_two_decimal}")
