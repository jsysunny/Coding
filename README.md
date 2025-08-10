https://www.notion.so/24a2f0b4683880ce9f31de0ee0e30c7e

# List, Dict  변경 가능 / Tuple, String 변경 불가능

# 📑 목차
0. [입출력,변수,함수](#함수)  
1. [List 함수들](#List-함수들)  
2. [String 함수들](#String-함수들)  
3. [Dictionary 함수들](#Dictionary-함수들)  
4. [Tuple 함수들](#Tuple-함수들)
5. [📌 도전 문제 모음](#-도전-문제-모음)

&nbsp;

# 입출력
## 입력
```python
1차원 입력 한개
input()
list(input()) / str(input()) / int(input()) / tuple(input())

각각
r,c = map(int, input().split())
r, c = tuple(map(int, input().split()))  
r, c = list(map(int, input().split())) -> r=temp[0] , c=temp[1]   
a, b = tuple(input().split()) : banana apple -> banana \n apple

1차원 입력 여러개
arr = input().split() : apple banana candy  -> ['apple', 'banana', 'candy']
numbers = list(map(int, input().split()))
string = list(map(str, input().split()))

2차원 입력 여러개
matrix = [list(map(int, input().split())) for _ in range(3)]
```

## 출력
```python
''.join(list)는 문자열 리스트를 하나의 문자열로 합치는 방법

chars = ['H', 'e', 'l', 'l', 'o']
result = ''.join(chars)
print(result)  # 출력: Hello

nums = [1, 2, 3]
result = ''.join(map(str, nums))  # ✅ ['1', '2', '3']로 바뀜
print(result)  # 출력: 123
```

&nbsp;
# 변수 
```python
a, b = map(int, input().split())

# Please write your code here.
def count(a,b):
    cnt=0
    #iscount=True 여기다 넣으면 한번 False가 되면 계속 False 이므로 i가 변할때마다 True로 바꾸어 줘야함 
    for i in range(a,b+1):
        iscount=True 
        if i%2==0:
            iscount= False
        elif i%10==5:
            iscount= False
        elif i%3==0 and i%9!=0:
            iscount= False
        
        if iscount:
            cnt+=1
    
    return cnt

print(count(a,b))
```
iscount를 어디다가 처음 선언할지를 잘 정해야함 

&nbsp;
# 함수
## return 사용
```python
a, o, c = input().split()
a = int(a)
c = int(c)

def plus(a, c):
    return f"{a} + {c} = {a + c}"

def calculate(a, o, c):
    if o == "+":
        return plus(a, c)

print(calculate(a, o, c))
```

&nbsp;

## print 사용
```python
def plus(a, c):
    print(f"{a} + {c} = {a + c}")

def calculate(a, o, c):
    if o == "+":
        plus(a, c)

calculate(a, o, c) #print(f"{a} + {c} = {a + c}") 이 값이 나옴
print(calculate(a, o, c)) # None : return 이 없으므로
```

&nbsp;
# List 함수들 -> pop만 인덱스 넣기
```python
# 반복문 for에서
# 요소를 가져올때 인덱스 값도 가져오고 싶다면
# enumerate()에 이터러블 객체를 전달하면
# 인덱스 i와 요소 e를 동시에 가져올 수 있다(set타입 형태로 변환)

my_list=["홍길동", "이", "김", "즙"]

for e in my_list:
    print(e)

for i,e in enumerate(my_list):
    print(f"i: {i}\t e:{e}")
```

```python
def modify(arr): # arr는 _list와 아예 동일
    arr[0] = 10


_list = [1, 2, 3, 4]
modify(_list)

for elem in _list:
    print(elem, end=" ")

>> 10 2 3 4
```

```python
def modify(arr): # arr는 _list와 관련이 없다.
    arr[0] = 10


_list = [1, 2, 3, 4]
modify(_list[:]) # 새로운 리스트를 만들어 넘기기

for elem in _list:
    print(elem, end=" ")

>> 1 2 3 4 # 값에 변화가 없다
```

### 1. `append()` : 리스트 마지막에 요소 추가
```python
list = [1, 2, 3, 4, 5]
list.append(6)
print(list)  # [1, 2, 3, 4, 5, 6]
```

&nbsp;

### 2. `insert()` : 원하는 위치에 요소 삽입
```python
list = [1, 2, 3, 4, 5]
list.insert(4, 6)
print(list)  # [1, 2, 3, 4, 6, 5]
```

&nbsp;

### 3. `sort()` : 리스트 정렬 (오름차순) 반대는 sort(reverse=True)
```python
list = [3, 4, 2, 1, 8]
list.sort()
print(list)  # [1, 2, 3, 4, 8]

list = ['d', 'f', 'a', 'e', 'c']
list.sort()
print(list)  # ['a', 'c', 'd', 'e', 'f']
```

&nbsp;

### 4. `reverse()` : 리스트 순서 뒤집기
```python
list = [3, 4, 2, 1, 8]
list.reverse()
print(list)  # [8, 1, 2, 4, 3]
```

&nbsp;

### 5. `index()` : 요소의 인덱스(위치) 반환
```python
list = [3, 4, 2, 1, 8]
print(list.index(2))  # 2
```

&nbsp;

### 6. `remove()` : 첫 번째로 등장하는 요소 삭제
```python
list = [3, 4, 2, 1, 8, 4, 4]
list.remove(4)
print(list)  # [3, 2, 1, 8, 4, 4]
```

```python
new = [-1, 7, 6, 3, -1, 8, 7, 4, 1, -3]

for n in new:
    if n > 0:
        new.remove(n)
```
       
1. 첫 번째 n = -1
음수니까 패스

2. 두 번째 n = 7
7은 양수 → 제거
→ new는 [-1, 6, 3, -1, 8, 7, 4, 1, -3]

❗ 문제 발생:

리스트에서 요소 하나가 사라지면, 그 다음 인덱스가 한 칸 앞으로 당겨짐

그런데 for 반복은 다음 인덱스로 넘어감 → 이때 6은 건너뜀!

&nbsp;

### 7. `pop()` : 인덱스 기반 요소 삭제 (기본은 마지막 요소)
```python
list = [3, 4, 2, 1, 8, 4, 4]
list.pop(5)
print(list)  # [3, 4, 2, 1, 8, 4]

list.pop()
print(list)  # [3, 4, 2, 1, 8]
```

&nbsp;

### 8. `count()` : 특정 요소 개수 세기
```python
list = [3, 4, 2, 1, 8, 4, 4]
print(list.count(4))  # 3
```

&nbsp;

### 9. `extend()` : 리스트 확장 (리스트 더하기)
```python
list_a = [10, 8, 2, 99]
list_b = [21, 22, 23]

list_a.extend(list_b)
print(list_a)  # [10, 8, 2, 99, 21, 22, 23]

list_b.extend([24, 25, 26])
print(list_b)  # [21, 22, 23, 24, 25, 26]
```

&nbsp;

### 10. `sum()` : 리스트 요소의 합 구하기
```python
list = [10, 8, 2, 99]
print(sum(list))  # 119
```


&nbsp;

### 11. `min()`, `max()` : 최소값, 최대값 구하기
```python
list = [10, 8, 2, 99]
print(min(list), max(list))  # 2 99
```


&nbsp;

### 12. `len()` : 리스트 길이(요소 개수) 구하기
```python
list = [10, 8, 2, 99]
print(len(list))  # 4
```

&nbsp;

[🔝 목차로 이동](#-목차)

&nbsp;

# String 함수들
string 은 immutable 이라 문자열을 바꾸려면 list 로 바꾸고 다시 string으로 바꿔야 한다. 
&nbsp;

## 🔠 문자열 대소문자 변환

| 함수 | 설명 | 예시 출력 |
|------|------|------------|
| `s.upper()` | 모든 문자를 대문자로 변환 | `'DAEUN PARK'` |
| `s.lower()` | 모든 문자를 소문자로 변환 | `'daeun park'` |
| `s.swapcase()` | 대문자는 소문자로, 소문자는 대문자로 | `'DAeUN PARk'` |
| `s.capitalize()` | 첫 글자만 대문자로 | `'Daeun park'` |
| `s.title()` | 각 단어의 첫 글자만 대문자로 | `'Daeun Park'` |

```python
s = 'daEun parK'
print(s.upper())      # DAEUN PARK
print(s.lower())      # daeun park
print(s.swapcase())   # DAeUN PARk
print(s.capitalize()) # Daeun park
print(s.title())      # Daeun Park
```

&nbsp;

## 🔢 문자열 개수, 위치 찾기

| 함수 | 설명 |
|------|------|
| `s.count(x)` | 문자열 `s`에서 `x`가 몇 번 나오는지 |
| `s.find(x)` | 문자열 `s`에서 `x`가 처음 나오는 위치 반환 (없으면 -1) |
| `s.index(x)` | `x`의 첫 위치 반환 (없으면 오류 발생) |

```python
s = 'My name is Daeun!'
print(s.count('a'))     # 2
print(s.count('is'))    # 1
print(s.find('~'))      # -1
print(s.index('a'))     # 4
# print(s.index('~'))   # ValueError: substring not found
```

&nbsp;

## 🔗 문자열 결합 및 삽입

| 함수 | 설명 |
|------|------|
| `s1.join(s2)` | `s2`의 문자 사이에 `s1`을 삽입 |
| `s1+s2` | 두 문자열 덧셈 |
| `s1*n` | 문자열 n번 곱셈(반복) [정수일경우에는 곱하기가됨] |
문자열은 뺄셈과 나눗셈 지원 안함

```python
a, b, c = "apple", "banana", "candy"
tot_str = ""

tot_str += a
tot_str += b
tot_str += c
print(tot_str)

>> applebananacandy
```

```python
a, b, c = "apple", "banana", "candy"
tot_str = ""

for target_str in [a, b, c]:
    tot_str += target_str
print(tot_str)

>> applebananacandy
```

```python
s1 = 'hello'
s2 = 'WORLD'
print(s1.join(s2))  # WhelloOhelloRhelloLhelloD
```

&nbsp;

## ✂️ 문자열 공백 및 문자 제거

| 함수 | 설명 |
|------|------|
| `s.strip([x])` | 양쪽에서 문자 또는 공백 제거 |
| `s.lstrip([x])` | 왼쪽에서 제거 |
| `s.rstrip([x])` | 오른쪽에서 제거 |
| `s.pop(i)` | i번째 문자 제거 |

```python
s = '  Hello World  '
print(s.strip())   # 'Hello World'
print(s.lstrip())  # 'Hello World  '
print(s.rstrip())  # '  Hello World'
```

&nbsp;

## 🔁 문자열 치환 및 분할

| 함수 | 설명 |
|------|------|
| `s.replace(x, y)` | x를 y로 치환 |
| `s.split([sep])` | 구분자 기준으로 문자열 분리 |

```python
s = 'My name is Daeun!'
print(s.replace('Daeun', 'Park'))  # My name is Park!
print(s.replace('a', 'A'))         # My nAme is DAeun!
print(s.split('is'))               # ['My name ', ' Daeun!']
print(s.split())                   # ['My', 'name', 'is', 'Daeun!']
```

&nbsp;

## ✅ 시작/끝 확인

| 함수 | 설명 |
|------|------|
| `s.startswith(x)` | 문자열이 `x`로 시작하는지 |
| `s.endswith(x)` | 문자열이 `x`로 끝나는지 |

```python
s = 'My name is Daeun!'
print(s.startswith('My'))    # True
print(s.endswith('n!'))      # True
print(s.endswith('Daeun'))   # False
```

&nbsp;

## 📐 문자열 정렬

| 함수 | 설명 |
|------|------|
| `s.center(i)` | i 너비 안에서 가운데 정렬 |
| `s.ljust(i)` | 왼쪽 정렬 |
| `s.rjust(i)` | 오른쪽 정렬 |

```python
s = 'My name is Daeun!'
print("'" + s.center(30) + "'")  # '       My name is Daeun!        '
print("'" + s.ljust(30) + "'")   # 'My name is Daeun!              '
print("'" + s.rjust(30) + "'")   # '              My name is Daeun!'
```

&nbsp;

## 🔤 문자열 구성 확인

| 함수 | 설명 |
|------|------|
| `s.isalpha()` | 알파벳/한글만 구성되었는지 |
| `s.isalnum()` | 알파벳/숫자/한글로 구성되었는지 |
| `s.isnumeric()` | 숫자만 구성되었는지 |

```python
s1 = "MynameisDaeun"
s2 = "Daeun0928"
s3 = "0928"

print(s1.isalpha())    # True
print(s2.isalpha())    # False
print(s3.isalpha())    # False

print(s1.isalnum())    # True
print(s2.isalnum())    # True
print(s3.isalnum())    # True

print(s1.isnumeric())  # False
print(s2.isnumeric())  # False
print(s3.isnumeric())  # True
```

&nbsp;

[🔝 목차로 이동](#-목차)

&nbsp;

# Dictionary 함수들

## 딕셔너리 생성
d = {'key1': 1}

&nbsp;

## 값 추가
```python
d['key2'] = 2
d['key3'] = 'value3'
d[4] = 4
d[(5, 6)] = 'value 5 and 6'  # 튜플 키
d['key7'] = (7, 8)           # 튜플 값
```

&nbsp;

## 출력 관련
```python
print(d)
# {'key1': 1, 'key2': 2, 'key3': 'value3', 4: 4, (5, 6): 'value 5 and 6', 'key7': (7, 8)}

print(d.keys())
# dict_keys(['key1', 'key2', 'key3', 4, (5, 6), 'key7'])

print(d.values())
# dict_values([1, 2, 'value3', 4, 'value 5 and 6', (7, 8)])

print(d.items())
# dict_items([('key1', 1), ('key2', 2), ('key3', 'value3'), (4, 4), ((5, 6), 'value 5 and 6'), ('key7', (7, 8))])

print(d['key3'])
# value3
```

&nbsp;

## 값 수정
```python
d['key3'] = 3
print(d['key3'])
# 3
```

&nbsp;

## 존재 여부 확인
```python
if 'key1' in d:
    print("'key1'이 존재합니다.")
else:
    print("'key1'이 존재하지 않습니다.")
# 'key1'이 존재합니다.

if 1 in d.values():
    print("1이 존재합니다.")
else:
    print("1이 존재하지 않습니다.")
# 1이 존재합니다.
```

&nbsp;

## get()으로 값 얻기
```python
print(d.get('key1'))     # 1
print(d.get('key1000'))  # None
```

&nbsp;

## 키-값 삭제
```python
del d['key1']
print(d)
# {'key2': 2, 'key3': 3, 4: 4, (5, 6): 'value 5 and 6', 'key7': (7, 8)}
```

&nbsp;

## 전체 삭제
```python
d.clear()
print(d)
# {}
```

&nbsp;

[🔝 목차로 이동](#-목차)

&nbsp;

# 📌 도전 문제 모음
### 250802
- [📂 100 도달하기 폴더](./250802/100%20도달하기)

- [📂 점수대 파악하기 폴더](./250802/점수대%20파악하기)

- [📂 코로나 메뉴얼2 폴더](./250802/코로나%20메뉴얼2)

- [📂 나눗셈의 나머지 폴더](./250802/나눗셈의%20나머지)

- [📂 배열 놀이 폴더](./250802/배열%20놀이)

- [📂 연속부분수열일까 폴더](./250802/연속부분수열일까)

- [📂 999 또는 -999](./250802/999%20또는%20-999)

- [📂 중복되지 않는 정수 중 최대](./250802/중복되지%20않는%20정수%20중%20최대)

- [📂 가장 왼쪽에 있는 최댓값](./250802/가장%20왼쪽에%20있는%20최댓값)

&nbsp;

[🔝 목차로 이동](#-목차)
