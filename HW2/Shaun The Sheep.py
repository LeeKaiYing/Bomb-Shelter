sheep_sizes = [5, 7, 300, 90, 24, 50, 75]
print ("Hello my name is Le and these is my sheep sizes")
print (sheep_sizes)
a = max(sheep_sizes)
print('Now my biggest sheep has size' ,a, 'lets sheer it!')


list_2 = [x + 50 for x in sheep_sizes]
print ("After 1 month, now here is my flock", list_2)
b = max(list_2)
print ("Now my biggest sheep has size", b, "let's shear it")
for m,i in enumerate(list_2):
    if i == b:
        list_2[m] = 8
print("After shearing, here is my flock", list_2)


list_3 = [x + 50 for x in list_2]
print ("After 1 month, now here is my flock", list_3)
c = max(list_3)
print ("Now my biggest sheep has size", c, "let's shear it")
for m,i in enumerate(list_3):
    if i == c:
        list_3[m] = 8
print("After shearing, here is my flock", list_3)

list_4 = [x + 50 for x in list_3]
print ("After 1 month, now here is my flock", list_4)
d = max(list_3)
print ("Now my biggest sheep has size", d, "let's shear it")
for m,i in enumerate(list_4):
    if i == d:
        list_4[m] = 8
print("After shearing, here is my flock", list_4)

e = sum(list_4)
print ("My flock has size in total:", e)
f = int(1077*2)
print ("I would get 1077*2$ =", f, "$")
