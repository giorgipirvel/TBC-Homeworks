import random 

def random_numbers():
    return[random.randrange(10,1000000000) for i in range (100)]

def shortest_and_longest(numbers):
    shortest = min(numbers, key=lambda x: len(str(x)))
    longest = max(numbers, key=lambda x: len(str(x)))
    return shortest, longest

def sort_numbers(numbers):
    ascending = sorted(numbers, key=lambda x: len(str(x)))
    descending = sorted(numbers, key=lambda x: len(str(x)), reverse=True)
    return ascending, descending

def main():
    numbers = random_numbers()
    shortest, longest = shortest_and_longest(numbers)
    print(f"Shortest number: {shortest}, Longest number: {longest}")
    print()

    ascending, descending = sort_numbers(numbers)
    print("Ascending order:",ascending)
    print()
    print("Descending order:",descending)

if __name__ == "__main__":
    main()
