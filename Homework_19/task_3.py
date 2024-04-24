def main():
    friends_dict = {}

    while True:
        input_str = input("Enter Names: ")

        if input_str == 'FINISH':
            print("Output:")
            for person, friends in sorted(friends_dict.items()):
                print(f"{person} – {', '.join(friends)}")
            break

        friend1, friend2 = input_str.split(' – ')

        friends_dict.setdefault(friend1, []).append(friend2)
        friends_dict.setdefault(friend2, []).append(friend1)

main()
