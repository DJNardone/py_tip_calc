#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator!")
total_bill = float(input("What is the total bill?  $"))
tip = int(input("How much tip % do you want to add: 10, 15, 18, or 20?  "))
split = int(input("How many people to split the bill?  "))

amt_each = (total_bill / split) * (1 + tip / 100)
print(f"Each person should pay:  ${amt_each:.2f}") # <= format to go out 2 decimel places for ($xx.xx)
