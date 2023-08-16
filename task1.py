# 1. Python program to check whether the given integer is a multiple of 5 and 7, and 10, 56.
# Note-> Number get from user (eg. a. 35 is multiple of 5 and 7, b. 560 is multiple of 10 and 56)

'''def no_multiple(x):
        if x%5 == 0 and x%7 == 0:
            return True
        elif x%10 == 0 and x%56 == 0:
            return True
        else:
            return False

n = int(input("enter a no"))
k = no_multiple(n)
print(k)'''

# 2. Python program to find the factorial of a number using recursion.
# Note-> Number get from user (eg. user input 5, then output is 120)

'''def factorial(x):
    if x == 0 or x==1:
        return 1
    else:
        return(x*factorial(x-1))

n = int(input("enter a no"))
k = factorial(n)
print(k)'''

#3.  Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length.
# For example:
#   Input:
#  [
#    [1, 2, 3, 4],
#    [5, 6, 7, 8],
#    [9, 10, 11, 12],
#  ]
# Output:
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

'''list1 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

list_transpose = list()

for i in range(len(list1[0])):
    x = list()
    for y in list1:
        x.append(y[i])
    list_transpose.append(x)

print(list_transpose)'''



#4.  Find the even elements from an array. Respectively multiply this element in the array.
#             For example:
# Input:
# example  a. [1, 2, 3, 4, 5], b. [1, 2, 3, 4, 5, 6]
# Output
# a. [4,8], b. [4,8,6]
#   (Note: Need one line code, don't use for loop and if statement)

'''x = [1,2,3,4,5,6]
y = [i*2 for i in x if i%2==0]
print(y)'''

# 5. Write a program.
# For example:
#     Input
#     [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
#     Output
#     [56.2, 51.7, 55.3, 52.5, 47.8]

'''def nan_remove(x):
    y = [i for i in x if not isinstance(i, float) or not math.isnan(i)]
    return y

import math

x = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
y = nan_remove(x)
print(y)'''


# 6. Flatten a list using list comprehension and for loop.
# For example:
#    Input:
#    [[1,2,3], [4,5,6], [7,8,9]]
#    Output:
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [j for i in list1 for j in i]
print(list2)'''

'''list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = []
for i in list1:
    for j in i:
        list2.append(j)
print(list2)'''


# 7.    A
#      B C
#     D E F
#    G H I J
#   K L M N O
#  P Q R S T U
# V W X Y Z [ \


'''def pattern1(n):
    letter1 = ord('A')
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        letters = " ".join(chr(letter1 + j) for j in range(i))
        print(spaces + letters)
        letter1 += i

k = int(input("Enter the number of rows: "))
pattern1(k)'''


# 8. Write a code to create a below pa:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# -> Note: Get value from user(eg. user input 4 then result be same as below:
#   *
#  * *
# * * *
#  * *
#   *
# )

'''def pattern2(height):
    for i in range(1,((height//2)+2)):
        spaces = " "*((height//2)-i+1)
        stars = "* "*i
        print(spaces + stars)

    for i in range(height//2,0,-1):
        spaces = " "*((height//2)-i+1)
        stars = "* "*i
        print(spaces + stars)

x = int(input("enter a no"))
k = pattern2(x)
print(k)'''


# 9. # write program to create blow pattern :
# # 5432112345
# # 5432  2345
# # 543    345
# # 54      45
# # 5        5
# -> Note: Get value from user(eg. user input 10 then result be same as below:
# 1098765432112345678910
# 1098765432  2345678910
# 109876543    345678910
# 10987654      45678910
# 1098765        5678910
# 109876          678910
# 10987            78910
# 1098              8910
# 109                910
# 10                  10
# )

'''def pattern3(n):
    for i in range(n, 0, -1):
        a = "" * (n - i)
        b = "".join(str(j) for j in range(n, n - i, -1))
        c = " " * (n-i) * 2
        d = "".join(str(j) for j in range(n - i + 1, n + 1))
        row = a + b + c + d
        print(row)

x = int(input("Enter a number: "))
pattern3(x)'''


# 10. # write program to create blow pattern :
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *
# -> Note: Get value from user(eg. user input 4 then result be same as below:
#   *
#  * *
# *   *
#  * *
#   *

'''def pattern_4(height):
    for i in range(1,height):
        space = " "*(height-1-i)
        stars = "* "*i
        if i != 1:
            stars1 = "* "+ ("  "*(i-2) ) + "*"
            print(space + stars1)
        else:
            print(space + stars)

    for i in range(height-2,0,-1):
        space = " "*(height-i-1)
        stars = "* "*i
        if i != 1:
            stars1 = "* "+ ("  "*(i-2) ) + "*"
            print(space + stars1)
        else:
            print(space + stars)

n = int(input("enter a no"))
k = pattern_4(n)
print(k)'''

# 11. write program to create blow pattern :
#     *
#   *   *
# *   *   *
#   *   *
#     *
# -> Note: Get value from user(eg. user input 8 then result be same as below:
#         *
#       *   *
#     *   *   *
#   *   *   *   *
# *   *   *   *   *
#   *   *   *   *
#     *   *   *
#       *   *
#         *

'''def pattern5(height):
    for i in range(1,((height//2)+2)):
        spaces1 = " "*((height//2)-i+1)*2
        stars = " *  "*i

        print(spaces1 + stars)

    for i in range(height//2,0,-1):
        spaces = " "*((height//2)-i+1)*2
        stars = " *  "*i
        print(spaces + stars)

x = int(input("enter a no"))
k = pattern5(x)
print(k)'''




