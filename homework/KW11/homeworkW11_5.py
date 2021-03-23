# quiz 3.1
given_list = [1, 3, 5, 7, 9, 15, 20]
num = int(input("Enter the number you want to search in list: "))


def recursion(num):
    if num in given_list:
        print("Yes, belongs")
    else:
        print("No doesn’t belong")


def iteration(num):
    for i in range(len(given_list)):
        if num in given_list:
            return print("Yes, belongs")
        else:
            return print("No doesn’t belong")


recursion(num)
iteration(num)
