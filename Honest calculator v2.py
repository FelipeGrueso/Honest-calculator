msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

operators = ["+", "-", "*", "/"]

while 1:

    try:
    
        calc = input(msg_0)

        x, ope, y = calc.split()
        x, y = float(x), float(y)
            
        if ope not in operators:
            print(msg_2)
        else:
            if ope == "+":
                print(x + y)
                break

            if ope == "-":
                print(x - y)
                
            if ope == "*":
                print(x * y)
                break
                
            if ope == "/":
                if y != 0:
                    print(x / y)
                    break
                else:
                    print("Yeah... division by zero. Smart move...")


    except ValueError:
        
        print(msg_1)
