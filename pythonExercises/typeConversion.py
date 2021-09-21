# TYPE CONVERSION

# name = 'Jordan Felan'
# age = 26
# relationship_status = 'single'
#
# relationship_status = 'it\'s complicated'
#
# print(relationship_status)



# AGE CALCULATING PROGRAM BASED OF INPUT OF BIRTH YEAR

#importing date class from datetime module
from datetime import date

todays_date = date.today()
current_year = todays_date.year
# print("Current year: ", current_year)
birth_year = input('What year were you born?')
age = current_year - int(birth_year)
print(f'So if the current year is {current_year} and you were born in {birth_year} you are {age}')