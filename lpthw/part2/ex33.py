# --coding: utf-8--
# guess number
import random
target = random.randint(10, 100)

his = []
print("Now I will mark a number between 10 to 100, you can guess it! 开始猜吧")
while True:
    number_str = input("Input a number 10-100:")
    if number_str.isdigit():
        number = int(number_str)
        his.append(number)
        if number < target:
            print("You should input a bigger one")
        elif number > target:
            print("You should input a little one")
        else:
            print ("You get it")
            break
    else:
        print("You should input a number!")

print("You guess the result use %d times" % len(his))
print("You input numbers are %r" % his)
