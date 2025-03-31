import json
transactions = []
add_income=[]
add_expense=[]
# Feature implementations
def add_transaction():
    global transactions
    print("1.Add transaction.")
    while True:
        try:   
            amount=float(input("Enter the amount: "))
            if amount>0:
                break
        except ValueError:
            print("Invalid input.Please enter a integer or float value ")
    category=str(input("Enter the category: "))
    while True:
        type=str(input("Enter income or expense: ")).lower()
        try:
            if type=='income':
                break
            elif type=='expense':
                break
        except TypeError:
            print("Invalid input please enter income or expense")
    while True:
        try:
            year=int(input("Enter the year[YYYY]: "))
            if 999<year<10000:
                break
        except:
            print("Invalid input.Please enter integer.")
    while True:
        try:
            month=int(input("Enter the month[MM]: "))
            if 0<month<=12:
                break
        except:
            print("Invalid input.Please enter integer.")
    while True:
        try:
            day=int(input("Enter the day[DD]: "))
            if 0<day<=31:
                date=f"{year}-{month}-{day}"
                print(date)
                break
        except:
            print("Invalid input.Please enter integer.")
        pass
    while True:
        save_new_transaction = str(input("Do you want to save new transaction (yes or no): "))
        if save_new_transaction.lower()=='yes':
            new_list=[amount,category,type,date]
            transactions.append(new_list)
            with open("C:/Users/dinuk/OneDrive/Desktop/Test/financetracker.json","w") as file:
                json.dump(transactions,file)
                print("saved successfully")
                if type=="income":
                    add_income.append(amount)
                    print(add_income)
                else:
                    add_expense.append(amount)
                    print(add_expense)
                print(transactions)
                break
        elif save_new_transaction.lower()=='no':
            print("not save")
            break
        else:
            print("Invalid input.Please enter yes or no")
            continue
def view_transactions():
    global transactions
    print("2.View transactions.")
    try:
        with open("financetracker.json","r") as file:
            transactions=json.load(file)
            print(transactions)
    except FileNotFoundError:
        print("file not found")
def update_transaction():
    try:
        with open("C:/Users/dinuk/OneDrive/Desktop/Test/financetracker.json","r") as file:
            transactions=json.load(file)
        while True:
            try:
                print("Take the first list as 0")
                change_list=int(input("Enter list index you want to change: "))
                if change_list >= len(transactions) or change_list<0:
                    print("your input is not in transactions list")
                    continue
                else:
                    break
            except ValueError:
                print("invalid input")
        while True:
            try:
                change_item=str(input("Do you want to change list yes or no: "))
                if change_item=='yes':
                    del transactions[change_list]
                    print(transactions)
                    break
                elif change_item=='no':
                    print("item not remove :")
                    break
            except:
                print("invalid input")
        while True:
            try:
                new_amount=float(input("Enter the amount: "))
                if new_amount>0:
                    break
            except ValueError:
                print("Invalid input.Please enter a integer or float value ")
        new_category=str(input("Enter the category: "))
        while True:
            new_type=str(input("Enter income or expense: "))
            try:
                if new_type.lower()=='income':
                    break
                elif new_type.lower()=='expense':
                    break
            except TypeError:
                print("Invalid input please enter income or expense")
        while True:
            try:
                new_year=int(input("Enter the year[YYYY]: "))
                if 999<new_year<10000:
                    break
            except ValueError:
                print("Invalid input.Please enter integer.")
        while True:
            try:
                new_month=int(input("Enter the month[MM]: "))
                if 0<new_month<=12:
                    break
            except ValueError:
                print("Invalid input.Please enter integer.")
        while True:
            try:
                new_day=int(input("Enter the day[DD]: "))
                if 0<new_day<=31:
                    new_date=f"{new_year}-{new_month}-{new_day}"
                print(new_date)
                break
            except ValueError:
                print("Invalid input.Please enter integer.")
            pass
        while True:
            save_updated_transaction = str(input("Do you want to save new transaction (yes or no): "))
            if save_updated_transaction.lower()=='yes':
                updated_list=[new_amount,new_category,new_type,new_date]
                transactions.append(updated_list)
                with open("C:/Users/dinuk/OneDrive/Desktop/Test/financetracker.json","w") as file:
                    json.dump(transactions,file)
                    if type=="income":
                        add_income.append(new_amount)
                        print(add_income)
                    else:
                        add_expense.append(new_amount)
                    print(add_expense)
                    print("saved successfully")
                    print(transactions)
                    break
            elif save_updated_transaction.lower()=='no':
                print("not save")
                break
            else:
                print("Invalid input.Please enter yes or no")
                continue
    except FileNotFoundError:
        print("file not found")
    

def delete_transaction():
    print("4.Delete transaction.")
    try:
        with open("C:/Users/dinuk/OneDrive/Desktop/Test/financetracker.json","r") as file:
            transactions=json.load(file)
        while True:
            try:
                print("Take the first as 0")
                s_list=int(input("Enter list index you want to delete: "))
                if s_list>=len(transactions) or s_list<0:
                    print("Your input is not in transactions list")
                    continue
                else:
                    pass 
                print("Take the first element index as 0")
                delete_item=int(input("Enter index you want to delete: "))
                if delete_item>=len(s_list) or delete_item<0:
                    print("Your input is not in list")
                    continue
                else:
                    break
            except ValueError:
                print("invalid input")
        while True:
            try:
                remove_item=str(input("Do you want to remove item yes or no: "))
                if remove_item=='yes':
                    del transactions[s_list][delete_item]
                    print("item remove successfully")
                    print(transactions)
                    break
                elif remove_item=='no':
                    print("item not remove :")
                    break
            except:
                print("invalid input")
    except:
        print("file not found")

def display_summary():
    print("5.display summary.")
    try:
        with open("C:/Users/dinuk/OneDrive/Desktop/Test/financetracker.json","r") as file:
            transactions=json.load(file)
            total_income=sum(add_income)
            print("total income =",total_income)
            total_expense=sum(add_expense)
            print("total expense =",total_expense)
    except FileNotFoundError:
        print("file not found")

def main_menu():
    while True:
        print( "Finance Tracker.")
        print("1.Add transaction.")
        print("2.View transactions.")
        print("3.Update transaction.")
        print("4.Delete transaction.")
        print("5.display summary.")
        print("6.Exit.")

        selection=input("Enter your selection(1-6): ")
        if selection == '1':
            add_transaction()
            
        elif selection == '2':
            view_transactions()
            
        elif selection == '3':
            view_transactions()
            update_transaction()
        
        elif selection == '4':
            view_transactions()
            delete_transaction()
        
        elif selection == '5':
            display_summary()
        
        elif selection == '6':
            print("Exiting the program.")
            break 
        else:
            print("Enter integer number betweeen 1 and 6. ")

if __name__ == "__main__":
    main_menu()
