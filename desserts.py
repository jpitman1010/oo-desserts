"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    
    cache = {}
    
    def __init__(self, name, flavor, price, qty=0):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = qty
        self.cache[name] = self    
    
    def add_stock(self,amount):
        self.qty += amount

    def sell(self, amount):
        if self.qty == 0:
            print('Sorry, these cupcakes are sold out')
        elif self.qty < amount:
            self.qty = 0
        else:
            self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount):
        ingredient_by_amount = []
        for ingredient in ingredients:
            ingredient_amount = ingredient[1] *amount
            ingredient_new_tuple = (ingredient[0], ingredient_amount)
            ingredient_by_amount.append(ingredient_new_tuple)
        return ingredient_by_amount

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    @classmethod
    def get(cls,name):        
        if name in cls.cache:
            return (cls.cache[name])
        else:
            print("Sorry, that cupcake doesn't exist")


class Brownie(Cupcake):

    def __init__(self, name, flavor, price, qty=0):
        
        super().__init__(name, flavor, price, qty=0)
        self.flavor = "chocolate"


if __name__ == '__main__':
    # test_cupcake = Cupcake()
    # test_cupcake.name = 'testing 123'
    # test_cupcake.qty = 0
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
