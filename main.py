# This is a sample Python script.
import os


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # Writing cmd file
    dir_path = os.path.dirname(__file__)
    line_1 = "@echo off\n"
    line_2 = 'set PROJECT_HOME="' + dir_path + '"\n'
    with open('run.cmd', 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line_1 + line_2 + content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
