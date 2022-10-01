'''
nothing=12345
and the next nothing is 44827

<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never
end. 400 times is more than enough. -->
'''

import re
import requests


def ch_4(nothing):
    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(nothing))
    n = re.findall('[0-9]+', r.text)

    if len(n):
        n = n.pop()
    else:
        print('************************')
        print('************************')
        print(r.text)
        print('************************')
        print('************************')
        n = str(int(int(nothing) / 2))

    print("ch_4 ----------")
    print(n)

    ch_4(n)


if __name__ == '__main__':
    ch_4('12345')
