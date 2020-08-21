#!/usr/bin/python

import requests
from bs4 import BeautifulSoup


def lookup_gaming_tvs():
    page = requests.get('https://www.rtings.com/tv/reviews/best/by-usage/video-gaming')
    soup = BeautifulSoup(page.content, 'html.parser')

    tv_dict = {}

    tv_li = soup.find_all('li', class_='recommendations_block is-winner')
    # for tv in tv_li:
    #     tv_names = []
    #     tv_names.append(tv.h2.text)
    #     tv_names.append(tv.img['src'])
    #     tv_dict.update(tv_names)
    #     # tv_name = tv_name.replace('<h2 class="t-h3 e-page_section_title">', '')
    # print(tv_dict)
    return tv_li

    # tv_names = soup.find_all('h2', class_='t-h3 e-page_section_title')
    # for tv_name in tv_names:
    #     print(tv_name.text.strip())
    #
    # tv_types = soup.find_all('span', class_='test_result_value e-test_result review-value-score')
    # # print(tv_types)
    # for tv_type in tv_types:
    #     print(tv_type.text.strip())


def main():
    lookup_gaming_tvs()


main()
