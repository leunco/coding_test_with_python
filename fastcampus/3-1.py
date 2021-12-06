### 백준 2920 : 음계
# c:1, d:2, e:3, f:4, g:5, a:6, b:7, C:8
# 1~8 : ascending / descending / mixed

## 내 풀이 (틀림)
_input = input("숫자를 입력하세요 : ")

if _input =='1 2 3 4 5 6 7 8':
    print('ascending')
elif _input == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')

#if _input[0]=='1' & _input[2]=='2' & _input[4]=='3' & _input[6]=='4' & _input[8]=='6' & _input[10]=='7' & _input[12]=='8':
#    print('ascending')
#elif _input[12]=='1' & _input[10]=='2' & _input[8]=='3' & _input[6]=='4' & _input[4]=='6' & _input[2]=='7' & _input[0]=='8':
#    print('descending')
#else:
#    print('mixed')


## 정답
a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1,8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')

### 백준 2798 : 블랙잭

## 내 풀이(중단)
N, M = tuple(map(int, input().split(' ')))
_card = list(map(int, input().split(' ')))

N * (N - 1) * (N - 2) / 6

if len(_card) != N:
    print('잘못 입력!')
else:
    _sum = 0
    for i in range(N):
        _sum = _card[i] + _card[i + 1] + _card

## 답
n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

count = 0
for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)
