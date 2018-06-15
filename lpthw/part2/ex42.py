# --coding:utf-8 --
import random


class GuessNumber(object):
    def __init__(self, times):
        self._target = random.randint(10, 100)
        self._times = times
        self._his = []

    def start(self):
        # type: () -> object
        print("I have marked a number between 10 to 100")
        while True:
            input_number = input("input a number > ")
            if input_number.isdigit():
                if self.judge(int(input_number)):
                    break
            elif input_number == 'result':
                print('result is ', self._target)
            else:
                print("You should input a number")

    def judge(self, input_number):
        result = False
        self._his.append(input_number)
        if self._target < input_number:
            print("You should input a smaller one")
        elif self._target > input_number:
            print("You should input a bigger one")
        else:
            print("God Job! You get it!")
            result = True
        return result


