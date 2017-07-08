# Celsius to Fahrenheit converter
# Preparatory statements
print("This program is a temperature converter")
print("Would you like to know the temperature?")
print(" ")

# First input prompt, need to simplify to Y or N
option = float(input("Please input 1 for Yes or 2 for No: "))
if option > 1:
    exit()


def Fahrenheit(Celsius):
    Fdegress = float(Celsius) * 1.8 + 32
    return Fdegress


temperature = float(input("What are the degrees in celsius? "))
print(str(Fahrenheit(temperature)) + " degrees fahrenheit")

if temperature < 10.0:
    print("That's pretty cold!")
else:
    print("Better get naked!")
print("Have a nice day!")


again = input('Do another temperature conversion? (Y/N)')

# Need to figure out how to get the program to loop, prolly learn later.
if again == "N":
    exit()
if again == "Y":
    my_func()
