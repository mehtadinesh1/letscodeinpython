#Welcome to the temperature conversion Program

print("Welcome to the temperature coversion program")
#get user input
Fahrenheit = float(input("\nWhat is the given temperature in degrees fahrenheit:"))

#use formula to convert fahrenheit degre to clecius
Celcius = (Fahrenheit-32)*5/9
#use round function for limit numberes after dot in float result
Celcius = round(Celcius,4)
#conversion
Kelvin = (Celcius+273.928)
# user round function
Kelvin = round(Kelvin,4)

#show result in table format

print("\nDegree Fahrenheit:    ",Fahrenheit)
print("\nDegree Kelvin:        ",Kelvin)
print("\nDegree celcius:       ",Celcius)
