n, m, k = map(int, input().split())
idMachine = list(map(int, input().split()))  # List of machine IDs in the current order

if n == 0:
    print(-1)
    exit()

for i in range(1, n + 1):  # Serve each of the n customers
    Time = 0  # Total time to serve customer i
    for j in range(1, m + 1):  # Serve m cakes to customer i
        curId = int(input())  # ID of the j-th cake the i-th customer wants to buy
        try:
            posMachine = idMachine.index(curId)  # Find the position of the machine with the given ID
        except ValueError:
            print(-1)
            exit()
        
        Time += posMachine + 1  # Time to serve += time to move cake j (position of the machine) + time to deliver cake j (1)
        
        # Move the machine to the front of the list
        idMachine.pop(posMachine)
        idMachine.insert(0, curId)

    print(Time, end=' ')

