def time(s):
    ans = s.split(":")
    return int(ans[0]) * 60 + int(ans[1]) + int(ans[2])/60

n = input("Enter the agreed clock time: ")

init_val = time(n)

nodes = int(input("Enter the number of nodes: "))

dict_nodes = {}
ls = []

for i in range(nodes):
    print(f"Enter the clock time for {i + 1} node : ")
    x = input()
    ls.append(time(x))
    dict_nodes[chr(97 + i)] = []

print()
for key in dict_nodes.keys():
    print(f"{key} : {dict_nodes[key]}")

print()
print(ls)

for i in range(nodes):
    val = -float('inf')
    for i in range(nodes):
        diff = ls[i] - init_val
        dict_nodes[chr(97 + i)].append(diff)
        if diff < 0:
            val = max(val, diff)
    for i in range(nodes):
        if val != -float('inf'):
            ls[i] += abs(val)
    print()
    print(*ls)

print()
for key in dict_nodes.keys():
    print(f"{key} : {dict_nodes[key]}")

for i in range(nodes):
    avg = sum(dict_nodes[chr(97 + i)]) / nodes
    if avg >= 0:
        ls[i] -= abs(avg)
    else:
        ls[i] += abs(avg)

print()
print(ls)

def get_time(val):
    hours = int(val // 60)
    mins = int(val - hours * 60)
    seconds = int((val - int(val)) * 60)
    return str(hours) + ":" +  str(mins) + ":" + str(seconds)

for i in range(nodes):
    print(f'Time for Node {chr(97 + i)} : ', get_time(ls[i]))