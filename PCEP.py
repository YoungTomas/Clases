print (2 +2 * 2 // 2)
print(2 + -2 / 2 +2 )
print(2 -2 *2 +2)
print(2//2*2-2)


print(type(1_000))

heigth = -84//2
print (heigth) 

total = 0
for i in range (4):
    if 2 * i < 4:
        total +=1
else:
    total +=1
    print


speed = 0
while speed < 30:
    speed *= 2
    if speed >10:
        continue
    print("*", end="")
else:
    print("done")

ecual=0
for i in range (2):
    for j in range(2):
        if i ==j:
            ecual+=1
        else:
            break
print(ecual)

floor=0
while floor !=0:
    floor -=1
    print("#", end="")
else:
    print("#")

the_list = ["list", False, 3e8]

print(the_list[1] in the_list)
print(int(the_list[2]) == len(the_list))
print(the_list.index(False) == 1)
print(300 in the_list and the_list[1])

rates=(1.2,1.4,1.0)
new = rates[:]
for rate in rates[-2:]:
    new += (rate,)
print(len(new))

menu = {"1": 3.21, "2": 4.50, "3": 5.00}
for value in menu.values():
    print(str(value)[1],end="")

collection = []
collection.append(1)
collection.insert(0, 2)
duplicate = collection[:]
duplicate.append(3)
print(len(collection) + len(duplicate))
def velocity(x=10):
    return speed * x

speed = 10
new_speed = velocity()
new_speed = velocity(new_speed)
print(new_speed)

def iterate (end, foo = 0):
    if end > 0:
        foo = iterate (end -1 , foo + end)
    return foo

print(iterate(2))