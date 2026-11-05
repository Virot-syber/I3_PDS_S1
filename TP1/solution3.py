def celsius_to_fahrenheit (celcius,round_to=1):
    F = celcius*9/5+32
    return F

def fahrenhait_to_celcius(F,round_to=1):
    C = (F-32)*5 /9
    return C

print("\n   °C |  °F")
print(" -----+------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}") 


