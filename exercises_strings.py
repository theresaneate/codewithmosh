# https://pythonbasics.org/exercises/
# Strings
from datetime import date

# # Make a program that displays your favourite actor/actress.
# favourite = "Clint Eastwood"
# print("My favourite actor is: " + favourite)

# Try to print the word ‘lucky’ inside string.
string = "Lucky lucky luck"
print(string[6:11])

# Try to print the day, month, year in the form “Today is 2/2/2016”.
today = date.today()
formatted = today.strftime("%d/%m/%y")
print("Today's date = ", formatted)
