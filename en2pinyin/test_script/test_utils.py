"""Some testing script for utils module.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import en2pinyin.utils as utils

ch2wubi_dict = utils.load_ch_wubi_dict()

print len(ch2wubi_dict)
