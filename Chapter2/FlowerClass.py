class Flower():
    def __init__(self, name, petal=1, price=10.0):
        self.name = name
        self.petal = petal
        self.price = price

    def set_price(self, new_price):
        self.price = new_price
        print("New price of " + str(self.name) + " flower is " + str(self.price))

    def view_price(self):
        print("The price of " + str(self.name) + "flower is " + str(self.price))


if __name__ in "__main__":

    flower1 = Flower("Rose", 10, 15)
    flower1.view_price()
    flower1.set_price(25.0)