english = float(input("enter your marks in english:"))
math = float(input("enter your marks in math:"))
science = float(input('enter your marks in science:'))
social = float(input("enter you marks in social:"))
computer = float(input("enter your marks in computer:"))

total_marks = math+science+computer+social+english
print(total_marks)
percentage = (total_marks*100)/500
print(f"the percentage is {percentage}")
