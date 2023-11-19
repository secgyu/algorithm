def hanoi_tower(n, start, temp, to):
    if n == 1:
        print(start,"에 있는 원판을 ",to,"로 옮기기")
    else:
        hanoi_tower(n-1, start, to, temp)
        hanoi_tower(1, start, temp, to)
        hanoi_tower(n-1, temp, start, to)


start = 1
temp = 2
to = 3
hanoi_tower(3, start, temp, to)