class ShoppingCart:
    def __init__(self):
        self.items = {}



    def __iter__(self):
        self.items2 = {k.lower(): v for k, v in self.items.items()}
        for k,v in self.items2.items():
            try: v.lower()
            except: continue
        for i in sorted(self.items, key=lambda x: self.items2.__getitem__(x)):
        # sorted(.. , key=lambda x: self.items.__getitems__(x))  --  use this to sort by values, lowest to highest with numbers, A-z
        # reverse=True  --  reverse the order
             yield i #+ ': $' + str(self.items[i])

    def __repr__(self):
        print( self.items)



    def add_item(self, name, price):

        self.items[name] = price

cart = ShoppingCart()
cart.add_item("FGSP", 12)
cart.add_item("Emoji Movie Tickets", 5)
cart.add_item("iPhone 8s", 1_000)
cart.add_item('aa', 10000)
cart.add_item('zz', 1)
cart.add_item('ABC', "BBC")
for i in cart: print(i)
