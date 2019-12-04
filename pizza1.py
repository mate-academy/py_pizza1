'''
Module
'''


class Pizza:
    '''Parent class'''
    def __init__(self, ingred=('ham', 'tomatoes', 'cheese')):
        self.ingred = list(ingred)

    def make_recipe(self):
        '''

        :return:
        '''
        strng = 'Make dough\n'
        for i in self.ingred:
            strng += 'Add {}\n'.format(i)
        strng += 'Bake'
        return strng

    def add_ingred(self, item):
        '''

        :param item:
        :return:
        '''
        self.ingred.append(item)


class PopcornPizza(Pizza):
    '''
    Class
    '''
    def __init__(self):
        self.ingred = ['ham', 'popcorn', 'cheese']
        super().__init__(self.ingred)


class ChoclatePizza(Pizza):
    '''
    class
    '''
    def __init__(self):
        self.ingred = ['fish', 'popcorn', 'chocolate']
        super().__init__(self.ingred)
