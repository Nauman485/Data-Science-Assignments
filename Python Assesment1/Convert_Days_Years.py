num_of_days = int(input("Enter number of days = "))
year = num_of_days//365
weeks = (num_of_days%365)//7
days = (num_of_days%365)%7
print(f"Number of years = {year}")
print(f"Number of weeks = {weeks}")
print(f"Number of days = {days}")