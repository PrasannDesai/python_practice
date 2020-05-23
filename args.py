my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = [1, 2, 3, 4, 5, 6]

print(a)
print(b)
print(c)


my_list = [1, 2, 3]
print(*my_list)


def my_sum(*args):
    print(args)
    # result = 0
    # for x in args:
    #     result += x
    # return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(list1, list2, list3))

k = [1, 2, 3, 4]
print(k)
