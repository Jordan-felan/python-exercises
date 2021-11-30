
# OBJECT ORIENTED PROGRAMMING

class MyRouter(object):
    "This is a class that describes the charateristics of a router."
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)

router1 = MyRouter('R1', '2600', '123456', '12.4')
print(router1)
print(router1.model)
print(router1.ios)
print(router1.serialno)
print(router1.routername)

router1.print_router("20181010")

router2 = MyRouter('R2', '7200', '101010', '12.2')
print(router2.model)
print(router2.ios)
print(router2.serialno)
print(router2.routername)
router2.print_router("20190101")
router2.ios = "12.3"
print(router2.ios)
print(getattr(router2, "ios"))
setattr(router2,"ios","12.1")
print(getattr(router2, "ios"))
print(hasattr(router2, "ios"))
print(hasattr(router2, "ios2"))
delattr(router2, "ios")
print(hasattr(router2, "ios"))

class MyNewrouter(MyRouter):
    def __init__(self, routername, model, serialnp, ios, portsno):
        MyRouter.__init__(self,routername,model,serialnp,ios)
        self.portsno = portsno

    def print_new_router(self, string):
        print(string + self.model)

new_router1 = MyNewrouter("newr1", "1800", "111111", "12.2", "10")
print(new_router1.portsno)

print(new_router1.model)
print(new_router1.ios)

new_router1.print_router("ahakhasjakis")
new_router1.print_new_router("ahakhasjakis")

print(issubclass(MyNewrouter, MyRouter))