print("Hello World")

print("Is this all right?")

previous = 0
current = 1
i = 0
while i < 20:
    print(current)
    temp = previous
    previous = current
    current = temp + current
    i += 1

def print_grade(midterm, final):
    total = midterm + final
    if total >= 90:
        print("You get an A")
    elif total >= 80:
        print("You get an B")
    elif total >= 70 :
        print("You get an C")
    elif total >= 60:
        print("You get an D")
    else: print("You fail")

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)