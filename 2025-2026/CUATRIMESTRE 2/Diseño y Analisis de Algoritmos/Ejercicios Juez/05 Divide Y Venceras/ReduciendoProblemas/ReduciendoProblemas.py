N = int(input())
objects = list(map(int, input().split()))
M = int(input())

prefix = [0] * (N + 1)

for i in range(N):
    prefix[i + 1] = prefix[i] + objects[i]
print(prefix)
def getSum(start, size):
    return prefix[start + size] - prefix[start]

def binarySearchFirstGreater(value, size):
    low = 0
    high = N - size
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        currentSum = getSum(mid, size)

        if currentSum > value:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer

for _ in range(M):
    value, size = map(int, input().split())
    position = binarySearchFirstGreater(value, size)
    print(position, getSum(position, size))