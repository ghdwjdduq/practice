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

#Prize
year = 1988
total = 50000000
APT = 1100000000
INTEREST = 0.12
while year < 2016:
    total = total * (1 + INTEREST)
    year += 1

if total > APT:
    print("%d원 차이로 동일 아저씨의 말씀이 맞습니다" % (total - APT))
else:
    print("%d원 차이로 미란 아주머니의 말씀이 맞습니다" % (APT - total))

print("I am not doing well enough")


# print_full_name 함수 정의
def print_full_name(first_name,last_name):
    print(last_name + ",", first_name)

# 테스트 코드
print_full_name("윤수", "이")
print_full_name("수민", "이")