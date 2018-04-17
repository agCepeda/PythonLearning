def main():
    print("------------------------------------------------")
    print("================= BUBBLE SORT ==================")
    print("------------------------------------------------")

    length = int(input("Enter the length of the array:"))

    data = []

    for i in range(length):
        data.append(int(input("Data[" + str(i) + "] = ")))

    print("------------------------------------------------")
    print("Sorted Array:")

    bubbleSort(data)

    for i in range(length):
        print("Data[" + str(i) + "] = " + str(data[i]))


def bubbleSort(data):
    for i in range(1, len(data)):
        for j in range(len(data) - i):
            if data[j] > data[j + 1]:
                aux = data[j]
                data[j] = data[j + 1]
                data[j + 1] = aux

if __name__ == "__main__":
    main()