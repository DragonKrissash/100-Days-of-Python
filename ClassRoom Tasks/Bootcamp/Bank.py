class Bank:
    def __init__(self,title,balance,ac_no):
        self.__title=title
        self.__balance=balance
        self.__ac_no=ac_no
        self._interest=0

    def updateInterest(self,interest):
        self._interest=interest

    def getInterest(self):
        print(f'Interest: {self._interest}')

    def withdraw(self,amt):
        if self.__balance>=amt:
            self.__balance-=amt
            print(f'Successfully withdrawn: {amt}')
        else:
            print(f'There is no enough balance!')

    def deposit(self,amt):
        self.__balance+=amt
        print('Deposited successfully!')

    def getBalance(self):
        print(f'The balance: {self.__balance}')

class SavAc(Bank):

    def __init__(self, title, ac_no):
        super().__init__(title=title, balance=0, ac_no=ac_no)
        self._interest=12
        self.getBalance()

    def add_int(self,interest):
        super()._interest=interest
        print(f'Interest updated: {super()._interest}')


class Cur_ac(Bank):
    def __init__(self,title,ac_no):
        super().__init__(title=title,ac_no=ac_no,balance=0)
        super()._interest=5

    def add_int(self,interest):
        super()._interest=interest
        print(f'Interest updated: {super()._interest}')

ac=SavAc(title='Krishna',ac_no=2301010)
ac.getInterest()