
# Quera Webpage https://quera.org/problemset/171795/
# Ali Nakhaee 
# https://github.com/Haj4li

test = int(input())
times = []
for t in range(test):
    inp = input().split(' ')
    rooms = int(inp[0])
    searcht = int(inp[1])
    changet = int(inp[2])
    times.append((rooms * searcht)+((rooms-1) * changet))

for t in times:
    print(t)