num=int(input("enter the first number"))
def fact(num):
    return 1 if num <= 1 else num * fact(num-1)

print(f"factorial of {num} is :" ,fact(num))