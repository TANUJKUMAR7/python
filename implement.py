import random

# Function to reverse a list
def reverse_list(arr):
    start = 0
    end = len(arr) - 1
{
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


# Function to shuffle a list using randint
def my_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0,i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# Main program
data = [1, 2, 3, 4, 5]

print("Original List:", data)

# Reverse
reversed_data = reverse_list(data.copy())
print("Reversed List:", reversed_data)

# Shuffle
shuffled_data = my_shuffle(data.copy())
print ("Shuffled List:", shuffled_data)

}