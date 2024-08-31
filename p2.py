import p1

n1 = int(input("Enter the number of N1:"))
n2 = int(input("Enter the number of N2:"))


calculater = int(input('''enter your choice 
                       1.addition
                       2.subtraction
                       3.multiplication
                       4.devision
                       5.max number
                       6.min number
                       7.percentage'''))    


def get_calculator(calculater):
    match calculater:
        case "addition":
            return p1.addnumber
        case "sub":
            return p1.subnum
        case "mul":
            return p1.mulnum
        case "div":
            return p1.div
        case "max":
            return p1.max
        case "min":
            return p1.min
        case "per":
            return p1.per
        case _:
            return"invalid"
        
print(get_calculator(calculater))