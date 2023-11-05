from Go import go

def main():
    while True:
        try:
            size = int(input("Enter the size of the Goban (9, 13, or 19): "))
            if size not in {9, 13, 19}:
                raise ValueError
            break
        except ValueError:
            print("Invalid size. Please choose a size 9, 13, or 19.")
    go(size, (), ())

if __name__ == "__main__":
    main()