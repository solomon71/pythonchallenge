# http://www.pythonchallenge.com/pc/def/peak.html --> peak hell? --> pickle?

import pickle
import os

from config import ROOT_DIR


def main():
    # rb = read binary, downloaded from http://www.pythonchallenge.com/pc/def/banner.p
    data = pickle.load(open(ROOT_DIR + 'src/files/banner.p', 'rb'))

    print(os.getcwd())
    print("ch_5 ----------")
    for line in data:
        # print(line)
        print(''.join([k * v for k, v in line]))


if __name__ == '__main__':
    main()
