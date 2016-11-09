"""Handing data preprocessing and IO pipeline.

Covers

+   Dictionary Preprocessing
+   Get a statistics for dictionary
+   Data formatting
+   General IO functions

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from __future__ import print_function
import os
import cPickle as pickle
from future.utils import iteritems

import en2pinyin as e2p


def load_dict(dict_path):
    """Load a dictionary.

    Currently only support Wubi typing method.

    Parameters
    ----------
    dict_path : str
        the absolute path to the dictionary

    Returns
    -------
    dict : Dictonary
        a mapping between one code to another
    """
    if not os.path.isfile(dict_path):
        raise ValueError("The target dictionary is not available at %s"
                         % (dict_path))

    return pickle.load(open(dict_path, "r"))


def save_dict(target_dict, filename, save_path=e2p.E2P_PACKAGE_DICT_PATH):
    """Save a Dictionary to some path.

    Parameters
    ---------
    target_dict : Dictionary
        A dictionary that is about to dump.
    filename : str
        the name of the dictionary.
    save_path : str
        the destination of the saving path.
    """
    file_path = os.path.join(save_path, filename)
    pickle.dump(target_dict, open(file_path, "wb"))
    print ("[MESSAGE] The target dictionary is saved at %s" % (file_path))


def load_ch_wubi_dict(dict_path=e2p.E2P_CH_WUBI_PATH):
    """Load Chinese to Wubi Dictionary.

    Parameters
    ---------
    dict_path : str
        the absolute path to chinese2wubi dictionary.
        In default, it's E2P_CH_WUBI_PATH.

    Returns
    -------
    dict : Dictionary
        a mapping between Chinese to Wubi Code
    """
    return load_dict(dict_path)


def load_wubi_ch_dict(dict_path=e2p.E2P_WUBI_CH_PATH):
    """Load Wubi to Chinese Dictionary.

    Parameters
    ---------
    dict_path : str
        the absolute path to chinese2wubi dictionary.
        In default, it's E2P_WUBI_CH_PATH.

    Returns
    -------
    dict : Dictionary
        a mapping between Wubi to Chinese Code
    """
    return load_dict(dict_path)


def reverse_dict(ori_dict):
    """Reverse dictionary mapping.

    Parameters
    ----------
    ori_dict : Dictionary
        original given dictionary

    Returns
    -------
    res_dict : Dictionary
        The result dictionary with the mapping of one-to-many
    """
    res_dict = {}
    for key in ori_dict:
        if ori_dict[key] not in res_dict:
            res_dict[ori_dict[key]] = [key]
        else:
            res_dict[ori_dict[key]].append(key)

    return res_dict


def reduce_dict(ori_dict):
    """Reduce one-to-many dictionary to one-to-one dictionary.

    The scenario here is the value is a list of Chinese characters, and
    the key is the wubi code. So the ideal processing is the Chinese
    character is mapping to some wubi code + order number.

    Parameters
    ---------
    ori_dict : Dictionary
        one-to-many dictionary.

    Returns
    -------
    res_dict : Dictionary
        result one-to-one dictionary.
    """
    res_dict = {}

    for key in ori_dict:
        if len(ori_dict[key]) > 1:
            for i in xrange(len(ori_dict[key])):
                res_dict[ori_dict[key][i]] = key+str(i)
        else:
            res_dict[ori_dict[key][0]] = key

    return res_dict


def build_chinese_wubi_dict(ch2wubi_dict):
    """Build a Chinese-Wubi one-to-one mapping.

    Parameters
    ----------
    ch2wubi_dict : Dictionary
        A Chinese to Wubi Dictionary

    Returns
    -------
    ch2wubi_res : Dictionary
        Chinese to Wubi code one-to-one mapping.
    wubi2ch_res : Dictionary
        Wubi to Chinese one-to-one mapping.
    """
    reverse_map = reverse_dict(ch2wubi_dict)
    ch2wubi_res = reduce_dict(reverse_map)
    wubi2ch_res = {v: k for k, v in iteritems(ch2wubi_res)}

    return ch2wubi_res, wubi2ch_res
