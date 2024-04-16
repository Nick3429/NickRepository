from car import Car

car_list = []
with open("cars.txt") as file:
    for line in file:
        # strip off end of line
        stripped_line=line.strip()
        # split each word separated by a space and store in the list tokens
        tokens = stripped_line.split()
        tokens[2]=int(tokens[2])
        tokens[3]=int(tokens[3])
        car=Car(tokens[0],tokens[1],tokens[2],tokens[3])
        car_list.append(car)
        

print(car_list[0].get_odometer())
print(car_list[0].get_gas_tank())
print(car_list[1].get_odometer())
print(car_list[1].get_gas_tank())
car_list[0].drive()
car_list[1].drive()
print(car_list[0].get_odometer())
print(car_list[0].get_gas_tank())



# drive(tokens[0])
# get_gas_tank(tokens[0])
# get_odometer(tokens[0])