from .student import *
class Monitor(Student):
    def __init__(self, name, age, grants, address, phone, email):
        Student.__init__(self, name, age, grants, address)
        self.setPhone(phone)
        self.setEmail(email)
    def setPhone(self, inputValue):
        self._phone = inputValue
    def setEmail(self, inputValue):
        self._email = inputValue
    def getPhone(self):
        return self._phone
    def getEmail(self):
        return self._email
    def __str__(self):
        return '<th>monitor</th><th>' + self.getName() + '</th><th>' + str(self.getAge()) + '</th><th>' + str(self.getGrants()) + '</th><th>' + str(self.getAddress()) + '</th><th>' + str(self.getPhone()) + '</th><th>' + str(self.getEmail())+'</th>'