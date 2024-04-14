import random

def generate_random_list(length):
    return [random.randint(1,100) for _ in range(10)]

def sum_of_lists(list1, list2, list3):
    for i in range(len(list1)):
        total = list1[i] + list2[i] + list3[i]
        print(f"Sum on index {i}: {total}")

def main():
    list1 = generate_random_list(10)
    list2 = generate_random_list(10)
    list3 = generate_random_list(10)

    print("List 1:",list1)
    print("List 2:",list2)
    print("List 3:",list3)

    print("\nsum of numbers standing on same index:")
    sum_of_lists(list1,list2,list3)

if __name__ == "__main__":
    main()
