msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"
operators = ["+", "-", "*", "/"]

M = float()
while 1:

    try:
    
        calc = input(msg_0)

        x, ope, y = calc.split()

        if y == "M":
            x, y = float(x), M

        else:
            x, y = float(x), float(y)
            
        if ope not in operators:
            print(msg_2)
        else:
            if ope == "+":
                print(x + y)
                store = input(msg_4)
                if store == "y":
                    M = x + y
                continue_ = input(msg_5)

            elif ope == "-":
                print(x - y)
                store = input(msg_4)
                if store == "y":
                    M = x - y
                continue_ = input(msg_5)
            elif ope == "*":
                print(x * y)
                store = input(msg_4)
                if store == "y":
                    M = x * y                
                continue_ = input(msg_5)
            elif ope == "/":
                try:
                    print(x / y)
                    store = input(msg_4)
                    if store == "y":
                        M = x / y
                    continue_ = input(msg_5)
                except ZeroDivisionError:
                    print(msg_3)
            

            if continue_ == "n":
                break
            

    except ValueError:
        
        print(msg_1)
