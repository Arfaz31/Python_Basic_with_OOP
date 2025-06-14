# def func(name, *args):
#     sum =0
#     print(args[1])
#     for i in args:
#         sum += i
#     return sum

# result = func("abc", 1, 2, 3, 4, 5)
# print(result)


# def square(num):
#     return num**2


#global and local scope

amount = 100 
def func(name, *args):
    global amount
    amount =500
    print(amount)

    func("hardik")
    print(amount)




