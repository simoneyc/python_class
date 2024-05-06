f = open("8/data.txt","r")
N, K = map(int, f.readline().split())
list1 = [[] for _ in range(N+1)]
list2 = [[_] for _ in range(N+1)]
list3 = [[] for _ in range(N+1)]
fake = 0
for i in range(7):
    D, x ,y = map(int, f.readline().split())
    if x>N or y>N:
        fake += 1
        continue
    elif D == 1:
        if x not in list1[y] and x not in list3[y] and y not in list1[x] and y not in list3[x]:
            list2[x] = list2[y] = list(set(list2[x]) | set(list2[y]))
        else:
            fake += 1
    elif D == 2:
        if x == y:
            fake += 1
        elif x not in list2[y] and x not in list3[y] and y not in list1[x] and y not in list2[x]:
            list2[x] = list1[y] = list(set(list2[x]) | set(list1[y]))
            list3[x] = list2[y] = list(set(list3[x]) | set(list2[y]))
            list1[x] = list3[y] = list(set(list1[x]) | set(list3[y]))
        else:
            fake += 1
print(fake)