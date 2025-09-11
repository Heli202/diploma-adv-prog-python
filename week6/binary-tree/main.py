from tree import Tree


def main():
    tree = Tree()
    tree.insert(50, 3.5)
    tree.insert(35, 2.645)
    tree.insert(75, 1.7)
    tree.insert(12, 0.5)
    tree.insert(39, 9.9)

    # tree.traverse(1)
    tree.traverse(2)
    # tree.traverse(3)


if __name__ == '__main__':
    main()
# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
