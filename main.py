def show_balance():
    print (f"Your current balance is: ${balance:.2f}")

def deposit():
    global balance
    try:
        a = int(input("Enter the amount you would like to desposit: "))
    except ValueError:
        print("Please enter a valid number")
        return

    balance += a
    print (f"Now your balance is ${balance:.2f}")

def withdraw():
    global balance
    try:
        b = int(input("Enter the amount you would like to withdraw: "))
    
    except ValueError:
        print("Please enter a valid number")
        return
    balance -= b
    print(f"You took out ${b}, Now your balance is ${balance:.2f}")

def savings():
    global balance, savings_amount
    print("1. Save / 2. Withdraw")
    try:
        user = input("Please pick 1 or 2: ")
    except ValueError:
        ("Please enter 1 or 2")
        return
    
    if user == '1':
        try:
            amount = int(input("Enter the amount you would like to save: "))
        
        except ValueError:
            print("Please enter a valid number")
            return
        
        if amount > balance:
            print("Not enough balance")

        balance -= amount
        savings_amount += amount

        print(f"You took out ${amount} from balance. Now you have ${savings_amount:.2f} in your savings account.")
    
    elif user == '2':
        pass


def budgeting():
    Needs1 = balance * 0.50
    Wants1 = balance * 0.30
    Saved1 = balance * 0.20
    indepth = True

    print (f" Needs: ${Needs1:.2f} / Wants: ${Wants1:.2f} / For savings: ${Saved1:.2f}")
    while indepth:
        indepth = input("Would you like a more detailed rundown on needs/want/savings? (Needs/Wants/Savings/No): ").lower()
        if indepth == 'needs':
            rent = Needs1 * 0.30
            groceries = Needs1 * 0.25
            gas = Needs1 * 0.2
            utilities = Needs1 * 0.15
            healthcare = Needs1 * 0.1
            print((f" Rent: ${rent:.2f} / Groceries: ${groceries:.2f} / Gas: ${gas:.2f} / Utlities: ${utilities:.2f} / Health: ${healthcare:.2f}"))
        elif indepth == 'wants':
            Eatingout = Wants1 * 0.30
            Entertainment = Wants1 * 0.25
            Travel = Wants1 * 0.2
            Shopping = Wants1 * 0.15
            Giftshobbies = Wants1 * 0.1
            print((f" Eating out: ${Eatingout:.2f} / Entertainment: ${Entertainment:.2f} / Travel: ${Travel:.2f} / Shopping: ${Shopping:.2f} / Gifts/hobbies: ${Giftshobbies:.2f}"))

        
        elif indepth == 'savings':
            fund = Saved1 * 0.4
            Invest = Saved1 * 0.3
            Education = Saved1 * 0.2
            Retirement = Saved1 * 0.1
            print((f" Emergency funds: ${fund:.2f} / Investments: ${Invest:.2f} / Education: ${Education:.2f} / Retirement: ${Retirement:.2f}"))
        
        elif indepth == 'no':
            indepth = False




        
    



balance = 0
savings_amount = 0
is_running = True

while is_running:
    print("-- Alexa's Banking Program -- ")
    print('1. Show balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Savings')
    print('5. Budgeting')
    print('6. Exit')

    choice = str(input("Enter your choice 1-6: "))
    print("------------------------")

    options = {
        '1': show_balance,
        '2': deposit,
        '3': withdraw,
        '4': savings,
        '5': budgeting,
    }


    if choice in options:
        options[choice]()
    
    elif choice == '6':
        print("Exiting server...")
        is_running = False
     

print("Thank you")

    
