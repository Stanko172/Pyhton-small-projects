import datetime, random 

def get_birthdays(max_birthdays):
    """
    Returns a list of random birthdays
    """
    birthdays = []
    for i in range(max_birthdays):
        #Create initial date, year is not important
        initial_date = datetime.date(2001, 1, 1)
        #Generate random number between 0 - 365 and add that to ini date
        random_days_number = random.randint(0, 365)
        new_birthday = initial_date + datetime.timedelta(random_days_number)
        #Append new birthday to the list
        birthdays.append(new_birthday)

    return birthdays 

def get_match(birthdays):
    """Returns match birthday if it exists, otherwise return None"""
    #Check if array has at least one match
    if len(birthdays) == tuple(birthdays): return None
    #Compare birthday with every other one
    #return match if it occures
    for num_a, birthday_a in enumerate(birthdays):
        for num_b, birthday_b in enumerate(birthdays[num_a + 1 :]):
            if birthday_a == birthday_b: return birthday_a

#Create months tuple for string representation
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
#Ask user for number of birthdays
while True:
    birthdays_number = input("> ")
    if(birthdays_number.isdecimal() and (0 < int(birthdays_number) <= 100)): 
        birthdays_number = int(birthdays_number)
        break
    else: print("The input has to be numeric value and less than 100!")
#Generate birthdays and display them in a more proper way
birthdays = get_birthdays(birthdays_number)
for num_birthday, birthday in enumerate(birthdays):
    print(f"#{num_birthday}: ", end="")
    print(f"{birthday.year} {MONTHS[birthday.month - 1]} {birthday.day}")
#Check for matches
if(get_match(birthdays) != None): print("There is a match!")
else: print("No matches")

#Run simulation for 100 000 times(Mone Carlo simulation)
match_counter = 0
for i in range(100_000):
    if(i % 10_000 == 0 and i != 0): print(f"{i} simulations done...")
    birthdays = get_birthdays(birthdays_number)
    result = get_match(birthdays)
    if(result != None): match_counter += 1

#Display results
match_percentage = round(match_counter / 100_000 * 100, 2)
print(f"Match found in {match_percentage}% of simulations")




