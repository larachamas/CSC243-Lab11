class scubatank:
    def __init__(self,label,bar):
        self.label = label
        self.__bar = bar
        
    def get_bar(self):
        return self.__bar
    
    def set_bar(self, bar):
        if 0<= bar <=300:
            self.__bar = bar
        else:
            print("Invalid pressure.")
    
    def fill(self, amount):
        if amount>0:
            self.__bar +=amount
        else:
            print("Invalid amount.")
    
    def release(self, amount):
        if amount <=0:
            print("Invalid amount.")
        elif amount > self.__bar:
            print("Not enough air.")
        else:
            self.__bar -=amount
    
    def __str__(self):
        return "Tank "+ self.label + ": "+ str(self.__bar)+" bar"
    
def transfer_air(source, target, amount):
    old_pressure = source.get_bar()
    source.release(amount)
    new_pressure = source.get_bar()
    if old_pressure - new_pressure == amount:
        target.fill(amount)

src = scubatank("A",150)
dst = scubatank("B",20)
transfer_air(src,dst,50)
print(src)
print(dst)
transfer_air(src,dst,120)
print(src.get_bar())
print(dst.get_bar())