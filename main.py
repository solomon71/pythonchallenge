# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
from src import ch_0, ch_1, ch_2, ch_3, ch_4, ch_5, ch_6, ch_7, ch_8


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('duder')

    print(os.getcwd())

    ch_0.main()
    ch_1.main()
    ch_2.main()
    ch_3.main()
    ch_4.main('66831')  # ch_4.ch_4('12345')
    ch_5.main()

    print("ch_6 --START---")
    ch_6.main('90052')
    ch_7.main()
    ch_8.main()

    print("")
    print("----------")
    print('Done')
