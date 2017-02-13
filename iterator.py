class Iterator(object):

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        else:
            self.low += 1
            return self.low - 1
        
if __name__ == "__main__":

    show = Iterator(1, 7)

    for i in show:
        print(i, end=' ')
