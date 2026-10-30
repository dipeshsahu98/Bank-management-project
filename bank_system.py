#mini bank management project
class account:
    def __init__(self, holder_name, account_number,bank_name, branch_name, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.balance = balance
        self.transaction = []
    def input_datas(self,massage):
        amount = input(massage)
        return amount
        
    def deposit(self):
        while True :
            try :
                add_balance = self.input_datas("enter deposit amount :")
                if not add_balance or not add_balance.isdigit():
                    raise ValueError("deposit balance enter and integer value:")
                add_balance = int(add_balance)   
                
                if not add_balance > 0 :
                    raise ValueError("please enter positive value not 0 starred 1 to your choice -:")
                    
                self.balance = self.balance + add_balance
                deposit_transaction = {
                    "type" : "Deposit",
                    "amount" : add_balance,
                    "balance after" : self.balance
                    }
                
                self.transaction.append(deposit_transaction)
                return f"Deposit Amount ₹: {add_balance}\nNew Amount ₹: {self.balance}"
            except ValueError as e:
                print(e) 
                continue
        
    def withdrawal(self):
        while True :
            try :
                
                withdraw_amount = self.input_datas("withdraw_amount :")
                if not withdraw_amount :
                    raise ValueError("enter a amount -")
            
                if not withdraw_amount.isdigit():
                    raise ValueError("enter a integer value")
                withdraw_amount = int(withdraw_amount  )   
                if withdraw_amount > 0:   
                    if self.balance >= withdraw_amount :
                        print("successfull withdraw money ")
                        self.balance = self.balance - withdraw_amount   
                        
                        withdraw_transaction = {
                            "type" : "withdraw",
                            "amount" : withdraw_amount,
                            "balance after" : self.balance
                            }
                        self.transaction.append(withdraw_transaction)   
                        return f"Wthdraw Amount ₹ : {withdraw_amount}\nNew Amount ₹ : {self.balance}"
                    
                    else :
                        print("withdraw amount not available your account :")
                    
                else :
                    return "please withdraw amount positive and started 1 to your choice :\n"
                
            except ValueError as error:
                print(error)
                continue
    
    def show_history(self):
        if not self.transaction:
            return "not available history of your account"
         
        history_tex = ""
        for data in self.transaction:
            for key,value in data.items():
                history_tex += f"{key} : {value}\n"
            
        return history_tex
        
        
        
    def check_balance(self):
        return self.balance
               
    def account_details(self):
        holder = f"{'account holder name':<22} : {self.holder_name}\n"
        acc_number = f"{'account number':<22} : {self.account_number}\n"
        bank_name = f"{'bank name':<22} : {self.bank_name}\n"
        branch_name = f"{'branch name':<22} : {self.branch_name}\n"
        balance = f"{'balance':<22} : {self.balance}"
            
        return holder + acc_number + bank_name + branch_name + balance
        
all_datas = []
def demo_accounts(account_class):
    demo_account_datas = [
        ("Prideep Kumar","10011","HFDC","Civil Lines",10000),
        ("Akash meena","10012","ICICI","Salt Lake",15000),
        ("Manish Sharma","10013","PNB","Station Road",6000),
        ("Nitesh Sahu","10014","SBI","Main Branch",7000),
        ("Ashavin Sahu","10015","YES BANK","Cyber City",10000),
        ("Nikita Sahu","10016","IDBI","Swaraj Nagar",12000),
        ("Vripind Rajput","10017","BANK OF BARODA","Nuna",2000),
        ("Rajendra kumar","10018","SBI","Maksudangarh",5200),
        ("Hemansu Sahu","10019","AXIS BANK","Bhopal",3100),
        ("Aniket Kumar","10020","BOI","KAROT BHOPAL BRANCH",0),
    ]    
    for acc_name,acc_num,bank_name,branch_name,balance in demo_account_datas :
        obj = account_class(acc_name,acc_num,bank_name,branch_name,balance)
        all_datas.append(obj)
        print("\n")
        print("="*44)
        print(obj.account_details())
        #print("a demo data for my project".upper())    

def account_datas(account_class):
    
    while True :
        try : 
            while True :
                holder_name = input("holder_name :")
                if holder_name and not holder_name.isdigit() :
                    break
                print("not except a empty holder name try again\nenter string value name ;")
            
            while True :
                account_number = input("account number :")
                if not account_number.isdigit():
                    print("enter only integer value :")
                    continue
                existing = False
                for acc in all_datas :
                    if acc.account_number== account_number :
                        existing = True
                        break
                if existing :
                    print("number already available so enter new number :")
                    
                else :
                    break
                    
            while True :
                bank_name = input("bank name :")
                if bank_name and not bank_name.isdigit() :
                    break
                print("enter a bank name and strin value:")
            
            while True :
                branch_name = input("branch name  :")
                if branch_name and not branch_name.isdigit() :
                    break
                print("enter a branch name and string value :")
           
            while True :
                try :
                    balance = int(input("balance :"))   
                    if balance >= 0:
                        break
                    print("balance value only integer :")
                except ValueError :
                    print("please enter a valid integer value :")         
            data = account_class(holder_name,account_number,bank_name,branch_name,balance)
            all_datas.append(data)
            choice = input("enter any accout datas write 'yes' / 'no'\nenter your choice -: ".title()).strip().lower()
            if choice !='yes':
                break 
        except ValueError as a:
            print(a)
    return all_datas

def main_data():
    predefiln_mode = False
    print("="*44)
    print("=======wellcome Bank management system======".upper())
    print(" Select your entry mode :")
    print("1.Run Demo Mode (With 10 Pre-loaded Accounts for strings ):".title())
    print("2.Run Custom Mode (Create and Manage Unlimited New Accounts) :".title())
    option = input("enter your choice -: ".title()).strip().lower()

    if option == "1" :
        demo_accounts(account)
        predefiln_mode = True
    
    elif option == "2" :
        print("user choice account enter data mode on".upper())
        account_datas(account)
    else :    
        print("option not available please enter a correct option".title())

    account_record = None
    while True :
        choice = input("\nenter a new account data 1 \nenter account num to search account 2 \ncheck your account condition 3 \ncheck balannce 4 \nenter deposit amount 5 \nenter withdraw amount 6 \ncheck your account all history 7 \nexit 8 \n\nenter choice -:".title()).strip()
        if choice == "1" :
            if predefiln_mode :
                print("not access demo account user add a new accout ok".title())
            
            else :
                account_datas(account)
                
        elif choice == "2":
            account_record = None 
            account_search_number = input('enter search account number :')
            found = False
            for acc in all_datas :
                if acc.account_number == account_search_number :
                    account_record = acc
                    print(account_record.account_details())
                    found = True 
                    break
            if not found:
                print(f"account{account_search_number}not available join a account :")
            
        elif choice in ["3","4","5","6","7"] :
            if account_record is None :
                print("please enter option 2 and search a account :")
                continue
            if choice == "3" :
                print(account_record.account_details())
            
            elif choice == "4" :
                print(account_record.check_balance())    
            
            elif choice == "5" :
                print(account_record.deposit())
            
            elif choice == "6" :
                print(account_record.withdrawal())
            
            elif choice == "7" :
                print("\n\n")
                print("="*44)
                print("account details and history ".upper().center(40))  
                print("="*44)
                print("\n")          
                print(account_record.account_details())
                print("*"*44)
                print("\n")
                print(account_record.show_history())
                print("\n\n")
            
        elif choice == "8" :
            break    
        else :
            print("not found a option")    
            continue
if __name__ == "__main__":
    main_data()