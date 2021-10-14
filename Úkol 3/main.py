def main():
    sum = 0
    x = 1
    print("Input numbers (end with 0):")
    while x > 0:
        num = int(input("Input " + str(x) + ". number: "))
        if num is 0:
            break
        sum = sum + num
        x = x + 1
    print("Sum is: ", sum, sep="")
    print("Avg is: ", round(sum/(x-1), 2), sep="")


if __name__ == "__main__":
    main()