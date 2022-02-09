## 곱하기 혹은 더하기
# 내 코드

str = input()
str = list(str)
opr = []

for i in range(len(str)-1):
    if (str[i] == '0' or str[i+1] == '0'):
        opr.append('+')
    else:
        opr.append('*')

n1 = int(str[0])
n2 = int(str[1])

if opr[0] == '*':
    _sum = n1 * n2
else:
    _sum = n1 + n2

for i in range(2,len(str)):
    n1 = int(str[i])

    if opr[i-1] == '*':
        _sum = _sum * n1
    else:
        _sum = _sum + n1

print(_sum)

# 풀이
data = input()

result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)