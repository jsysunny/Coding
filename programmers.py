#Lv1
'''
git add programmers.py  # 또는 수정한 파일 이름
git commit -m "문제 코드 수정"
git push
list : .sort() , .remove()
string은 수정 불가 
string: .lower , sorted(n)
둘다 : .count 

'''


'''
1
문제 설명

자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
제한사항

    N의 범위 : 100,000,000 이하의 자연수

입출력 예
N 	answer
123 	6
987 	24
입출력 예 설명

입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.
'''
def solution(n):
    answer = 0
    n=str(n)
    for s in n:
        answer+=int(s)

    return answer

'''

2.
문제 설명

자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
제한 조건

    n은 10,000,000,000이하인 자연수입니다.

입출력 예
n 	return
12345 	[5,4,3,2,1]
'''
def solution(n):
    return [int(i) for i in str(n)[::-1]]

'''
3.
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
제한 조건

    x는 -10000000 이상, 10000000 이하인 정수입니다.
    n은 1000 이하인 자연수입니다.

입출력 예
x 	n 	answer
2 	5 	[2,4,6,8,10]
4 	3 	[4,8,12]
-4 	2 	[-4, -8]

'''
def solution(x, n):
    return [x*i for i in range(1,n+1)]

'''
4.
문제 설명

자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.
제한사항

    3 ≤ n ≤ 1,000,000

입출력 예
n 	result
10 	3
12 	11
입출력 예 설명

입출력 예 #1

    10을 3으로 나눈 나머지가 1이고, 3보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 3을 return 해야 합니다.

입출력 예 #2

    12를 11로 나눈 나머지가 1이고, 11보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 11을 return 해야 합니다.

생각
n을 어떤 수 x(변수)로 나눈게 1이 되어야 하니까 일단 1부터 n까지 x를 증가시켜서 1이 되면 가장 작을때니까 break해서 나오기
'''
def solution(n):
    answer = 0
    for i in range(1,n):
        if n%i==1:
            answer=i
            break
    return answer

'''
5.
문제 설명

문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
제한 조건

    s의 길이는 1 이상 5이하입니다.
    s의 맨앞에는 부호(+, -)가 올 수 있습니다.
    s는 부호와 숫자로만 이루어져있습니다.
    s는 "0"으로 시작하지 않습니다.

입출력 예

예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

생각
양수는 부호가 있을 수도 없을수도 있으니까 음수를 먼저 조건으로 거르는게 편함
부호는 항상 앞에 오고 s가 string이니까 list처럼 해석 가능

'''
def solution(s):
    answer = 0
    if s[0]=="-":
        answer=int(s[1:])
        return -answer
    else:
        answer=int(s)
        return answer

'''
6.

문제 설명

정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
제한 사항

    n은 0 이상 3000이하인 정수입니다.

입출력 예
n 	return
12 	28
5 	6
입출력 예 설명

입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.

'''  
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer+=i
    return answer


'''
7.
문제 설명

두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
제한 조건

    a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
    a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
    a와 b의 대소관계는 정해져있지 않습니다.

입출력 예
a 	b 	return
3 	5 	12
3 	3 	3
5 	3 	12

생각
a,b 둘 사이를 더한다고 하면 뭐가 큰지 모르니까 min max 으로 하면 됨 
'''

def solution(a, b):
    answer = 0
    for i in range(min(a,b),max(a,b)+1):
        answer+=i
    return answer

'''
8.

문제 설명

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
제한사항

    문자열 s의 길이 : 50 이하의 자연수
    문자열 s는 알파벳으로만 이루어져 있습니다.

입출력 예
s 	answer
"pPoooyY" 	true
"Pyy" 	false
입출력 예 설명

입출력 예 #1
'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

입출력 예 #2
'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.

※ 공지 - 2021년 8월 23일 테스트케이스가 추가되었습니다.

'''

def solution(s):
    s = s.lower()  
    return s.count('p') == s.count('y')

'''

9. 문제 설명

임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
제한 사항

    n은 1이상, 50000000000000 이하인 양의 정수입니다.

입출력 예
n 	return
121 	144
3 	-1
입출력 예 설명

입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.


'''
def solution(n):
    for i in range(1,n+1):
        if i*i==n:
            return (i+1)**2
    return -1

'''
10.
문제 설명

양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
제한 조건

    x는 1 이상, 10000 이하인 정수입니다.

입출력 예
x 	return
10 	true
12 	true
11 	false
13 	false
입출력 예 설명

입출력 예 #1
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

입출력 예 #2
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

입출력 예 #3
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

입출력 예 #4
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.

'''
def solution(x):
    answer = True
    sum=0
    for a in str(x):
        sum+=int(a)
    if x%sum!=0:
        answer=False
    return answer

'''
11.

문제 설명

어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
제한사항

    absolutes의 길이는 1 이상 1,000 이하입니다.
        absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
    signs의 길이는 absolutes의 길이와 같습니다.
        signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

입출력 예
absolutes 	signs 	result
[4,7,12] 	[true,false,true] 	9
[1,2,3] 	[false,false,true] 	0
입출력 예 설명

입출력 예 #1

    signs가 [true,false,true] 이므로, 실제 수들의 값은 각각 4, -7, 12입니다.
    따라서 세 수의 합인 9를 return 해야 합니다.

입출력 예 #2

    signs가 [false,false,true] 이므로, 실제 수들의 값은 각각 -1, -2, 3입니다.
    따라서 세 수의 합인 0을 return 해야 합니다.


생각
1. 문제에서 뭘 묻는지 이해
absolutes: 절댓값만 있는 숫자들

signs: 이 숫자들이 양수인지 음수인지 알려주는 표식

📌 목표:
→ "진짜 정수들의 합을 구하라"
→ 절댓값에 부호를 붙여서 더하라는 말

2. 머릿속 질문으로 바꿔보기
"각 숫자의 부호를 어떻게 정하지?"

signs[i] == True → +absolutes[i]

signs[i] == False → -absolutes[i]

🧠 그래서 이렇게 생각할 수 있어:

"각 숫자를 하나씩 보면서, signs에 따라 + 또는 -로 바꿔서 더하면 되겠다!"

'''
def solution(absolutes, signs):
    answer =0
    for i in range(0,len(absolutes)):
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer

'''
12.
문제 설명

0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
제한사항

    1 ≤ numbers의 길이 ≤ 9
        0 ≤ numbers의 모든 원소 ≤ 9
        numbers의 모든 원소는 서로 다릅니다.

입출력 예
numbers 	result
[1,2,3,4,6,7,8,0] 	14
[5,8,4,0,6,7,9] 	6
입출력 예 설명

입출력 예 #1

    5, 9가 numbers에 없으므로, 5 + 9 = 14를 return 해야 합니다.

입출력 예 #2

    1, 2, 3이 numbers에 없으므로, 1 + 2 + 3 = 6을 return 해야 합니다.

'''
def solution(numbers):
    answer = 0
    for i in range(0,10):
        if i not in numbers:
            answer+=i
    return answer

'''
13.
문제 설명

함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.
제한 조건

    n은 1이상 8000000000 이하인 자연수입니다.

입출력 예
n 	return
118372 	873211

여기서 sorted는 string에서 sort해서 list로 반환됨 고로 s=int(s) 이러면 안됨 / s="".join(s) 이렇게 써야 함 
'''
def solution(n):
    s = str(n)
    s = sorted(s, reverse=True)
    s = "".join(s)
    return int(s)


'''
14.

문제 설명

array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
제한사항

    arr은 자연수를 담은 배열입니다.
    정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
    divisor는 자연수입니다.
    array는 길이 1 이상인 배열입니다.

입출력 예
arr 	divisor 	return
[5, 9, 7, 10] 	5 	[5, 10]
[2, 36, 1, 3] 	1 	[1, 2, 3, 36]
[3,2,6] 	10 	[-1]
입출력 예 설명

입출력 예#1
arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.

입출력 예#2
arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.

입출력 예#3
3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.

'''
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor==0:
            answer.append(a)
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer

'''
15.
문제 설명

String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
제한 사항

    seoul은 길이 1 이상, 1000 이하인 배열입니다.
    seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
    "Kim"은 반드시 seoul 안에 포함되어 있습니다.

입출력 예
seoul 	return
["Jane", "Kim"] 	"김서방은 1에 있다"


'''
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            return f"김서방은 {i}에 있다"
        

'''
16.

문제 설명

1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요. 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.
제한 사항

    입력된 수, num은 1 이상 8,000,000 미만인 정수입니다.

입출력 예
n 	result
6 	8
16 	4
626331 	-1
입출력 예 설명

입출력 예 #1
문제의 설명과 같습니다.

입출력 예 #2
16 → 8 → 4 → 2 → 1 이 되어 총 4번 만에 1이 됩니다.

입출력 예 #3
626331은 500번을 시도해도 1이 되지 못하므로 -1을 리턴해야 합니다.

※ 공지 - 2022년 6월 10일 다음과 같이 지문이 일부 수정되었습니다.

    주어진 수가 1인 경우에 대한 조건 추가

'''
def solution(num):
    answer = 0
    while num>1:
        if num%2==0:
            num=num/2
            answer+=1
        else:
            num=num*3+1
            answer+=1
    if answer>=500:
        answer=-1
    return answer

'''
17.
문제 설명

프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
제한 조건

    phone_number는 길이 4 이상, 20이하인 문자열입니다.

입출력 예
phone_number 	return
"01033334444" 	"*******4444"
"027778888" 	"*****8888"

str은 수정 불가능한 자료형이어서 phone_number[:-4] = "*" 이게 안됨
'''
def solution(phone_number):
    stars = "*" * (len(phone_number) - 4)
    return stars + phone_number[-4:]

'''
18.
문제 설명

단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
재한사항

    s는 길이가 1 이상, 100이하인 스트링입니다.

입출력 예
s 	return
"abcde" 	"c"
"qwer" 	"we"

'''
def solution(s):
    answer = ''
    if len(s)%2==0:
        answer=s[len(s)//2-1]+s[len(s)//2]
    else:
        answer=s[(len(s)-1)//2]
    return answer

'''
19.
문제 설명

정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
제한 조건

    arr은 길이 1 이상인 배열입니다.
    인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

입출력 예
arr 	return
[4,3,2,1] 	[4,3,2]
[10] 	[-1]

'''
def solution(arr):
    arr.remove(min(arr))
    if not arr:
        arr=[-1]
    return arr
