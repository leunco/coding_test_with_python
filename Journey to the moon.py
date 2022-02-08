def find_set_index(a):
    for i in range(len(_list)):
        if a in _list[i]:
            return i

def journeyToMoon(n, astronaut):
    for a1, a2 in astronaut:
        i1, i2 = find_set_index(a1), find_set_index(a2)
        if i1 != i2:
            _list[i1] = _list[i1].union(_list[i2])
            del _list[i2]

    _sum2 = 0
    for i in range(len(_list)-1): # timeout
        _sum1 = 0
        for j in range(i+1,len(_list)):
            _sum1 += len(_list[j])
        _sum2 += len(_list[i]) * _sum1

    return _sum2

n, p = map(int, input().split())
astronaut = []
for _ in range(p):
    astronaut.append(list(map(int, input().split())))

_list = [{x} for x in range(n)]
print(journeyToMoon(n, astronaut))

