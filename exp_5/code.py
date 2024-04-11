# no. of nodes
n = 5

request_queue = {0: [], 1: [], 2: [], 3: [], 4: []}
holder = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1}
token = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0}

adj_matrix = [[1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0]]

print("\nRaymond Tree Based Mutual Exclusion")
print("\nAdjacency Matrix for spanning tree:\n")

for i in adj_matrix:
    print(*i)  # printing values as individual elements and not as a list

# Process that wants to enter CS
req_process = int(input("\nEnter the process who wants to enter CS : "))


def find_parent(req_process):

    # Sending the request to the root that has the token
    request_queue[req_process].append(req_process)  # 3: [3]

    for i in range(n):
        if(adj_matrix[req_process][i] == 1):  # if req_process is pointing to the node i
            parent = i  # node number 1 is the parent
            # node no.1 appends node no.3(req_process) in its req_q
            request_queue[parent].append(req_process)
            break

    print("\nProcess {} sending request to Parent Process {}".format(
        req_process, parent))
    print("Request queue: ", request_queue)

    # checking if parent has the token or not
    if(token[parent] == 1):
        return parent
    else:
        parent = find_parent(parent)

    return parent


parent = find_parent(req_process)

while(token[req_process] != 1):  # while 3 does not have token

    child = request_queue[parent][0]  # 1 (child of 0)
    request_queue[parent].pop(0)  # removing 1 from req_q list of node no.0

    holder[parent] = child  # node 0 pointing to node 1
    holder[child] = 0  # node 1 not pointing to any node
    token[parent] = 0  # token is no longer with node 0
    token[child] = 1  # token is with node 1

    print("\nParent process {} has the token and sends the token to the request process {}".format(
        parent, child))
    print("Request Queue: ", request_queue)
    parent = child

if(token[parent] == 1 and request_queue[parent][0] == parent):
    request_queue[parent].pop(0)
    # holder variable for the node which has the token points to itself
    holder[parent] = parent
    print("\nProcess {} enter the Critical Section".format(parent))
    print("Request Queue: ", request_queue)

if(len(request_queue[parent]) == 0):
    print("\nRequest Queue of process {} is empty. Therefore Release Critical Section".format(parent))

print("\nHolder: ", holder)