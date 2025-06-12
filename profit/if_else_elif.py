math =float(input("enter your marks"))
science =float(input("enter your marks"))
nepali =float(input("enter your marks"))
social =float(input("enter your marks"))
optional =float(input("enter your marks"))
totalmarks = math + science + nepali + social + optional;
percentage= totalmarks*100/500;
if math>=40 and science>=40 and nepali>=40 and optional>=40 and social>=40:
    print("pass")
else:
    print("fail")
    
if percentage>=90:
    print("A+")
    print("outstanding")
elif percentage>=80:
    print("A")
    print("excellent")
elif percentage>=70:
    print("B+")
    print("very good")
elif percentage>=60:
    print("B")
    print("good")
elif percentage>=50:
    print("C+")
    print("not bad")
else:
    print("fail")
    



