# Custom length function
def len_(s):
    count = 0
    for _ in s:
        count += 1
    return count


# Count occurrences of a substring
def count_(s, sub):
    len_s = len_(s)
    len_sub = len_(sub)
    count = 0

    for i in range(len_s - len_sub + 1):
        if s[i: i + len_sub] == sub:
            count += 1
    return count


# Right split function
def rsplit_(s, sep=" ", maxsplit=-1):
    if sep == "":
        raise ValueError("Empty separator")

    result = []
    temp = ""
    s_len = len_(s)
    sep_len = len_(sep)
    split_count = 0
    i = s_len - 1

    while i >= 0:
        if maxsplit != -1 and split_count >= maxsplit:
            result.append(s[:i + 1])
            break

        if i - sep_len + 1 >= 0 and s[i - sep_len + 1: i + 1] == sep:
            result.append(temp[::-1])
            temp = ""
            i -= sep_len
            split_count += 1
        else:
            temp += s[i]
            i -= 1

    result.append(temp[::-1])
    return result[::-1]


# Find last occurrence of a substring (raises ValueError if not found)
def rindex_(s, sub, start=0, end=None):
    if end is None:
        end = len_(s)

    len_sub = len_(sub)

    for i in range(end - len_sub, start - 1, -1):
        if s[i: i + len_sub] == sub:
            return i

    raise ValueError("substring not found")


# Find last occurrence of a substring (returns -1 if not found)
def rfind_(s, sub, start=0, end=None):
    if end is None:
        end = len_(s)

    len_sub = len_(sub)

    for i in range(end - len_sub, start - 1, -1):
        if s[i: i + len_sub] == sub:
            return i
    return -1


# Menu-driven interface
def main():
    while True:
        print("\n===== STRING FUNCTION MENU =====")
        print("1. Count occurrences of a substring")
        print("2. Find last occurrence (rfind)")
        print("3. Split string from right (rsplit)")
        print("4. Find last occurrence (rindex)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            s = input("Enter the string: ")
            sub = input("Enter the substring: ")
            print("Count:", count_(s, sub))

        elif choice == '2':
            s = input("Enter the string: ")
            sub = input("Enter the substring: ")
            print("Last occurrence index (or -1 if not found):", rfind_(s, sub))

        elif choice == '3':
            s = input("Enter the string: ")
            sep = input("Enter the separator (default is space): ") or " "
            maxsplit = input("Enter max splits (-1 for all): ")
            maxsplit = int(maxsplit) if maxsplit.isdigit() or maxsplit == "-1" else -1
            print("Split result:", rsplit_(s, sep, maxsplit))

        elif choice == '4':
            s = input("Enter the string: ")
            sub = input("Enter the substring: ")
            try:
                print("Last occurrence index:", rindex_(s, sub))
            except ValueError as e:
                print(e)

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()