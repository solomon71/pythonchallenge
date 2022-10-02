# http://www.pythonchallenge.com/pc/def/channel.html
# zip
# now there are pairs
# ok, try this URL http://www.pythonchallenge.com/pc/def/channel.zip

import re
import zipfile

comments = []

def main(nothing):
    f = zipfile.ZipFile('./files/channel.zip')
    contents = f.read('{}.txt'.format(nothing)).decode("utf-8")
    comment = f.getinfo('{}.txt'.format(nothing)).comment.decode("utf-8")
    comments.append(comment)
    f.close()

    try:
        next_nothing = re.findall('[0-9]+', contents).pop()
        print(next_nothing)
        main(next_nothing)
    except IndexError:
        print(contents)
        print(comments)
        print(''.join(comments))

        # it's in the air. look at the letters.
        # OXYGEN

        print("ch_6 ----------")
        print("oxygen")


if __name__ == '__main__':
    main('90052')
