class ReverseIterator(object):
    def __init__(self, iterable_object):
        self.list = iterable_object
        self.index = len(iterable_object)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.list[self.index]

    __next__ = next


class Days(object):

    def __init__(self):
        self.days = ["Monday","Tuesday","Wednesday","Thursday",
                     "Friday","Saturday","Sunday"]

    def reverse_iter(self):
        return ReverseIterator(self.days)

if __name__ == "__main__":
    days = Days()
    for day in days.reverse_iter():
        print(day, end=' ')
