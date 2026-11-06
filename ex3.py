def celsius_to_fahrenheit(celsius, round_to=1):
    temp = (celsius * 9/5) + 32
    return temp
def fahrenheit_to_celsius(fahrenheit, round_to=1):
    temp = (fahrenheit - 32) *5/9
    return temp,

#(a) convert table
print("\n  °C |    °F ")
print("-------+-------")
for celsius in range(0, 101 , 20):
    print(f"{celsius:4} | {celsius_to_fahrenheit(celsius):6}")
#(b) normal body temperature
print(f"98.6 °F = {fahrenheit_to_celsius(98.6)} °C")

#(c)
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))

#(d)
print(celsius_to_fahrenheit(37, round_to=3))