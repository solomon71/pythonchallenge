# http://www.pythonchallenge.com/pc/def/peak.html --> peak hell? --> pickle?

import pickle
import requests


def main():
    # rb = read binary, downloaded from http://www.pythonchallenge.com/pc/def/banner.p
    data = pickle.load(open('./files/banner.p', 'rb'))

    print("ch_5 ----------")
    for line in data:
        # print(line)
        print(''.join([k * v for k, v in line]))


if __name__ == '__main__':
    main()
