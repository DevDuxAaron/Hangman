# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def read():
    numbers = []
    with open("./archives/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Alan", "Aarón", "Joel", "Sara"]
    with open("./archives/names.txt", "a", encoding="utf-8")as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    # read()
    write()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
