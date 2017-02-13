class Singleton(object):

     def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

if __name__ == "__main__":

    singleton = Singleton()
    another_singleton = Singleton()

    if singleton is another_singleton:
        print('singleton is another_singleton')
    else:
        print('singleton is not another_singleton')
