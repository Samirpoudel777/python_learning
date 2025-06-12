# # def square(sq):
# #     print(f"the square of the number is {sq*sq}")
# # square(9)


# # write a program of function max_of_three number and return largest numbers
# def max_of_three(first,second,third):
#     if first>second>third:
#         return first;
#     elif second>first>third:
#         return second;
#     else:
#         return third;
# print("the largest number is ", max_of_three(4,5,6))

# # 
# def fullname(firstname,lastname):
#     return firstname+" "+lastname
# x=fullname("nabin","paudel")
# print(x)

# write a python program to create function name percentage and pass the marks of english, nepali ,social ,computer and find the percenatege
# def marks(english,nepali,computer,social):
#     total =  english+nepali+computer+social
#     percent = (total/400)*100
#     return percent
# print(marks(99,99,99,99))
# def positive_negative(number):
#     if number<0:
#         print("the number is negative")
#     elif number>0:
#          print("the number is positive")
#     else:
#         print("the number zero")
# print(positive_negative(0))

# ternary operation
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(check_even_odd(7))  # Output: Odd

# def check_postive_negative(num):
#     return "Postive" if num > 0 else "Negative" if num<0 else "zero"
# print(check_even_odd(0))


# 2! = 2*1
# 3 = 3*2*1
# # 4! = 4*3*2*1
# # 5! = 5*4*3*2*1

# def factroial(num):
#     fact=1;
#     for i in range(1,num+1):
#         fact = fact*i;
#     return fact;
    
# print(factroial(999999))