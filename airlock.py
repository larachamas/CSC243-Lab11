class airlock:
    def __init__(self,code):
        self.code=code
        self.__sealed = False
    
    def is_sealed(self):
        return self.__sealed
    
    def __lock_bolts(self):
        print("Bolts locked.")
    
    def __unlock_bolts(self):
        print("Bolts unlocked.")
    
    def seal(self):
        if self.__sealed:
            print("Already sealed.")
        else:
            self.__lock_bolts()
            self.__sealed=True
            print("Airlock sealed.")
    
    def unseal(self):
        if not self.__sealed:
            print("Already open.")
        else:
            self.__unlock_bolts()
            self.__sealed=False
            print('Airlock open.')
    
    def __str__(self):
        if self.__sealed:
            status = "sealed"
        else:
            status = "open"
        return "Airlock " + self.code + ": "+ status

a = airlock("Hi")
print(a)
a.seal()
print(a.is_sealed())
a.seal()
a.unseal()
print(a)
a.unseal()