# http://www.pythonchallenge.com/pc/def/oxygen.html
# smarty
# http://www.pythonchallenge.com/pc/def/oxygen.png

from PIL import Image
from PIL.ExifTags import TAGS

import config


def main():
    im = Image.open(config.ROOT_DIR + '/src/files/oxygen.png')
    exifdata = im.getexif()

    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")

    print(im.format, im.size, im.mode)
    print("ch_7 ----------")
    print("oxygen")


if __name__ == '__main__':
    main()
