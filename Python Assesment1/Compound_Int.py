amount = int(input("Enter principal amount = "))
rate = int(input("Enter rate of interest = "))
time = int(input("Enter the time in years = "))
Compound_Interst = amount*(1+(rate/100))**time
print(f"Compund interest of {amount} at the rate of {rate} for {time} years is {Compound_Interst}")