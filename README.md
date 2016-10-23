# en2pinyin

Translate English to Pinyin.

## Short Introduction

So translating English to Chinese is hard. One reason is embedding over 80,000 Chinese characters. And this is proven to be hard. So, here is another approach I'm interested in, translating English to Pinyin and then convert Pinyin to Chinese characters.

Well, why would this thing work anyway? Well, first of all, one can compress any Chinese characters in romanization form without losing any meaning, second, then one can process this stuff as Enligh to any other Indo-European languages. In particular, one can model a significantly smaller network for modeling this big language.

This is not the whole story for sure, one need to answer the question of converting Pinyin to real Chinese Characters. There are generally two approach:

1. Train a network that do this, because one Pinyin may be corresponse to more than one characters, one may train such network to do this job, but I wouldn't find this method could work effectively.

2. Modify the Pinyin in pre-processing. Even Pyinyin to Chinese chars is a one-to-many relationship. However, this "many" is generally lower than 20 (my personal hunch). So one only need to model this id as one additional feature to Pinyin, in this way, one only need a lookup table to do this thing.

This is just some random thoughts.

In building the network, any character that is out of scope of ASCII is not considered.

## General Todo list

+ [x] Sample dataset with 20 news articles sampled.
+ [ ] Character-level ConvNets study.
+ [ ] Benchmark dataset translation (Chinese character to Pinyin)
+ [ ] First sample model trying.

## Requirements

+ `pinyin`

The program will search for the environment variable `EN2PINYIN_PATH`, a easy way to set it is to add following path to your bash profile:

```bash
export EN2PINYIN_PATH = $HOME/.en2pinyin
```

## Contacts

Yuhuang Hu  
Email: duguyue100@gmail.com
