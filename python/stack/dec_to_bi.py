from stack import Stack

def dec_to_bi(decNumber):
    bin = Stack()

    while decNumber > 0:
        bin.push((decNumber % 2))
        decNumber = decNumber // 2

    binString = ""

    while not bin.isEmpty():
        binString = binString + str(bin.pop())

    return binString

print(dec_to_bi(7))