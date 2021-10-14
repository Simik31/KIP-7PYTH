def main():
    sum = 0
    for x in range(10):
        sum = sum + int(input("Input " + str((x + 1)) + ". number: "))
    print("Sum is: ", sum, sep="")
    print("Avg is: ", round(sum/10, 2), sep="")


if __name__ == "__main__":
    main()