import random;

words = ["Python","JavaScript","Go","Luo","Roby"]
sum = 0
for i in range(1,6):
    userGusser = input("Please Gusser The Programmer Language With Capitalize: ")

    randNum = random.randint(1,4)

    if words[randNum] == userGusser:
        print("Congrates",words[randNum])
        sum += 1
    else:
        print("Opps :(",words[randNum])
print(sum)
