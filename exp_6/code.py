n=int(input("Enter the number of processes : "))
r=int(input("Enter the number of resources : "))

alloc=[]
mx=[]
need=[]

print("Eneter allocated amount for each process :")
for i in range(n):
    list=(input()).split()
    alloc.append(list)
print("Eneter max amount for each process :")
for i in range(n):
    list=(input()).split()
    mx.append(list)
print("Eneter needed amount for each process :")
for i in range(n):
    list=(input()).split()
    need.append(list)

avail=(input("Enter the available resources : ")).split()

safe = []


def display(mx, alloc, need, avail):
    print('Available Resources : ', avail)
    print('Allocated Matrix :- ')
    print(alloc)
    print()
    print('Max Matrix :- ')
    print(mx)
    print()
    print('Need Matrix :- ')
    print(need)
    print()


def bankers(n, r, mx, alloc, need, avail):
    print('***** Initially *****')
    display(mx, alloc, need, avail)

    while True:
        mark = True

        for i in range(n):
            if i+1 in safe:
                continue

            mark = True
            for j in range(r):
                if need[i][j] > avail[j]:
                    mark = False
                    break

            if mark:
                safe.append(i+1)
                for j in range(r):
                    avail[j] += alloc[i][j] # once process done, increase jth resource availability
                    alloc[i][j] = 0
                    need[i][j] = '-' # ecause process is done

                print(f'***** After allocating resources to P{i+1} *****')
                print(f'P{i + 1} can be allocated resources for execution..')
                display(mx, alloc, need, avail)
                print()
                break

        if not mark:
            print("System is NOT in safe state !!")
            break
        if len(safe) == n:
            print("System is in safe state !!")
            print("Safe Sequence is : ", end=" ")
            for i in safe:
                print(f"P{i}", end=" ")
            print()
            break


bankers(n, r, mx, alloc, need, avail)