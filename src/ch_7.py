# http://www.pythonchallenge.com/pc/def/oxygen.html
# smarty
# http://www.pythonchallenge.com/pc/def/oxygen.png

from PIL import Image
import re

import config


def main():
    print('ch_7 --START---')
    img = Image.open(config.ROOT_DIR + '/src/files/oxygen.png')
    color_blocks = [img.getpixel((x, int(img.height / 2))) for x in range(img.width)]
    color_blocks = color_blocks[::7]  # get every 7th pixel
    ordinals = [b for (r, g, b, a) in color_blocks if r == g == b]  # only grab gray pixels
    message = ''.join(map(chr, ordinals))
    print(message)  # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

    new_message_list = re.findall("\d+", message)
    new_message = ''.join(map(chr, map(int, new_message_list)))

    print(new_message)  # integrity

    print("ch_7 ----------")
    print("integrity")


if __name__ == '__main__':
    main()
