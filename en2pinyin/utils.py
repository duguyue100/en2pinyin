"""Handing data preprocessing and IO pipeline.

Covers

+   Dictionary Preprocessing
+   Get a statistics for dictionary
+   Data formatting
+   General IO functions

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import os
import cPickle as pickle

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
