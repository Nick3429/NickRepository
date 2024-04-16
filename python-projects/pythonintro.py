print("hello world")
#Comment

#Variables
x = 10
print(x)
x= 'hello world'
print(x)
s= 'hello world'

x= 100
y= 10
r = int(x/y)
print(r)
r = x//y
print(r)

#math functions
m = min(100,20)
print(m)
p= pow(2,4)
print(p)
p= 2**4

#if statements
x= -1
y = 1

if x < 0:
    x=1
    x+=10
    print("x was negative")

print("outside of if statement")

if x<0 and y == 1:
    print("x is negative and y is 1")

if x<0 or y==1:
    print("x is negative and y is 10")

if x<0:
    print("x is negative ")
elif x>0:
    print("x is positive")
else:
    print("x is 0")

#loops
counter = 0
while counter < 10:
    print(counter)
    counter+=1

nums = [10, 20, 30 , 40, 50]
for i in range(2,len(nums)):
    print(nums[i])

for num in nums:
    num+=5
    print(num)
print(nums)

for i, val in enumerate(nums):
    print("i is ", i , " and val is ", val)

dogs = ["boomer", "rocky", "daisy"]

nums = [1,2,3,4,5]
sum_nums=0
for val in nums: 
    sum_nums += val
print("The sum of nums is", sum_nums)
print(f"The sum of nums is {sum_nums}")


def hello(name="friend"):
    print("hello!", name)
hello()
hello("bob")

course = "Platform Computing"
platform= course[0:8]
computing = course[9:18]
print(platform, computing)

#Exercise
swap= [0,3,8,5,4]
temp = swap[2]
swap[2]= swap[4]
swap[4]= temp
print(swap)


