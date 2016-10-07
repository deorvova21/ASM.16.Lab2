class Student:
    def __init__(self, name, age, grants, address):
        self.setName(name)
        self.setAge(age)
        self.setGrants(grants)
        self.setAddress(address)
    def setName(self, inputValue):
        self._name = inputValue
    def setAge(self, inputValue):
        self._age = inputValue
    def setGrants(self, inputValue):
        self._grants = inputValue
    def setAddress(self, inputValue):
        self._address = inputValue
    def getName(self):
        return self._name
    def getAge(self):
        return self._age
    def getGrants(self):
        return self._grants
    def getAddress(self):
        return self._address
    def getForm(self, q):
        self.setName(q.getfirst("name", None))
        self.setAge(q.getfirst("age", None))
        self.setGrants(q.getfirst("grants", None))
        self.setAddress(q.getfirst("address", None))
        return self
    def __str__(self):
        return '<th>student</th><th>' + str(self.getName()) + '</th><th>' + str(self.getAge()) + '</th><th>' + str(self.getGrants()) + '</th><th>' + str(self.getAddress()) + '</th><th></th><th></th>'