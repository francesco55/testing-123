def enlarge(i):
    return i * 100

if __name__ == "__main__":
    my_number = float(input("Please input a number."))
    n = enlarge(my_number)
    print("enlarging number:", n)