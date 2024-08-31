# class student:
#     college_name = "apna college"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks


#     def hello(self):
#         print("wellcome")


# s1 = student("dhruv" , 97)
# print(s1.name, s1.marks, s1.college_name)
# s1.hello()

# # s2 = student("sujal" , 99)
# # print(s2.name, s2.marks, s2.college_name)



class account:
    def __init__(self, bal , acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount 
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was crebited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = account(100000, 12345)
acc1.credit(5000)
acc1.debit(50000)