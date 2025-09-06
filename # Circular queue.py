# Circular queue
# https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1



def canCompleteCircuit(gas, cost):
    n = len(gas)
    total_gas = 0
    total_cost = 0
    start = 0
    tank = 0

    for i in range(n):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:
            start = i + 1
            tank = 0

    if total_gas < total_cost:
        return -1
    else:
        return start


if __name__ == "__main__":
    gas = [4, 5, 7, 4]
    cost = [6, 6, 3, 5]
    print("Starting Station Index:", canCompleteCircuit(gas, cost)) 

    gas = [3, 9]
    cost = [7, 6]
    print("Starting Station Index:", canCompleteCircuit(gas, cost))  
