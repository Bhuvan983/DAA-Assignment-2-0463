import random
import matplotlib.pyplot as plt
import time

random.seed('ABC')
amount=int(input("Enter number of elements in array: "))
numbers = [random.randint(0, 100) for _ in range(amount)]

def bubble_sort(number_lst):
    n = len(number_lst)

    for i in range(n):
        for j in range(0, n-i-1):
            if number_lst[j] > number_lst[j+1]:
                number_lst[j], number_lst[j+1] = number_lst[j+1], number_lst[j]
                plot_bars(number_lst)

def selection_sort(number_lst):
    n = len(number_lst)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if number_lst[j] < number_lst[min_index]:
                min_index = j

        number_lst[i], number_lst[min_index] = number_lst[min_index], number_lst[i]
        plot_bars(number_lst)

def insertion_sort(number_lst):
    n = len(number_lst)

    for i in range(1, n):
        key = number_lst[i]
        j = i - 1
        while j >= 0 and key < number_lst[j]:
            number_lst[j + 1] = number_lst[j]
            j -= 1
        number_lst[j + 1] = key
        plot_bars(number_lst)

def quick_sort(number_lst, low, high):
    if low < high:
        pi = partition(number_lst, low, high)
        quick_sort(number_lst, low, pi)
        plot_bars(number_lst)
        quick_sort(number_lst, pi + 1, high)
        plot_bars(number_lst)

def partition(number_lst, low, high):
    pivot = number_lst[low]
    left = low
    right = high

    while True:
        while number_lst[left] < pivot:
            left += 1
        while number_lst[right] > pivot:
            right -= 1
        if left >= right:
            return right
        number_lst[left], number_lst[right] = number_lst[right], number_lst[left]
        left += 1
        right -= 1

def merge_sort(number_lst, left, right):

    if left >= right:
        return

    mid = (left + right) // 2

    plt.bar(list(range(amount)), number_lst)
    plt.pause(0.001)
    plt.clf()

    merge_sort(number_lst, left, mid)
    merge_sort(number_lst, mid + 1, right)

    merge(number_lst, left, right, mid)

    plt.bar(list(range(amount)), number_lst)
    plt.pause(0.5)
    plt.clf()

def merge(number_lst, left, right, mid):
    left_cpy = number_lst[left:mid + 1]
    right_cpy = number_lst[mid + 1:right + 1]

    l_counter, r_counter = 0, 0
    sorted_counter = left

    while l_counter < len(left_cpy) and r_counter < len(right_cpy):

        if left_cpy[l_counter] <= right_cpy[r_counter]:
            number_lst[sorted_counter] = left_cpy[l_counter]
            l_counter += 1

        else:
            number_lst[sorted_counter] = right_cpy[r_counter]
            r_counter += 1

        sorted_counter += 1

    while l_counter < len(left_cpy):

        number_lst[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
        sorted_counter += 1

    while r_counter < len(right_cpy):
        number_lst[sorted_counter] = right_cpy[r_counter]
        r_counter += 1
        sorted_counter += 1

def plot_bars(number_lst):
    plt.bar(list(range(amount)), number_lst)
    plt.pause(0.2)  # Adjust the pause time as needed
    plt.clf()

def main():
    
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")
    print("5. Merge Sort")


    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        bubble_sort(numbers)
    elif choice == '2':
        selection_sort(numbers)
    elif choice == '3':
        insertion_sort(numbers)
    elif choice == '4':
        quick_sort(numbers, 0, len(numbers) - 1)
    elif choice == '5':
        merge_sort(numbers,0,len(numbers)-1)

    else:
        print("Invalid choice")

    print("Sorted list:", numbers)

if __name__ == "__main__":
    main()

# Plot the final sorted list
plt.bar(list(range(amount)), numbers)
plt.show()
