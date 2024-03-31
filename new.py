import random

def generate_random_list(length):
    return [random.randint(1, 1000) for _ in range(length)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def print_list(arr):
    for num in arr:
        print(num)

def main():
    length = 20
    random_list = generate_random_list(length)

    print("Venkatesh Kumar")
    print_list(random_list)

    bubble_sort(random_list)

    print("\nSorted List:")
    print_list(random_list)

if __name__ == "__main__":
    main()
