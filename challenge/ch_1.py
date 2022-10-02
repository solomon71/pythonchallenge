import string

# http://www.pythonchallenge.com/pc/def/map.html

# k -> M  :: K L M
# O -> Q  :: O P Q
# E -> G  :: E F G
def main():
    # key = "abcdefghijklmnopqrstuvwxyz"
    # key_shift = "cdefghijklmnopqrstuvwxyzab"
    # trans = str.maketrans(key, key_shift)

    trans = str.maketrans(string.ascii_lowercase[:], string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr " \
           "ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    translation = str.translate(code, trans)
    print("ch_1 ----------")
    print(translation)
    print("translating map")
    print(str.translate("map", trans))


if __name__ == '__main__':
    main()
