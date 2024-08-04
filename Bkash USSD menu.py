def bkash_menu():
    while True:
        print("Bkash Menu")
        print("(1) Send money")
        print("(2) Cash out")
        print("(3) Mobile Recharge")
        print("(4) Payment")
        print("(5) My Bkash")
        print("(6) Help")
        print("(7) Exit")

        try:
            opt = int(input("Choose option: "))
            print("........................")
            if opt in [1, 2, 3, 4]:
                if opt == 1:
                    transaction_type = "Send money"
                    number = input("Enter  number           : ")

                elif opt == 2:
                    transaction_type = "Cash out"
                    number = input("Enter Agnet number      : ")
                elif opt == 3:
                    transaction_type = "Mobile Recharge"
                    print("")
                    print("Choose Sim Operator: ")
                    print("(1) Robi")
                    print("(2) GP")
                    print("(3) Banglalink")
                    print("(4) Teletalk")
                    print("(5) Airtel")
                    sim_opt = int(input("Enter : "))
                    if sim_opt in [1, 2, 3, 4, 5] :
                        if sim_opt ==1 :
                            sim_name = "Robi"
                        elif sim_opt ==2 :
                            sim_name = "Gp"
                        elif sim_opt == 3 :
                            sim_name = "Banglalink"
                        elif sim_opt == 4:
                            sim_name = "Teletalk"
                        elif sim_opt == 5:
                            sim_name = "Airtel"
                    print("........................")
                    number= input(f"Enter {sim_name} number      : ")
                elif opt == 4:
                    transaction_type = "Payment"
                    number = input("Enter Merchandise number: ")

                balance = 100000
                amount = float(input("Amount                  : "))
                pin = input("Enter your PIN          : ")

                c_balance = balance - amount
                print("........................message............................")
                print(f". {transaction_type} {amount}tk to {number}. Current balance = {c_balance} tk |")
                print("...........................................................")
                print("Thanks for choosing bkash")
                break
            elif opt == 5:
                print("")
                print("Choose option ")
                print("(1) Check Balance")
                print("(2) Statement")
                print("(3) Change pin")
                print("(4) Main Menu")
                print("")
                opt_5 = int(input("Enter : "))
                if opt_5 in [1, 2, 3, 4]:
                    if opt_5 == 1:
                        print("Your current balance is 100000.00 tk")
                    elif opt_5 == 2:
                        print("These are the statements")
                    elif opt_5 == 3:
                        n_pin = int(input("Set new pin : "))
                        print("Your new pin : ",n_pin)
                    elif opt_5 == 4:
                        bkash_menu()

                else:
                    print("Invaild number")
                break
            elif opt == 6:
                print("(1) Call bkash helpline")
                print("(2) Main Menu")
                opt_6 = int(input("Enter (1-2) : "))
                if opt_6 in [1, 2]:
                    if opt_6 == 1:
                        print("Call in 16262")
                    elif opt_6 == 2:
                        bkash_menu()
                break
            elif opt == 7:
                print("Exiting Program\nThanks for choosing bkash")
                break

        except ValueError:
            print("Please enter a valid number.")
            print("")

dial = int(input("Dial for bkash  (247): "))
if dial == 247:
    bkash_menu()
else:
    print("Dial correct number")
