def deposit(accounts, acc_no, amount):
    accounts[acc_no] += amount
    print(f"{amount} deposited to Account {acc_no}.")


def withdraw(accounts, acc_no, amount):
    if amount > accounts[acc_no]:
        print("Insufficient balance!")
    else:
        accounts[acc_no] -= amount
        print(f"{amount} withdrawn from Account {acc_no}.")


def transfer(accounts, from_acc, to_acc, amount):
    if to_acc not in accounts:
        print("Recipient account not found!")
    elif amount > accounts[from_acc]:
        print("Insufficient balance for transfer!")
    else:
        accounts[from_acc] -= amount
        accounts[to_acc] += amount
        print(f"{amount} transferred from Account {from_acc} to Account {to_acc}.")


def account_menu(accounts, acc_no):
    while True:
        print(f"\n--- Account {acc_no} Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            print(f"Current balance: {accounts[acc_no]}")
        elif choice == '2':
            amt = float(input("Enter deposit amount: "))
            deposit(accounts, acc_no, amt)
        elif choice == '3':
            amt = float(input("Enter withdrawal amount: "))
            withdraw(accounts, acc_no, amt)
        elif choice == '4':
            to_acc = int(input("Enter recipient account number: "))
            amt = float(input("Enter amount to transfer: "))
            transfer(accounts, acc_no, to_acc, amt)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice! Try again.")

def main():
    accounts = {
        1001: 5000.0,
        1002: 3000.0,
        1003: 7000.0
    }

    while True:
        print("\n--- Welcome to Simple Bank System ---")
        acc_no = int(input("Enter your account number (0 to exit): "))
        if acc_no == 0:
            print("Exiting program...")
            break
        elif acc_no in accounts:
            account_menu(accounts, acc_no)
        else:
            print("Account not found!")


main()