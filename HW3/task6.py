N = int(input())

numbers = list(map(int, input().split()))

max_index = 0
min_index = 0

for i in range(1, N):
    if numbers[i] > numbers[max_index]:
        max_index = i
    if numbers[i] < numbers[min_index]:
        min_index = i

numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

print(*numbers)