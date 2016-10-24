

class DataUser (object):
    __slots__ = ('surname', 'name', 'group')

    def __init__(self):
        self.surname=input("surname: ")
        self.name=input("name: ")
        #self.group = group TODO

    def __str__(self):
        print("surname: {}\nname: {}\n".
              format(
            self.surname,
            self.name
        ))
        return("")

