class InputData(object):

    def __init__(self, number, power):
        self.number = number
        self.power = power

    def sqrNumber(self):
        return pow(self.number, self.power)


class OutputData(object):

    def __init__(self, num):
        self.num = num

    def rez(self):
        print(str(number) + '^' + str(power) + ' = ' + str(self.num.sqrNumber()))

if __name__ == "__main__":

    number = int(input("Number: "))
    power = int(input("Power: "))

    num = InputData(number, power)
    show = OutputData(num)

    show.rez()
