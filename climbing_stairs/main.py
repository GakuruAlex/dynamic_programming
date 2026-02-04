import ways
def main():
    while True:
        try:
            height: int = int(input("Enter the number of the stairs: "))
        except ValueError:
            print("Please enter a number.")
        else:
            break

    print(f"The number of ways up {height} is {ways.climbing_stairs(height)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

