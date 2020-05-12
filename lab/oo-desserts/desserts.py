"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""
        

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__(self,name, flavor,price):
        self.name = name
        self.qty = 0
        self.flavor = flavor
        self. price = price

        self.cache[name] = self


    def add_stock(self,amount):
        self.qty+=amount

    def sell(self, amount):
        if self.qty == 0:
            print ("Sorry, these cupcakes are sold out")
            return
        
        if self.qty <= amount:
            self.qty = 0
            return
       
        self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients,amount):
        ingredients_lst=[]
        for ing_name, ing_qty in ingredients:
            ingredients_lst.append((ing_name, ing_qty*amount))
        return ingredients_lst

    @classmethod
    def get(cls,name):
        for cupcake_name in cls.cache:
            if cupcake_name == name:
                return cls.cache[name]
        print ("Sorry, that cupcake doesn't exist")
# test_cupcake = Cupcake('testing 123',0)

class Brownie(Cupcake):
    def __init__(self, name, price):
        super().__init__(name,price, flavor = "Chocolate")
        
        




if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
