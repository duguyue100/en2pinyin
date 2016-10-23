"""Initialization file for en2pinyin package.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import os
from os.path import join

E2P_PATH = os.environ("EN2PINYIN_PATH")
E2P_DATA_PATH = join(E2P_PATH, "data")
E2P_EN_DATA_PATH = join(E2P_DATA_PATH, "en")  # English data
E2P_CN_DATA_PATH = join(E2P_DATA_PATH, "cn")  # Chinese character data
E2P_PY_DATA_PATH = join(E2P_DATA_PATH, "py")  # Pinyin data

# Create necessary folder structure

if not os.path.isdir(E2P_PATH):
    os.makedirs(E2P_PATH)

if not os.path.isdir(E2P_DATA_PATH):
    os.makedirs(E2P_DATA_PATH)

if not os.path.isdir(E2P_CN_DATA_PATH):
    os.makedirs(E2P_CN_DATA_PATH)

if not os.path.isdir(E2P_CN_DATA_PATH):
    os.makedirs(E2P_EN_DATA_PATH)

if not os.path.isdir(E2P_PY_DATA_PATH):
    os.makedirs(E2P_PY_DATA_PATH)
