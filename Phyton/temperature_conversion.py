'''Complete the program by writing and calling a function that converts a temperature from Celsius into Fahrenheit. 
Use the formula F = C x 9/5 + 32.
Test your program knowing that 50 Celsius is 122 Fahrenheit.'''

def c_to_f(celsius):
    return  celsius * 9/5 +32

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = c_to_f(temp_c)

print('Fahrenheit:' , temp_f) 