class Person:

    def __init__(self, name):
        self.name = name
        self.size = {}

    def add_dick(self, size, *args):
        if args:
            john = args[0]
        else:
            john = 'Unknow Fag'
        self.size.update({john: size})

hank = Person("Hank")
hank.add_dick(8, 'fred')
hank.add_dick(size=2)
print(hank.size)
