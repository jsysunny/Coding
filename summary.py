#2
# 프로그램이란 문제 해결을 위해 필요한 데이터를 변수에 저장하고 처리방식(명령어)과 명령어들의
# 순서를 결정(알고리즘)하는 것의 집합
# 프로그램 = 데이터(data) + 명령어(instruction)

# 폰 노이만 아키텍처 
# 입력장치 -> cpu(제어장치 /산술 논리장치/ 메모리) -> 출력장치

# 데이터 (Data, 자료) / 데이터 타입(data type, 자료형) - 숫자형(정수, 실수), 문자열, 불리언,리스트,딕셔너리,클래스
# 변수(variable) 저장 위치는 컴퓨터의 ram(주기억장치, 메인메모리)  저장 위치를 주소로 기억
# 변수 (숫자로 시작 불가, 미리 예약된 이름 사용 불가, 공백 사용 불가)

#4
# 리스트 (값 변경 가능)
# del clovers[1] /clovers.remove("클로버1")
# clovers.insert(3,"클로버3") / clovers.extend(["클로버4", "클로버5", "클로버6"])

# 딕셔너리
# clover.get("번호") -> 9

#7
def scope_test():
    #global a -> 함수 호출 후 a 값도 1
    a=1
    print("scope_test() 함수 안의 a 값은", a)
a=0
print("scope_test() 함수 밖의 a 값은",a) #->0
scope_test() #->1
print("scope_test() 함수 호출 후 a 값은",a) # ->0

# 8 - id 함수
# 선택 정렬
# 하나만 정렬
c=[21,10,11,15,13]
mina=c[0]
minx=0
for i in range(0,4):
    if mina>c[i]:
        mina=c[i]
        minx=i
temp=c[0]
c[0]=c[minx]
c[minx]=temp
# c=[10,21,11,15,13]

for i in range(0,4):
    mina=c[i]
    minx=i
    for j in range(i+1,4):
        if c[i]>c[j]:
            mina=c[j]
            minx=j
    temp=c[i]
    c[i]=c[j]
    c[j]=temp
# c=[10,11,13,15,21]


# 9 10 클래스
# 절차적 프로그래밍(Procedural programming) -oop에 비해 상대적으로 처리 속도 빠름/유지 보수 어렵
# 객체 지향 프로그래밍(OOP)
# 클래스 멤버 (클래스 내, 클래스 메소드 외부에서 선언 ) ex) name="아이유"
# 인스턴스 멤버 (클래스 내, 클래스 메소드 내부에서 선언) ex) self.name="아이유"

class Cvalue:
    def __init__(self):
        self.lista=[]
    def add(self,num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)
def plus(a,b):
    return a+b

if __name__=="__main__":
    p1=Cvalue()
    p1.add(1)
    p1.fprint()
# 이거를 mex1으로 저장

import mex1
p2=mex1.Cvalue()
p2.add(11)
p2.fprint()
value=mex1.plus(10,20)
print(value)
# plus 만 쓰고 싶으면 form mex1 import plus

# random 모듈
import random
animals=['체셔고양이', '오리', '도도새']
print(random.choice(animals)) # 임의로 하나를 선택
print(random.sample(2)) # 임의로 n개를 선택
print (random.randint(1,10))

# 부모 class (super) 자식 class(sub) 상속 받음
# 오버라이딩: 부모 클래스의 메소드를 동일한 이름으로 자식 클래스에서 재정의

class Animal:
    def __init__(self, animal):
        self.animal=animal
    def eat(self):
        print("먹다")
    def move(self):
        print("움직이다")

class Cat(Animal):
    def __init__(self,animal,age):
        super.__init__(animal)
        self. age=age
    def eat(self):
        print("잡식하다")

# 11 tkinter
# Tkinter 소개 및 윈도우 생성
# - Tkinter는 Python에서 GUI 애플리케이션을 만들기 위한 표준 라이브러리
# - Tk 클래스는 최상위 윈도우 객체를 생성
# - Button, Label 등 다양한 위젯을 사용할 수 있음

# Tkinter 라이브러리 임포트
import tkinter as tk

# 1. 기본 윈도우 생성 및 버튼 추가
otk = tk.Tk()  # Tk 클래스로 최상위 윈도우 객체 생성
obtn = tk.Button(otk, text="click")  # Button 위젯 생성
obtn.pack()  # 버튼을 기본 위치(중앙)에 배치
otk.mainloop()  # 메인 이벤트 루프 실행 (창 유지)

# 2. geometry() 메서드 사용
# - geometry("widthxheight+x_offset+y_offset") 형식으로 창의 크기 및 위치 설정 가능
otk = tk.Tk()
otk.geometry("100x150")  # 창의 크기: 100x150
obtn = tk.Button(otk, text="click")
obtn.pack()
otk.mainloop()

otk = tk.Tk()
otk.geometry("100x150+400+400")  # 창의 크기: 100x150, 위치: (400, 400)
obtn = tk.Button(otk, text="click")
obtn.pack()
otk.mainloop()

# 3. 버튼 클릭 시 함수 호출
def hello():
    print("hello there")  # 버튼 클릭 시 "hello there" 출력

otk = tk.Tk()
obtn = tk.Button(otk, text="click me", command=hello)  # 버튼에 command로 함수 연결
obtn.pack()
otk.mainloop()

# 4. 여러 버튼 생성
otk = tk.Tk()
btn1 = tk.Button(otk, text="PUSH1")
btn2 = tk.Button(otk, text="PUSH2")
btn3 = tk.Button(otk, text="PUSH3")
btn1.pack()  # 첫 번째 버튼 배치
btn2.pack()  # 두 번째 버튼 배치
btn3.pack()  # 세 번째 버튼 배치
otk.mainloop()

# 5. Label 위젯 생성
otk = tk.Tk()
label1 = tk.Label(otk, text="적", bg="red", width=20)  # 빨간색 배경
label2 = tk.Label(otk, text="녹", bg="green", width=20)  # 초록색 배경
label3 = tk.Label(otk, text="파", bg="blue", width=20)  # 파란색 배경
label1.pack()  # 첫 번째 라벨 배치
label2.pack()  # 두 번째 라벨 배치
label3.pack()  # 세 번째 라벨 배치
otk.mainloop()

# 6. Tkinter Entry 위젯과 다양한 배치 관리자를 사용하는 예제
# - Entry: 동적 입력을 위한 위젯
# - StringVar(): 입력된 값을 동적으로 저장할 수 있는 변수
# - pack(), grid(), place() 메서드를 사용해 위젯의 위치를 조절할 수 있음

import tkinter as tk

# 1. Entry 위젯 생성 및 사용 (문자 동적 입력)
oroot = tk.Tk()
ostring = tk.StringVar()  # 동적 문자열 변수 생성

# Entry 위젯에 ostring 변수를 연결 (입력된 데이터가 ostring에 저장됨)
oentry = tk.Entry(oroot, textvariable=ostring)
oentry.pack()

# Label 위젯에 Entry에서 입력된 데이터를 표시
olabel = tk.Label(oroot, textvariable=ostring)
olabel.pack()

oroot.mainloop()

# 2. Geometry Manager (배치 관리자) 사용
# pack(), grid(), place() 메서드를 사용해 다양한 방식으로 위젯 배치 가능

# pack() 메서드: 위젯을 순서대로 배치 (좌우상하 지정 가능)
oroot = tk.Tk()
oroot.geometry("200x100+600+300")  # 창 크기 및 위치 지정
obtn1 = tk.Button(oroot, text="PUSH1")
obtn2 = tk.Button(oroot, text="PUSH2")
obtn3 = tk.Button(oroot, text="PUSH3")

obtn1.pack(side="left")  # 왼쪽 정렬
obtn2.pack(side="right")  # 오른쪽 정렬
obtn3.pack(side="top")  # 상단 정렬

oroot.mainloop()

# grid() 메서드: 행(row)과 열(column) 기준으로 위젯 배치
oroot = tk.Tk()
oroot.geometry("200x100")
obtn1 = tk.Button(oroot, text="PUSH1")
obtn2 = tk.Button(oroot, text="PUSH2")
obtn3 = tk.Button(oroot, text="PUSH3")

obtn1.grid(row=0, column=0)  # 0행 0열에 배치
obtn2.grid(row=1, column=1)  # 1행 1열에 배치
obtn3.grid(row=0, column=4)  # 0행 4열에 배치

oroot.mainloop()

# place() 메서드: 절대 좌표 (x, y)로 위젯 배치
oroot = tk.Tk()
oroot.geometry("200x100")
obtn1 = tk.Button(oroot, text="PUSH1")
obtn2 = tk.Button(oroot, text="PUSH2")
obtn3 = tk.Button(oroot, text="PUSH3")

obtn1.place(x=10, y=60)  # x=10, y=60 위치에 배치
obtn2.place(x=140, y=60)  # x=140, y=60 위치에 배치
obtn3.place(x=80, y=10)  # x=80, y=10 위치에 배치

oroot.mainloop()

# Tkinter 이벤트, 바인딩, 라디오 버튼, 체크 버튼, 이미지, 옵션 메뉴 예제

import tkinter as tk

# 1. 버튼 이벤트 처리
def order():
    print("주문하세요")  # 버튼 클릭 시 출력

root = tk.Tk()
btn = tk.Button(root, text="주문", command=order)  # command로 함수 연결
btn.pack()
root.mainloop()

# 2. 바인딩 (binding) 사용
def msg():
    print("start tkinter")

root = tk.Tk()
mlabel = tk.Label(root, text="시작해볼까")
mlabel.pack(side="top")
mbutton = tk.Button(root, text="시작버튼", command=msg)
mbutton.pack(side="bottom")
root.mainloop()

# 3. 라디오 버튼 사용
root = tk.Tk()
radio_value = tk.IntVar()  # 정수형 변수 생성
radio_value.set(1)  # 기본값 설정

lunch = {0: "한식", 1: "일식",2: "중식"}
orb1 = tk.Radiobutton(root, text=lunch[0], variable=radio_value, value=0)
orb2 = tk.Radiobutton(root, text=lunch[1], variable=radio_value, value=1)
orb3 = tk.Radiobutton(root, text=lunch[2], variable=radio_value, value=2)
orb1.pack()
orb2.pack()
orb3.pack()

def buy():
    value = radio_value.get()
    print(lunch[value])

obtn = tk.Button(root, text="주문", command=buy)
obtn.pack()
root.mainloop()

# 4. 체크 버튼 사용
root = tk.Tk()
coffee = {0: "아메리카노", 1: "라떼", 2: "카푸치노", 3: "에스프레소"}
check_value = {}

for i in range(len(coffee)):
    check_value[i] = tk.BooleanVar()  # 체크박스 상태 저장
    ocheckbutton = tk.Checkbutton(root, text=coffee[i], variable=check_value[i])
    ocheckbutton.pack(anchor="w")

def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(coffee[i])

tk.Button(root, text="주문", command=buy).pack()
root.mainloop()

# 5. 이미지 추가
root = tk.Tk()
root.geometry("200x100")
img1 = tk.PhotoImage(file="pizzasb2.png")  # 이미지 파일 불러오기
olabel = tk.Label(root, image=img1)  # Label에 이미지 추가
olabel.place(x=-20, y=-20)  # 이미지 좌표 설정
obutton1=tkinker.Button(root,text="PUSH1")
obutton2=tkinker.Button(root,text="PUSH2")
obutton3=tkinker.Button(root,text="PUSH3")
obutton1.place(x=10,y=60)
obutton1.place(x=140,y=60)
obutton1.place(x=80,y=10)
root.mainloop()

# 6. 옵션 메뉴
root = tk.Tk()
options_list = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar()
selected_option.set(options_list[0])  # 기본값 설정

option_menu = tk.OptionMenu(root, selected_option, *options_list)  # 옵션 메뉴 생성
option_menu.pack()
root.mainloop()


# 12
# 여러 줄 주석처리/해제 - ctrl / 
# 여러 줄 탭처리/ 해제 - tab, shift tab

# 파일
"""
\n - new license
\t- tap
\b - backspace
\' - 작은 따옴표
\"" - 큰 따옴표
\r - 커서를 현재줄의 맨 앞으로 이동
"""
# 디렉토리 확인
import os 
print(os.getcwd())

# 파일 쓰기
f = open("F:/rokey/ch12/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일 내용 추가
path = "F:/rokey/ch12/file1.txt"
f = open(path,'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일 읽기
# f.readline()  파일을 line을 읽어서 결과값을 반환
path = "./ch12/file1.txt"
f = open(path, 'r')
line = f.readline()
print(line)
f.close()

#f.readlines() 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 반환
path = "F:/rokey/ch12/file1.txt"
f = open(path, 'r')
lines = f.readlines()
accountlist=[]
accountDict={}
for line in lines:
    print(line, end='')
    newlist=line.split(' ') # 각 라인을 빈 space 하나로 나누어 리스트로 저장
    print(newlist)
    accountlist.append(line[5:18])
    accountDict[newlist[0]]=newlist[1]
for key, value in accountDict.items():
    print(key,":",value)
f.close()

# f.read() - 파일의 내용 전체를 문자열로 반환
path = "F:/rokey/ch12/file1.txt"
f = open(path, 'r')
data = f.read()
print(data)
f.close()

with open("test.txt", "w") as file:
    file.write("Hello, World!")
print(file.closed) # true

file = open("data.txt", "w")
file.write("Python")
file.close()
file = open("data.txt", "r")
print(file.read())
file.close()

pizza_menu = {
    "페퍼로니 피자": 3000,
    "치즈 피자": 3200,
    "콤비네이션 피자": 3500
}
f = open("F:/rokey/ch12/pizza_file1.txt", 'w', encoding='utf-8')
for key, value in pizza_menu.items():
    f.write(f"{key} :{value}\n")
f.close()

pizza_menu_add = {
    "불고기 피자": 3600,
    "해산물 피자": 3800
}
f = open("F:/rokey/ch12/pizza_file1.txt", 'a', encoding='utf-8')
for key, value in pizza_menu_add.items():
    f.write(f"{key} :{value}\n")
f.close()

# 13
# 예외처리
# 모든 예외의 공통 기본 클래스: BaseException •실행 중 감지되는 예외의 기본 클래스: Exception
# Typeerror는 자료형이 틀렸을때 / Valueerror 자료형은 맞지만 값이 틀렸을때
# typeerror - int("2"+2) , len(123) / valueerror- int("문자열") 
# typeerror 들어오는게 틀림/ valueeroor 들어오는게 맞지만 나가는게 틀림
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try: 
    f = open('myfile.txt') 
    s = f.readline() 
    i = int(s.strip()) 
except OSError as err: 
    print("OS error:", err) 
except ValueError: 
    print("Could not convert data to an integer.") 
except Exception as err: 
    print(f"Unexpected {err=}, {type(err)=}")

try:
    x = int("abc")
except ValueError:
    print("ValueError occurred!")
except (TypeError,NameError):
    print(" ")
finally:
    print("Execution finished.") # finally는 무조건 나옴

try:
    raise KeyError("Key is missing!")
except KeyError as e:
    print(type(e), e)

# 람다
add = lambda x, y: x + y
print(add(3, 5))

numbers=[1,2,3,4,5]
def square(x):
    return x**2
squared_numbers=map(square,numbers)
squared_numbers1=map(lambda x:x**2, numbers)
print(list(squared_numbers))
print(list(squared_numbers1))

#14
# 정규표현식
# [] 문자 [abc] a,b,c 중 한개의 문자와 매치 [a-c] 
# [a-zA-z] 모든 알파벳 [0-9] 모든 숫자 [^0-9] ^:not /숫자가 아닌 문자만 매치
# \d - 숫자와 매치. [0-9]와 동일한 표현식
# - \D - 숫자가 아닌 것과 매치. [^0-9]와 동일한 표현식
# - \s - 화이트스페이스(whitespace) 문자와 매치. [ \t\n\r\f\v]와 동일한 표현식. 맨 앞의 빈칸은 공백 문자(space)를 의미
# - \S - 화이트스페이스 문자가 아닌 것과 매치. [^ \t\n\r\f\v]와 동일한 표현식
# - \w - 문자+숫자(alphanumeric)와 매치. [a-zA-Z0-9_]와 동일한 표현식
# - \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치. [^a-zA-Z0-9_] 동일한 표현식

# a.b a와 b사이 어떤 문자가 들어가도 된다는 의미 단, \n은 불가
# a[.]b 는 말그대로 .문자가 쓰여야 매치

# ca*t a가 0부터 무한대까지 반복될 수 있음
# ca+t a가 1부터 무한대 (무조건 한번은 쓰여야)

#{m,n} m부터 n까지인 문자 매치 (m이상 n이하)
# {1,}==+ , {0,}==*
#ca{m}t 반드시 a m번 반복
#ab?c ->{0,1} 있어도 되고 없어도 됨

# match() - 문자열과 처음부터 정규식과 매치되는지 조사
# search()- 문자열 전체를 검색하여 정규식과 매치되는지 조사
# findall()- 정규식과 매치되는 모든 문자열을 리스트로 리턴
# finditer()- 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴
#match search는 정규식과 매치될때, match객체를 리턴하고 매치되지 않을 경우 none으로 리턴
# match 객체 종류 : group, start, end, span

import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m)
#<re.Match object; span=(0, 6), match='python'>
m1 = p.match("3 python")
print(m1)
# None

"""
p = re.compile(정규표현식)
m = p.match( '조사할 문자열' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
"""

import re
p = re.compile('[a-z]+')
m = p.search("python")
print(m)
#<re.Match object; span=(0, 6), match='python'>
m1 = p.search("3 python")
print(m1)
#<re.Match object; span=(2, 8), match='python'>
result = p.findall("life is too short")
print(result)
# ['life', 'is', 'too', 'short']
result = p.finditer('life is too short')
print(result)
# <callable_iterator object at 0x01F5E390>
for r in result: print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>

m = p.match("python")
m.group() #'python'
m.start() #0
m.end()   #6 
m.span()  #(0,6)

import re
pattern = r'(ab)+'
text = "ababab"
match = re.match(pattern, text)
print(match.group())

import re
pattern = r'\w+'
text = "Hello, World!"
print(re.findall(pattern, text))

import re

# 1. DOTALL(S) 옵션: .(dot)이 줄바꿈 문자(\n)를 포함하여 모든 문자와 매치되도록 함
# 일반적인 정규식에서 .은 줄바꿈을 제외한 모든 문자와 매치됨
p = re.compile('a.b')
m = p.match('a\nb')
print(m)  # 결과: None (줄바꿈 문자와 매치되지 않음)

# re.DOTALL 옵션 사용
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)  # 결과: <re.Match object; span=(0, 3), match='a\nb'> (줄바꿈도 매치됨)


# 2. IGNORECASE(I) 옵션: 대소문자를 구분하지 않고 매치
p = re.compile('[a-z]+', re.I)
print(p.match('python'))  # 결과: <re.Match object; span=(0, 6), match='python'>
print(p.match('Python'))  # 결과: <re.Match object; span=(0, 6), match='Python'>
print(p.match('PYTHON'))  # 결과: <re.Match object; span=(0, 6), match='PYTHON'>


# 3. MULTILINE(M) 옵션: ^, $ 메타 문자가 각 줄의 처음과 끝을 의미하도록 함
data = """python one
life is too short
python two
you need python
python three"""

# 기본 정규식
p = re.compile("^python\s\w+")
print(p.findall(data))  # 결과: ['python one']

# re.MULTILINE 옵션 사용
p = re.compile("^python\s\w+", re.MULTILINE)
print(p.findall(data))  # 결과: ['python one', 'python two', 'python three']


# 4. VERBOSE(X) 옵션: 주석과 여러 줄로 정규식을 작성할 수 있어 가독성이 향상됨
# 일반 정규식
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# re.VERBOSE 옵션 사용
charref_verbose = re.compile(r"""
    &[#]                 # Start of a numeric entity reference
    (
        0[0-7]+          # Octal form
        | [0-9]+         # Decimal form
        | x[0-9a-fA-F]+  # Hexadecimal form
    )
    ;                    # Trailing semicolon
    """, re.VERBOSE)
print(charref_verbose)  # 결과: re.Pattern 객체가 생성됨


# 5. 역슬래시 문제와 raw string 사용법
p = re.compile('\\section')  # 의도한 대로 \\section을 찾을 수 있음
print(p.pattern)  # 결과: \\section

# raw string 사용 시 역슬래시 두 개를 하나로 줄여서 표현 가능
p = re.compile(r'\section')
print(p.pattern)

print(p.pattern)  # 결과: \\section
# 일반 문자열에서 \section은 \s가 공백 문자로 해석됨
p = re.compile('\\\\section')  # 의도한 대로 \\section을 찾을 수 있음
print(p.pattern)  # 결과: \\section

# raw string 사용 시 역슬래시 두 개를 하나로 줄여서 표현 가능
p = re.compile(r'\\section')
print(p.pattern)  # 결과: \\section

#15
# 이터레이터, 제너레이터
nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))

a = [1, 2, 3] 
ia = iter(a) 
for i in ia:
    print(i) 
for i in ia: 
    print(i)
# stopiteration 예외 미 발생, 첫번째 for문에서는 1,2,3 나오지만 두번째 for문은 아무것도 안나옴

class MyItertor:
    def __init__(self, data):
        self.data = data
        self.position = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyItertor([1,2,3])
    for item in i:
        print(item)

class ReverseItertor:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.position <0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

if __name__ == "__main__":
    i = ReverseItertor([1,2,3])
    for item in i:
        print(item)

def mygen():
    for i in range(1, 1000):
        result = i * i
    yield result
gen = mygen()
print(next(gen)) 
print(next(gen)) 
print(next(gen))

gen = (i * i for i in range(1, 1000))

class MyIterator:
    def __init__(self):
        self.data = 1
    def __iter__(self):
        return self
    def __next__(self):
        result = self.data * self.data
        self.data += 1
        if self.data >= 1000:
            raise StopIteration
        return result

import time
def longtime_job():
    print("job start")
    time.sleep(1) # 1초 지연
    return "done"
list_job = [longtime_job() for i in range(5)]
print(list_job[0])

import time
def longtime_job():
    print("job start")
    time.sleep(1) # 1초 지연
    return "done"
list_job = (longtime_job() for i in range(5))
print(next(list_job)) 
# job start
# done

def my_gen():
    yield 1
    yield 2
    yield 3
gen = my_gen()
print(next(gen))
print(next(gen))

def countdown(n):
    while n > 0:
        yield n
        n -= 1
gen = countdown(3)
for x in gen:
    print(x, end=" ")

#16
#스택 (LIFO 후입선출)
#함수 호출 스택
# 웹 브라우저 방문 기록 (뒤로 가기)
# 괄호 검사와 같은 문자열 처리

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return

    def is_empty(self):
        return len(self.stack) == 0

    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return

    def status_stack(self):
        return self.stack


# Stack 사용 예제
s1 = Stack()
print(s1.peak()) # None
s1.pop()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
print(s1.peak())
s1.pop()
print(s1.status_stack())

# 큐(FIFO 선입선출)
# enqueue 큐에 데이터 삽입
# dequeue 큐에서 데이터 제거
# 프로세스 관리(작업대기열)
# BFS 구현

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return

    def is_empty(self):
        return len(self.queue) == 0

    def status_queue(self):
        return self.queue


# Queue 사용 예제
q1 = Queue()
q1.dequeue()
q1.enqueue(1)
q1.enqueue(2)
q1.dequeue()
print(q1.status_queue())
q1.enqueue(3)
q1.enqueue(4)
q1.dequeue()
print(q1.status_queue())

#덱
# 회전 큐(슬라이딩 윈도우)
# 문자열 회문 검사

from collections import deque

dq = deque()  # 덱 생성
dq.append(1)  # dq에 뒤로 데이터 넣기
print(dq)

dq.appendleft(2)  # dq에 앞으로 데이터 넣기
print(dq)

dq.pop()  # 마지막 데이터 꺼내기
print(dq)

dq.popleft()  # 처음 데이터 꺼내기
print(dq)

#괄호 짝 검사
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


def is_bracket_balanced(s):
    stack = Stack()
    bracket_map = {')': '(', '}': '{', ']': '['}
    opening_brackets = set(bracket_map.values())

    for char in s:
        if char in opening_brackets:
            stack.push(char)
        elif char in bracket_map:
            top = stack.pop()
            if top != bracket_map[char]:
                return False

    return stack.is_empty()

# 테스트
print(is_bracket_balanced("()"))        # True
print(is_bracket_balanced("{[()]}"))    # True
print(is_bracket_balanced("{[(])}"))    # False
print(is_bracket_balanced("{[}"))       # False

# 회전 큐 검사
from collections import deque

def rotate_deque(dq, steps):
    dq.rotate(-steps)  # steps만큼 왼쪽으로 회전
    return dq


# 테스트
dq = deque([1, 2, 3, 4, 5])
print("Before Rotation:", list(dq))
dq = rotate_deque(dq, 2)
print("After Rotation:", list(dq))


#17
# 노드- 하나의 데이터 단위를 나타내는 객체 / 엣지(간선): 두 노드간의 연결 관계를 나타내는 데이터 (연결선)
# 두 노드 사이에 엣지가 있으면, [두 노드는 인접해 있다] 라고 표현함

#차수(degree) : 하나의 노드에 연결된 엣지의 수
#경로(path) : 한 노드에서 다른 노드까지 가는 길(노드들의 순서)

#G=(V,E) V: 노드의 집합, E: 두 노드를 연결하는 간선의 집합
#V = {1, 2, 3, 4, 5}
# E = {(1, 2), (1, 3), (1, 5), (2, 3), (3, 4), (3, 5), (4, 5)}

myGraph={ 'A':[B,C,D], 'B':[A,E], 'C':[A,F,G] , 'D':[A,H] ,'E':[B,I], 'F':[C,J], 'G':[C],'H':[D]
,'I':[E], 'J':[F]}

# DFS 깊이 우선 탐색
def my_dfs(graph,start_node):
    stack=list()
    visited=list()

    stack.append(start_node)

    while stack:
        node=stack.pop()

        if node not in visited:
            stack.extend(reversed(graph[node]))
            visited.append(node)

    print("dfs- ",visited)
    return visited

my_dfs(myGraph,'A')
# dfs- ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']
#   pop   stack          visited
# 1	A	['D', 'C', 'B']	['A']
# 2	B	['D', 'C', 'E']	['A', 'B']
# 3	E	['D', 'C', 'I']	['A', 'B', 'E']
# 4	I	['D', 'C']	['A', 'B', 'E', 'I']
# 5	C	['D', 'G', 'F']	['A', 'B', 'E', 'I', 'C']
# 6	F	['D', 'G', 'J']	['A', 'B', 'E', 'I', 'C', 'F']
# 7	J	['D', 'G']	['A', 'B', 'E', 'I', 'C', 'F', 'J']
# 8	G	['D']	['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G']
# 9	D	['H']	['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D']
# 10 H	[]	['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']

#BFS 너비 우선 탐색
def my_bfs(graph,start_node):
    queue=list()
    visited=list()

    queue.append(start_node)

    while queue:
        node=queue.pop(0)

        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)

    print("bfs -",visited)
    return visited

my_bfs(myGraph,"A")
#bfs - ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#    pop 	queue       	visited
# 1	A	['B', 'C', 'D']	['A']
# 2	B	['C', 'D', 'E']	['A', 'B']
# 3	C	['D', 'E', 'F', 'G']	['A', 'B', 'C']
# 4	D	['E', 'F', 'G', 'H']	['A', 'B', 'C', 'D']
# 5	E	['F', 'G', 'H', 'I']	['A', 'B', 'C', 'D', 'E']
# 6	F	['G', 'H', 'I', 'J']	['A', 'B', 'C', 'D', 'E', 'F']
# 7	G	['H', 'I', 'J']	['A', 'B', 'C', 'D', 'E', 'F', 'G']
# 8	H	['I', 'J']	['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 9	I	['J']	['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# 1 J	[]	['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

#연습문제 답 dfs-[1,2,5,6,3,4] / bfs-[1,2,3,4,5,6]

#18
# 정사각형 그리기 // 직사각형 그리기
import turtle

turtle.mainloop() # turtle.done()
turtle.title("정사각형 그리기")
turtle.setup(410,310)
turtle.bgcolor("beige") #배경색

t=turtle.Turtle()
t.shape("turtle")
t.color("black", "green") # 거북이 경계선, 거북이 색상
t.pencolor("skyblue")
t.pensize(5)

#t.write("거북이")
#t.write("거북이", font=("arial",30,"bold"))
#t.home() # 원래 위치

""" 정사각형
t.fd(70);t.left(90)
t.fd(70);t.left(90)
t.fd(70);t.left(90)
t.fd(70)
"""

""" 직사각형 
t.left(90); t.fd(80)
t.right(90); t.fd(120)
t.right(90); t.fd(80)
t.right(90); t.fd(120)
t.left(180)
"""

""" 다각형
n=int(input("갯수를 입력하세요:" ))
t.beginfill() # 다각형 채우기 시작 
for i in range(n):
    t.right(360/n)
    t.fd(50)
t.endfill()
"""

""" 원 그리기
t.speed(0)
# "fastest":0 / "fast":10 / "normal": 6 / "slow": 3 / "slowest":1
n=60
for i in range(n):
    t.circle(50) # 50은 반지름
    t.right(360/n)
"""

""" 복잡한 도형
n=300
for i in range(n):
    t.fd(i)
    t.right(91)
"""

turtle.exitonclick()

#별 그리기
import turtle
turtle.setup(410,310)
turtle.bgcolor("black")

star=turtle.Turtle()
star.speed(1)
star.pensize(2)

colors=['red','yellow','blue','green','purple']

def drawStar():
    n=5
    for i in range(n):
        star.color(colors[i])
        star.forward(100)
        star.fd(360/5)

drawStar()
star.hideturtle()

turtle.exitonclick()

# 무지개 색 원 그리기
import turtle
turtle.setup(400,150)
turtle.bgcolor("black")

rainbow=turtle.Turtle()
rainbow.speed(0)
rainbow.pensize(2)

colors=['red','orange','yellow','green','blue','navy','purple']

def drawRainbow(radius):
    for color in colors:
        rainbow.color(color)
        rainbow.circle(radius)
        radius+=5

def drawRainbow(radius,x,y):
    for color in colors:
        rainbow.color(color)
        rainbow.penup()
        rainbow.goto(x,y)
        rainbow.pendown()
        rainbow.setheading(90)
        rainbow.circle(radius, 180) # 반원
        x+=7
        radius+=5

drawRainbow(50)
drawRainbow(50,50,0)

rainbow.hideturtle()
turtle.exitonclick()

#19
#pip install pandas
import pandas as pd

data=[10,20,30]
series=pd.Series(data)
print(series)

# 0 10
# 1 20
# 2 30
# dtype: int64

data={'a':10, 'b':20, 'c':30}
# a 10
# b 20
# c 30
# dtype: int64

data=[[1,'Alice',30],[2,'Bob',35],[3,'Charlie',25]]
df=pd.DataFrame(data,colums=['ID','Name','Age'])

data={'ID':[1,2,3], 'Name':['Alice','Bob','Charlie'], 'Age':[30,35,25]}
df= pd.DataFrame(data)
print(df)

#  ID Name Age
# 0 1 Alice 30
# 1 2 Bob 35
# 2 3 Charlie 25

#데이터 로드
df_csv=pd.read_csv('D:/rokey/ch19/data.csv')
# CSV 파일 구조
# 줄 바꿈으로 구분되는 1개 이상의 행(레코드)으로 구성
# 각 행은 1개 이상의 열(필드)로 구성 
# 필드는 큰따옴표로 둘러싸도 됨 (단, 통일성은 있어야 함)

#pip install openpyxl
df_xl=pd.read_excel('D:/rokey/ch19/data.xlsx')
# Excel 파일 구조 
# 파일을 북(book)이라고 함 
# 하나의 북 내부에는 여러 개의 시트(sheet)가 존재
# 각 시트는 행(row)와 열(column)을 가진 2차원 셀(cell)로 구성

# csv 파일
# ID,이름,가격 
# 1,비누,300
# 2,장갑,150 
# 3,마스크,230 
# 4,손수건,400 
# 5,볼펜,200
# 6,건전지,250

#데이터 상위 5행 / 하위 5행
df_csv.head()
df_csv.tail()
# 데이터 요약
df.info()
# 기술 통계 ( count , mean, std, min, 25%, 50% ,75%, max)
df.describe()
# 랜덤 샘플링 / 특정 비율 샘플링
df.sample(2)
df.sample(frac=0.5) # 50%

#열 선택 /추가/행 추가/ 삭제/ 필터링
df['Name']
df['Salary']=[50000,60000,70000]
df.loc[len(df)]=[4, 'David', 40, 60000]
df=df.drop(1) # 1번 행 삭제
filtered=df[df['Age']>30]
#정렬
sorted=df.sort_values(by='Age') #오름차순 age 25, 30 ,35 이런식
#연결
data2={'ID':[5,6], 'Name':['Eve','Frank'], 'Age': [28,33]}
df2=pd.DataFrame(data2)
concated=pd.concat([df,df2])

# ID Name Age Salary
#0 1 Alice 30 50000.0
#2 3 Charlie 25 70000.0 
#3 4 David 40 80000.0 
#0 5 Eve 28 NaN 
#1 6 Frank 33 NaN

#열을 병합하고 싶으면
merged=pd.merge([df,df2])
# -> 인덱스가 0 1 2 3 4 5로 됨

#NaN(결측값, Not a Number) - 정의되지 않는 값, 누락된 값, 모르는 값
#값이 없는 경우 None으로 데이터 입력 가능
#결측치 확인
df.isnull().sum()
#ID 0
#Name 0 
#Age 0
#Salary 2 
#Department 0 
#dtype: int64

meanVal = merged['Salary'].mean()
merged['Salary'] = merged['Salary'].fillna(meanVal)

#중복 데이터 처리
df.duplicated()
# 0 False 
# 1 False 
# 2 False 
# dtype: bool

#중복 제거
df=df.drop_duplicates()

#Numpy -다차원 배열 및 행렬 연산 지원 라이브러리
# pip install numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.shape) # 배열의 모양 
print(arr.dtype) # 데이터 타입

# [1 2 3 4 5]
# (5,) -> 5개라는 뜻
# int64

#0. 0으로 초기화된 배열 
zeros = np.zeros((3, 3)) 
print(zeros) 
#[[0. 0. 0.] ,
# [0. 0. 0.] ,
# [0. 0. 0.]] 

# 1로 초기화된 배열: 
ones = np.ones((2, 4)) 
print(ones) 
# [[1. 1. 1. 1.],
# [1. 1. 1. 1.]]

# 1. 특정 값으로 채운 배열 생성
full = np.full((2, 2), 7)
print(full)
# 실행 결과:
# [[7 7]
#  [7 7]]

# 2. 단위 행렬 생성
identity = np.eye(3)
print(identity)
# 실행 결과:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 3. 난수 배열 생성
random = np.random.rand(3, 3)
print(random)
# 실행 결과 (랜덤 값이므로 예시는 다를 수 있음):
# [[0.98926147 0.25809324 0.38728431]
#  [0.72484548 0.54439084 0.42520048]
#  [0.10259329 0.32706793 0.83867207]]

# 4. 정수 난수 배열 생성
randint = np.random.randint(1, 10, (3, 3))
print(randint)
# 실행 결과 (랜덤 값이므로 예시는 다를 수 있음):
# [[7 7 7]
#  [2 6 5]
#  [1 9 7]]

# 5. 배열 연산
arr = np.array([1, 2, 3, 4])
print(arr + 5)
# 실행 결과: [6 7 8 9]
print(arr * 2)
# 실행 결과: [2 4 6 8]

# 6. 통계 함수
print(arr.sum())
# 실행 결과: 10
print(arr.mean())
# 실행 결과: 2.5
print(arr.max())
# 실행 결과: 4
print(arr.min())
# 실행 결과: 1

# 7. 브로드캐스팅
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])
result = arr1 + arr2
print(result)
# 실행 결과:
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]

# 8. 선형 대수 연산 (행렬 곱)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result_matrix = np.dot(matrix1, matrix2)
print(result_matrix)
# 실행 결과:
# [[19 22]
#  [43 50]]

# 9. 배열 인덱싱 및 슬라이싱
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1, 2])  
# 실행 결과: 6
print(arr[0, :])      
# 실행 결과: [1 2 3]
print(arr[:, 1])      
# 실행 결과: [2 5]

# 10. 조건부 연산 (조건 필터링)
arr = np.array([1, 2, 3, 4, 5])
filtered = arr[arr > 3]
print(filtered)
# 실행 결과: [4 5]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Numpy 배열 저장 및 로드
arr = np.array([1, 2, 3, 4, 5])
np.save('array.npy', arr)  # 배열 저장
loaded = np.load('array.npy')  # 배열 로드
print(loaded)
# 실행 결과: [1 2 3 4 5]

# 2. Numpy와 Pandas 통합 사용
df = pd.DataFrame(arr, columns=['Value'])
print(df)
# 실행 결과:
#    Value
# 0      1
# 1      2
# 2      3
# 3      4
# 4      5

# 3. Matplotlib 기본 사용법 (선 그래프)
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()  # 실행 결과: 선 그래프가 출력됩니다.

# 4. 다양한 그래프 종류

# Bar Chart (막대 그래프)
categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]
plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()  # 실행 결과: 막대 그래프가 출력됩니다.

# Histogram (히스토그램)
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.show()  # 실행 결과: 히스토그램이 출력됩니다.

# Scatter Plot (산점도)
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
plt.scatter(x, y, color="green")
plt.title("Scatter Plot")
plt.show()  # 실행 결과: 산점도가 출력됩니다.

# Pie Chart (파이 차트)
sizes = [15, 30, 45, 10]
labels = ["Group A", "Group B", "Group C", "Group D"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
plt.show()  # 실행 결과: 파이 차트가 출력됩니다.

# Box Plot (박스 플롯)
data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()  # 실행 결과: 박스 플롯이 출력됩니다. (min, 25%, 50%, 75% ,max)

# 5. 그래프 커스터마이징
# 커스터마이징된 Line Plot
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Customized Line Plot")
plt.show()  # 실행 결과: 커스터마이징된 선 그래프가 출력됩니다.

# 축 범위와 눈금 설정
plt.plot(x, y)
plt.xlim(0, 5) #x축 범위 표시
plt.ylim(0, 40) # y축 범위 표시
plt.xticks(range(1, 5)) # x축 눈금
plt.yticks(range(0, 41, 10)) # y축 눈금
plt.show()  # 실행 결과: 축 범위가 조정된 그래프가 출력됩니다.

# 범례 추가 및 위치 설정
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
x1 = [1, 2, 3, 4]
y2 = [3, 5, 9, 7]
plt.plot(x, y, label="Data 1")
plt.plot(x1, y2, label="Data 2")
plt.legend(loc="upper left")
plt.show()  # 실행 결과: 범례가 있는 그래프가 출력됩니다.

# 그래프 저장
plt.plot(x, y)
plt.savefig("my_plot.png")  # 그래프가 my_plot.png로 저장됩니다.

# Subplot 활용
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].bar(categories, values)
axs[1, 0].scatter(x, y)
axs[1, 1].hist(data)
plt.tight_layout()
plt.show()  # 실행 결과: 여러 그래프가 한 화면에 출력됩니다.

#20 
import statsmodels.api as sm
import pandas as pd

# statsmodels 패키지: 통계적 모델 추정 및 테스트를 위한 Python 라이브러리
# 주요 기능:
# 1. 선형 및 로지스틱 회귀 분석
# 2. 시계열 분석 (ARIMA 모델 포함)
# 3. 통계적 테스트 (가설 검정, 모델 선택 등)
# 4. 데이터 탐색 및 시각화

# 선형 회귀(Linear regression)
# 회귀란 레이블이 포함된 데이터를 통해 생성한 모델에 새로운 데이터를 입력하고 결과 값을 예측하는 것
# 독립 변수와 종속 변수 간의 선형 관계를 모델링하는 기법
# H(x)= Wx+b

# 데이터 준비 및 탐색
# mtcars 데이터셋: 1974년 Motor Trend US Magazine에서 가져온 자동차 데이터셋
# 32종 자동차의 10가지 특성 (mpg: 연비, cyl: 실린더 수, disp: 배기량, hp: 마력 등)
data = sm.datasets.get_rdataset("mtcars").data
print(data.head())  # 데이터의 첫 5행 출력

# 단순 선형 회귀 분석
# mpg(연비)와 hp(마력) 간의 관계를 모델링
X = data['hp']  # 독립 변수: 마력 (hp)
y = data['mpg']  # 종속 변수: 연비 (mpg)

# 상수항 추가 (절편 포함)
X = sm.add_constant(X)

# 선형 회귀 모델 생성 및 학습
model = sm.OLS(y, X).fit()  # OLS(최소제곱법)로 선형 회귀 모델 생성 및 학습

# 결과 출력
print(model.summary())

# 결과 분석:
# No.observations(총 표본 수)
# DF Residuals(잔차의 자유도)
# DF model(독립변수의 개수)

# 1. R-squared (결정계수): 독립 변수가 종속 변수를 얼마나 설명하는지 나타내는 지표 (0 ~ 1)
#    - 1에 가까울수록 설명력이 높음
#    - 예: R-squared가 0.6이면 독립 변수가 종속 변수의 60% 정도를 설명함
# 2. Adj. R-squared (수정된 결정계수): 독립 변수의 개수가 많아질 때 발생하는 R-squared 증가 현상을 조정한 값
#    - 모델의 설명력을 좀 더 정확히 평가하기 위해 사용
# 3. F-statistic (F 검정 통계량): 회귀 모델의 전체적인 유의성을 검정
#    - 회귀 모델의 분산과 오차항의 분산의 비율로 계산
#    - F값이 클수록 모델이 유의미할 가능성이 큼
# 4. Prob (F-statistic): F-통계량에 대한 P-값
#    - 0.05 이하인 경우 모델이 통계적으로 유의미하다고 판단
# 5. AIC (Akaike Information Criterion): 모델의 적합도를 평가하는 기준 (값이 낮을수록 좋은 모델)
# 6. BIC (Bayesian Information Criterion): AIC와 비슷하지만 패널티를 부여하여 모델 평가 성능을 더 정확히 측정( 값이 낮을수록 좋은 모델)
# 7. coef (회귀계수): 각 독립 변수의 계수
#    - 예: const가 30.0989, hp가 -0.0682이면 회귀식은 H(x) = -0.0682 * hp + 30.0989
#    - hp가 1 증가할 때마다 mpg가 0.0682 감소한다고 해석 가능
# 8. std err (표준오차): 계수 추정치의 표준오차 (값이 작을수록 좋음)
# 9. t (t-통계량): 독립 변수와 종속 변수의 상관관계를 평가 (값이 클수록 상관성이 높음)
# 10. P>|t| (P-값): 회귀 계수가 통계적으로 유의미한지 판단 (0.05 이하인 경우 유의미)

# 다중 선형 회귀 분석
# 독립 변수가 여러 개인 경우 (hp, wt: 마력과 중량)
X = data[['hp', 'wt']]  # 독립 변수: 마력 (hp)와 중량 (wt)
y = data['mpg']  # 종속 변수: 연비 (mpg)

# 상수항 추가 (절편 포함)
X = sm.add_constant(X)

# 다중 선형 회귀 모델 생성 및 학습
model = sm.OLS(y, X).fit()

# 결과 출력
print(model.summary())

# 결과 분석 추가:
# 1. 다중 선형 회귀에서는 여러 독립 변수들이 종속 변수에 어떻게 영향을 미치는지 확인할 수 있음
# 2. coef 값으로 각 독립 변수의 영향을 확인
#    - 예: wt의 coef가 -3.8778이면 중량이 1 단위 증가할 때 mpg가 3.8778 감소한다고 해석
# 3. P>|t| 값이 0.05 이하인 경우 해당 독립 변수가 통계적으로 유의미


# Python 기반의 머신러닝 라이브러리  
# 다양한 데이터 전처리, 모델링, 평가 도구 제공

# Scikit-learn 주요 특징:  
# 간단하고 일관된 API 제공  
# 공통적 메서드 제공: fit(X, y), predict(X), score(X, y)  
# 통일된 입/출력 형식: Numpy 배열, Pandas 데이터프레임 등 표준화된 데이터 구조  
# 풍부한 알고리즘 지원 (분류, 회귀, 클러스터링 등)  
# 확장성과 다양한 데이터셋 제공  

# 설치 및 환경 설정:  
# 설치 명령어: pip install scikit-learn  
# 임포트: import sklearn as sk  

# scikit-learn 패키지를 활용한 XOR 연산 학습  
# 배타적 논리합(XOR) 설명:  
# 두 입력 중 하나만 참이고, 다른 한 쪽이 거짓일 때 참(True)  
# 모두 참이거나 모두 거짓인 경우는 거짓(False)  

# 필요한 라이브러리 임포트
from sklearn import svm  # SVM (Support Vector Machine) 사용
from sklearn import metrics  # 정확도 계산을 위한 metrics 사용
import pandas as pd  # 데이터 조작을 위한 pandas 사용

# 1. 데이터 직접 입력하고 학습
from sklearn import svm  # SVM (Support Vector Machine) 사용
from sklearn import metrics  # 정확도 계산을 위한 metrics 사용

# 데이터 학습하기
clf = svm.SVC()  # 알고리즘 선택 - SVM 분류 모델
# fit 메서드를 사용해 학습 (학습 데이터와 정답 레이블을 입력)
clf.fit([
    [0, 0],  # 입력 데이터
    [0, 1],
    [1, 0],
    [1, 1]
], 
[ 0, 1, 1, 0]) # 정답 레이블  # 학습(모델링) 완료

# 데이터 예측하기
# predict 메서드를 사용해 테스트 데이터를 예측
pre = clf.predict([
    [0, 1],  # 예측 대상 데이터
    [1, 1]
])  # 예측 수행 (결과 반환)
print(pre)  # 예측 결과 출력

# 결과 확인
ac_score = metrics.accuracy_score([1, 0], pre)  # 예측 결과와 실제 정답 비교하여 정확도 계산
print(f"정답률: {ac_score}")  # 정답률 출력

# 2. 데이터셋 학습 데이터와 레이블 분할 후 학습 
xor_data = [
    [0, 0, 0],  # 입력: (0, 0) → 결과: 0
    [0, 1, 1],  # 입력: (0, 1) → 결과: 1
    [1, 0, 1],  # 입력: (1, 0) → 결과: 1
    [1, 1, 0]   # 입력: (1, 1) → 결과: 0
]

# 데이터프레임 생성
xor_df = pd.DataFrame(xor_data)  # pandas 데이터프레임 생성
data = xor_df.loc[:, :2]  # 입력 데이터 추출
label = xor_df.loc[:, 2]   # 결과 데이터 추출 (정답 레이블)

# 학습 알고리즘 선택 및 모델 생성 (분류 모델)
clf = svm.SVC()  # SVM 분류 모델 생성
clf.fit(data, label)  # 모델 학습 (fit 메서드 사용)

# 예측하기
pre = clf.predict(data)  # 입력 데이터로 예측 수행
print("예측 결과:", pre)  # 예측 결과 출력

# 정확도 확인
ac_score = metrics.accuracy_score(label, pre)  # 정확도 계산
print(f"정답률: {ac_score:.2f}")  # 정답률 출력 (소수점 2자리까지 표시)

# 붓꽃의 품종 분류하기
# sklearn 패키지 내 datasets 모듈을 통해 유명한 붓꽃(Iris) 데이터셋을 로드할 수 있습니다.
from sklearn.datasets import load_iris  # 데이터셋 로드 모듈 임포트
import pandas as pd  # 데이터프레임 처리를 위한 pandas 사용

# 1. Iris 데이터셋 로드
iris = load_iris()  # 데이터셋 로드

# 데이터프레임 생성
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target  # target 열 추가

# target 값을 0, 1, 2 → 'setosa', 'versicolor', 'virginica'로 변환
target_names = {
    0: iris.target_names[0],  # 'setosa'
    1: iris.target_names[1],  # 'versicolor'
    2: iris.target_names[2]   # 'virginica'
}
df['target'] = df['target'].map(target_names)  # 정수형 레이블을 문자열로 변환
print(df.head())  # 데이터프레임의 상위 5개 행 출력
# 실행 결과
# sepal length (cm) sepal width (cm) petal length (cm) petal width (cm) target
# 0 5.1 3.5 1.4 0.2 0
# 1 4.9 3.0 1.4 0.2 0
# 2 4.7 3.2 1.3 0.2 0
# 3 4.6 3.1 1.5 0.2 0
# 4 5.0 3.6 1.4 0.2 0

# 데이터셋을 학습용과 테스트용으로 나누기
from sklearn.model_selection import train_test_split  # 데이터 분할 함수 임포트

# 필요 열 추출
iris_data = df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]
iris_label = df['target']

# 데이터 분할 (80% 학습, 20% 테스트)
train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label, test_size=0.2)

# 학습 및 예측하기
from sklearn import svm, metrics  # SVM과 metrics 임포트
#SVM: 서포트 벡터 머신 / 데이터 집합 내에서 최대 마진을 가진 최적의 선(평면)을 찾아 데이터 분류

# SVM 분류 모델 생성 및 학습
clf = svm.SVC()  # SVC: 서포트 벡터 분류
clf.fit(train_data, train_label)  # 학습 진행

# 테스트 데이터 예측
pre = clf.predict(test_data)  # 예측 수행
print("예측 결과:", pre)  # 예측 결과 출력

# 정확도 확인
ac_score = metrics.accuracy_score(test_label, pre)  # 정확도 계산
print("정답률 =", ac_score)  # 정답률 출력

# Scipy 소개
# Python의 과학 및 공학 계산 라이브러리
# NumPy와 함께 사용되어 데이터 분석 및 수학적 계산에 적합
# 주요 서브모듈:
#   - linalg (선형대수)
#   - optimize (최적화)
#   - stats (통계)
#   - integrate (적분)
#   - sparse (희소 행렬)

# Scipy와 NumPy의 차이점:
# NumPy: 다차원 배열과 기본 연산 제공
# Scipy: 고급 수학 및 과학 계산 기능 제공 (NumPy 위에 구축됨)

# 설치: pip install scipy
# 임포트: import scipy as sp

# 1. 선형 대수 계산 (scipy.linalg)
from scipy.linalg import solve

# Ax = b 형태의 선형 방정식 풀이
# 예제: 3x + 1y = 9, 1x + 2y = 8
A = [[3, 1], [1, 2]]  # 계수 행렬
b = [9, 8]            # 상수 벡터
x = solve(A, b)       # Ax = b 방정식 풀이
print(f"Solution: {x}\n")  # 해 출력

# 2. 최적화 (scipy.optimize)
from scipy.optimize import minimize, root  # 최적화 및 방정식 근 찾기

# 2차 함수 최적화
def f(x):
    return x**2 + 4*x + 4

result = minimize(f, x0=0)  # 초기값 x0=0에서 시작해 함수의 최소값을 찾음
print(f"Optimal value: {result.x}")

# 방정식의 근 찾기 (x^2 - 4 = 0)
def equation(x):
    return x**2 - 4

sol = root(equation, x0=1)  # 초기값 x0=1에서 시작해 방정식의 근을 찾음
print(f"Root: {sol.x}")

# 3. 통계 계산 (scipy.stats)
from scipy.stats import describe

# 데이터 통계 요약
data = [1, 2, 3, 4, 5, 6, 7]  # 샘플 데이터
stats = describe(data)         # 통계 요약
print("Statistics summary:")
print(stats, "\n")             # DescribeResult 출력

# 4. 희소 행렬 변환 (scipy.sparse)
from scipy.sparse import csr_matrix

# 0이 많은 2차원 배열을 희소 행렬로 변환 (Compressed Sparse Row)
data = [
    [0, 0, 3],
    [4, 0, 0],
    [0, 5, 0]
]
sparse_matrix = csr_matrix(data)  # 희소 행렬 생성
print("Sparse matrix representation:")
print(sparse_matrix)              # 희소 행렬 출력

# 희소 행렬의 Coords와 Values를 확인할 수 있음
# Coords  Values
# (0, 2)  3
# (1, 0)  4
# (2, 1)  5

#21
#seaborn 패키지
# python의 데이터 시각화 라이브러리
#통계적 그래프를 간단하고 아름답게 생성
#matplotlib 위에서 동작
#간결한 문법과 고급 시각화 기능 제공

import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

# 샘플 데이터셋 로드: 붓꽃(Iris) 데이터셋
iris = sns.load_dataset("iris")

# 1. Scatter Plot (산점도)
# 두 변수 간의 관계를 시각적으로 표현
sns.set_theme(style="whitegrid")  # 기본 스타일 설정
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
plt.title("Scatter Plot Example")
plt.show()

# 2. Linear Regression Plot (선형 회귀선)
# 데이터의 설명적 관계를 시각적으로 표현
sns.lmplot(data=iris, x="sepal_length", y="sepal_width", hue="species", height=6)
plt.title("Linear Regression Plot")
plt.show()

# 3. Histogram (히스토그램)
# 데이터의 분포를 확인하는 데 유용, kde=True로 커널밀도추정 곡선 추가
sns.histplot(data=iris, x="sepal_length", hue="species", kde=True)
plt.title("Histogram Example")
plt.show()

# 4. Box Plot (상자 그림)
# 데이터 분포와 이상치를 시각적으로 분석
sns.boxplot(data=iris, x="species", y="sepal_length")
plt.title("Box Plot Example")
plt.show()

# 5. Violin Plot (바이올린 플롯)
# 상자 그림과 커널밀도추정이 결합된 형태 , quart :25% 50% 75%
sns.violinplot(data=iris, x="species", y="sepal_length", inner="quart")
plt.title("Violin Plot Example")
plt.show()

# 6. Pair Plot (페어 플롯)
# 여러 변수 간의 관계를 한 번에 확인
sns.pairplot(iris, hue="species")
plt.show()

# 7. 스타일 커스터마이징
# - set_theme()로 스타일 변경 가능 (darkgrid, whitegrid, dark, white, ticks)
# - palette로 색상 테마 적용 가능 (deep, muted, bright, pastel, dark, colorblind)
sns.set_theme(style="darkgrid", palette="muted")
sns.histplot(data=iris, x="sepal_length", hue="species", kde=True)
plt.title("Customized Style Example")
plt.show()

# 8. 그래프 크기 조정
# sns.set_context()를 사용해 그래프 크기 조정
sns.set_context("notebook", rc={"figure.figsize": (10, 6)})
sns.boxplot(data=iris, x="species", y="sepal_length")
sns.set_palette("pastel") # 색상 테마 적용
plt.title("Adjusted Box Plot Size")
plt.show()

# 9. 복합 그래프 작성
# 여러 개의 서브플롯을 생성하여 비교 분석 가능 (FacetGrid 사용)
# g=sns.FacetGrid(data,row,col, height,aspect)
# g.map_dataframe(func,x,kde)
# g.set_titles(row_template,col_template) # 행제목, 열제목
g = sns.FacetGrid(iris, col="species", height=4, aspect=1)
g.map_dataframe(sns.histplot, x="sepal_length", kde=True)
g.set_titles(col_template="{col_name}")
plt.show()

# OpenCV 소개 및 기본 설정
# - OpenCV(Open Source Computer Vision)는 실시간 컴퓨터 비전을 위한 라이브러리
# - Python을 포함한 여러 프로그래밍 언어에서 사용 가능
# - 이미지 및 영상 처리 기능 제공

# 설치 및 라이브러리 임포트
# 설치: pip install opencv-python
import cv2  # OpenCV 모듈 임포트

# 1. 기본 이미지 로드 및 표시
image = cv2.imread('./ch21/opencv/sample.jpg')  # 이미지 로드
cv2.imshow('Loaded Image', image)  # 이미지 표시
cv2.waitKey(0)  # 키 입력 대기
cv2.destroyAllWindows()

# 2. 이미지 크기 조정
# cv2.resize()를 사용해 이미지를 300x300 크기로 변경
resized = cv2.resize(image, (300, 300))
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 색상/강도 변환 (그레이스케일로 변환)
# cv2.cvtColor()를 사용해 BGR 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. 이미지 회전 (이미지 중심 기준 45도 회전)
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. 엣지 검출 (Canny Edge Detection)
edges = cv2.Canny(image, 100, 200) # 낮은 임계값, 높은 임계값
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. 블러 처리 (Gaussian Blur)
blurred = cv2.GaussianBlur(image, (15, 15), 0) # 가우시안커널, x방향 시그마,y방향 시그마
cv2.imshow('Gaussian Blur', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. 객체 검출 (얼굴 검출)
# Haar Cascade 분류기를 사용해 얼굴을 검출
image=cv2.imread('./ch21/opencv/people.jpg')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# scalefactor: 검색 윈도우 확대 비율(1보다 커야 함) minneighbor 최소 중첩 횟수 , minsize 검출할 객체 최소 크기
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # 얼굴에 사각형 그리기 # 마지막 thickness

cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# OpenCV 실시간 비디오(웹캠) 영상 처리
# - cv2.VideoCapture(index)로 비디오 캡처 객체 생성
#   index: 0은 기본 웹캠, 1은 두 번째 카메라를 의미
# - read(): 비디오 프레임을 읽기 위한 함수 (프레임을 읽으면 (True, frame) 반환)
# - cv2.imshow(): 프레임을 화면에 표시
# - cv2.waitKey(): 키 입력 대기
# - video.release(): 사용된 메모리 반환
# - cv2.destroyAllWindows(): 모든 창 닫기

import cv2

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)  # 0: 기본 웹캠 사용

while True:
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:  # 프레임을 읽지 못하면 반복 종료
        break

    # Canny 엣지 검출 적용
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow('Edge Detection', edges)  # 결과 표시

    # 'q' 키가 입력되면 종료
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()  # 메모리 해제
cv2.destroyAllWindows()  # 모든 창 닫기

# 특정 색상 필터링
# - cv2.inRange(src, lowerb, upperb): 특정 범위의 색상 필터링
#   src: 입력 이미지
#   lowerb, upperb: 색상 범위 (하한값, 상한값)
# - cv2.bitwise_and(src1, src2, mask): 마스크를 적용하여 필터링된 결과 반환

import numpy as np

# 이미지 로드
image = cv2.imread('./ch21/opencv/candies.png')

# 녹색 범위 지정 (HSV 색 공간 사용)
green_lower = np.array([35, 100, 100])  # 하한값
green_upper = np.array([85, 255, 255])  # 상한값

# BGR 이미지를 HSV로 변환
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 녹색 색상 필터링
mask = cv2.inRange(hsv, green_lower, green_upper)
result = cv2.bitwise_and(image, image, mask=mask)

# 결과 표시
cv2.imshow('Green Color Filtering', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
