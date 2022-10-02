'''
http://www.pythonchallenge.com/pc/def/linkedlist.html ->
http://www.pythonchallenge.com/pc/def/linkedlist.php
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

nothing=12345
and the next nothing is 44827

<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never
end. 400 times is more than enough. -->
'''

import re
import requests


def main(nothing):
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

    # check for .html in the response text
    stop_chex = re.search(".html", r.text)
    if stop_chex is not None:
        print("ch_4 ----------")
        print(r.text)
    else:
        print("ch_4 ----------")
        print(n)
        main(n)


if __name__ == '__main__':
    main('12345')
