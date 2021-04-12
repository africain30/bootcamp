class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount
    

def corrupted_account(account):
    if type(account)!= Account:
        return False
    cdt0 = dir(account)
    if(len(cdt0)%2 != 0):
        return False
    cdt1 = []
    """la fonction n'est pas encore complete"""
    



class Bank:
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        if type(amount)!=float or amount<0:
            raise TypeError
            
        elif type(origin)!=int and type(origin)!=str:
            raise TypeError
            
        elif type(dest)!=int and type(dest)!=str:
            raise TypeError
         """ici manque une partie pour continuer la verification"""   

                

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        if type(account)!=int and type(account)!=str:
            raise TypeError
        elif type(account)==int:
            if account!=int(id):
                raise TypeError
        elif type(account)==str:
            if account!=str(name):
                raise TypeError
        elif corrupted_account(accont)==True:
            return True 
        """la pratie de la corectiondu compte n'est pas encore faite"""
    
