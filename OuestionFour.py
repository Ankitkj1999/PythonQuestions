dict = {"Audii": 10000000, "Nishan": 500000, "Ford": 7000000, "BMW": 8000000}
print(sorted(dict.items(), key=lambda kv: (kv[1], kv[0])))
print("Enter name of the car :\n")
t = input()
c = 0
for i in sorted(dict):
    if i == t:
        c = 1
        data = dict[i]
        break

if c == 0:
    print("Car name that u entered does not exsit !!")
    print("Please enter the price of that car :")
    p = input()
    dict[t] = p
else:
    print("Car found !! and the price of that car is :", data)

for k in sorted(dict.keys()):
    print(k, dict[k], end=" ")