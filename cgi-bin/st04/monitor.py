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
        return 'monitor: ' + self.getName() + ' age: ' + str(self.getAge()) + ' grants: ' + str(self.getGrants()) + ' address: ' + self.getAddress() + ' phone: ' + self.getPhone() + ' email: ' + self.getEmail()