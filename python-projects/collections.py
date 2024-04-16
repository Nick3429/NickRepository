lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40)
print(lst)

lst.pop(2)
print(lst)

lst.reverse()
print(lst)
lst.sort()
print(lst)

lst[0] = 500
print(lst)

lst = lst[1:]
print(lst)

index3 = lst.index(7)
print(index3)

lst.append(20)
lst.append(20)
lst.append(20)
print(lst)

num20 = lst.count(20) #Need to use count function for hw2
print(num20)

lst_copy = lst
print(lst_copy)
lst_copy[1] = 99
print(lst_copy)
print(lst) #lst and lst copy both get changed at the 1st index spot with value 99 as both point to same mem address

new_copy = lst.copy()
print(new_copy)
new_copy[0] = 1000
print(lst)
print(new_copy)

new_copy = lst[:] # Same as new_copy = lst.copy()

empty_lst = []
for el in lst:
    empty_lst.append(el)
print(empty_lst)

empty_lst =[0]*10
print(empty_lst)
empty_lst[1] = 100
print(empty_lst)

squares = []
for x in range(1,10):
    squares.append(x*x)
print(squares)

plus_5 = [5 + x for x in lst]
print(plus_5)

small_vals = [val for val in lst if val < 20]
print(small_vals)

fav_food = {"Kathleen":"pizza", "Maya":"ice cream", "Tom":"ice cream", "Eric":"Steak" }
print(fav_food)

mff = fav_food["Maya"]
print(mff)

for key in fav_food:
    print(f"{key}'s favorite food is {fav_food[key]}")

for person, food in fav_food.items():
    print(f"{person}'s favorite food is {food}")

if "Bob" in fav_food:
    print(fav_food["Bob"])
else:
    fav_food["Bob"] = "wings"
print(fav_food)





