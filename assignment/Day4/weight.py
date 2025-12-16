weight = float(input("Enter weight in tonnes: "))

converters = [
    lambda t: t * 1000,            
    lambda kg: kg * 1000,         
    lambda g: g * 1000,             
    lambda mg: mg / 453592.37    
]

kg = converters[0](weight)
g = converters[1](kg)
mg = converters[2](g)
lb = converters[3](mg)

print(f"Tonnes to kilograms   : {kg:.4f} kg")
print(f"Kilograms to grams    : {g:.4f} g")
print(f"Grams to milligrams   : {mg:.4f} mg")
print(f"Milligrams to pounds  : {lb:.6f} lb")