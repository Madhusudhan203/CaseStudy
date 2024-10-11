
accno=200919325863
db={}
dic={}
class Bank:
    def createAccount(self):
        global dic
        global accno
        accno+=1
        self.fname=input("Enter your First Name:")
        self.lname=input("Enter your Last Name:")
        self.phno=input("Enter yourn Phone number:")
        self.email=input("Enter your mail id:")
        data=[self.fname,self.lname,self.phno,self.email]
        print("Account Created!!!!!!!!!!!!")
        print("Your Account Number is:",accno)
        bal=0
        dic[accno]=[0]
        data.append(bal)
        db[accno]=data
        print("Your Account Balance is:",bal)
    def viewAccDetails(self,acc):
        if acc in db:
            print(db[acc])
        else:
            print("Account Not Found!!!!!!")
    def withdraw(self,acc,amount):
        if acc in db:
            if amount>db[acc][4]:
                print("Insufficient Balance")
            else:
                db[acc][4]-=amount
                dic[acc].append(-amount)
                print("Your Account Balance is:",db[acc][4])
        else:
            print("Account Not Found!!!!!!!!!!!")
    def deposit(self,acc,amount):
        for i in db:
            if i==acc:
                db[acc][4]+=amount
                dic[acc].append(amount)
                print("Deposit Rs.",amount,"is success!!!!!")
                print("Your Bank Balance is:",db[acc][4])
                break
        else:
            print("Account not found!!!!!!")
    def printTransactions(self,acc):
        for i in db:
            if i==acc:
                print("Transaction History:\n ")
                print(acc,":",dic[acc])
                break
        else:
            print("Account Not Found!!!!!!!!!")
    def fundTransfer(self,acc,acc2,amount):
        if acc in db and acc2 in db:
            if amount > db[acc][4]:
                print("insufficient funds")
            else:
                db[acc][4]-=amount
                dic[acc].append(-amount)
                db[acc2][4]+=amount
                dic[acc2].append(amount)
                print("Transaction Successfull!!!!!!!!!!!!")
        else:
            print("Account Not Found!!!!!!!!!")
    def checkBalance(self,acc):
        if acc in db:
            print(db[acc][4])
        else:
            print("Account Not Found!!!!!!!!!!")

        

while(True):
    print('''
    1.CREATE ACCOUNT
    2.VIEW ACCOUNt DETAILS BY ACCOUNT NUMBER
    3.WITHDRAW
    4.DEPOSIT
    5.FUND TRANSFER
    6.PRINT TRANSACTIONS
    7.EXIT
Select option you want:''')
    choice=int(input())
    if choice==1:
        obj=Bank()
        obj.createAccount()
    elif choice==2:
         accno=int(input("Enter AccountNo:"))
         obj.viewAccDetails(accno)
    elif choice==3:
        acc=int(input("Enter AccountNo:"))
        amount=int(input("Enter amount you want to deposit:"))
        obj.withdraw(acc,amount)
    elif choice==4:
        acc=int(input("Enter AccountNo:"))
        amount=int(input("Enter amount you want to Deposit:"))
        obj.deposit(acc,amount) 
    elif choice == 5:
        acc=int(input("Enter Your AccountNo:"))
        acc2=int(input("Enter Recipent AccountNo:"))
        amount=int(input("Enter amount want to transfer:"))
        obj.fundTransfer(acc,acc2,amount)
    elif choice==6:
        acc=int(input("Enter AccountNo:"))
        obj.printTransactions(acc) 
    elif choice == 7:
        acc=int(input("Enter AccountNo:"))
        obj.checkBalance(acc)
    else:
        break