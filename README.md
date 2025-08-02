## list 함수들
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

---

## 📌 도전 문제 모음
### 250802
- [📂 100 도달하기 폴더](./250802/100%20도달하기)

- [📂 점수대 파악하기 폴더](./250802/점수대%20파악하기)

- [📂 코로나 메뉴얼2 폴더](./250802/코로나%20메뉴얼2)

- [📂 나눗셈의 나머지 폴더](./250802/나눗셈의%20나머지)

- [📂 배열 놀이 폴더](./250802/배열%20놀이)

- [📂 연속부분수열일까 폴더](.250802/연속부분수열일까)
