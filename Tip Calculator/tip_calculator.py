#Calculating the tip
#Using basic arithmetic operators

print('Welcome to the tip calculator')
bill = float(input('What was the total bill? $'))
tip  = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
no_of_people = int(input('How many people to split the bill? '))


#Result =  (Bill + tip%*bill) / Number of people

result = (bill + (0.01*tip*bill)) / no_of_people
print("Each person should pay: ${:.2f}".format(result))