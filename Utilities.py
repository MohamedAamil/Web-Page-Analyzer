"""
Utilities.py : Functions to parse html, get word,lines,unique words and top words counting
"""
import requests
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

#https://www.edutopia.org/article/help-students-build-intrinsic-motivation

"""
Web Utilities
"""


def get_html_content(url):
    """
    Gets the html data of the Url
    :param url: string , input url
    :return: html data
    """

    html = requests.get(url)
    return html.content


def parse_html(html , tag):
    """
    Parse the html using the required tag
    :param html: string, html data
    :param tag: string, html tag
    :return: list, all data with given tag
    """


    soup = BeautifulSoup(html, 'html.parser')
    data = [para.text for para in soup.find_all(tag)]

    return data


"""
Utilities for collecting required data
"""


top_words_count = 5

def get_statistics(data):
    """
    Get the lines count,words count, unique words count and top words
    :param data: list, all paras in the Url
    :return: dict, (lines,words,unique words,top words)
    """

    lines = get_lines(data)
    words = get_words(lines)
    wordlength = len(words)
    unique_words = list(set(words))
    top_n_words = get_top_words(top_words_count,words )
    statistics = {'line_count': len(lines), 'word_count': wordlength ,'unique_words': len(unique_words),
                  'top_words': top_n_words}
    return statistics



def get_lines(value):
    """
    Gets the lines in the Url
    :param value: list, parsed html using tag
    :return: list, All Lines in the Url
    """

    lines = []
    for para in value:
        para_lines = re.split('[.]+',para)
        lines.extend(para_lines)
    cleaned_lines = clean_string(lines)
    return cleaned_lines


def clean_string(lines):
    """
    Removes Punctuations, empty spaces, and lowers the case
    :param lines: list, All lines from the Url
    :return: list, cleaned lines
    """

    st = str.maketrans("", "", string.punctuation)
    cleaned_lines = [line.translate(st).lower().strip() for line in lines if line]
    return cleaned_lines


def get_words(lines):
    """
    Gets all the words in the given lines
    :param lines: list, lines of the Url
    :return: list, words
    """

    words = []
    for line in lines:
        words.extend(line.split())
    return words


def get_top_words(n,words):
    """
    Get the top words from Url after removing stop words
    :param n: int, count for top words to display
    :param words: list, words
    :return: list, top words
    """

    fp = open("stopwords.txt", "r")
    stop_words = fp.read().split("\n")
    fp.close()

    for stop_word in stop_words:
        for word in words:
            if word == stop_word:
                words.remove(word)

    top_n_words = Counter(words).most_common(n)
    top_words = []

    for x, y in top_n_words:
        top_words.append(x)

    return top_words