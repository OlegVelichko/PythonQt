def decorate(func):
   def func_wrapper(self):
       return "<p>-{0}-</p>".format(func(self))
   return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Wick"

    @decorate
    def get_full_name(self):
        return self.name + ' ' + self.family


my_person = Person()

print(my_person.get_full_name())
