import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_2, click_pos_reg, text_check_get_num, change_number

    from massenger import line_to_me
    from character_select_and_game_start import character_change, game_ready
    from clean_screen import all_skip, clean_screen_start
    from potion import maul_potion
    from action import juljun_off, juljun_on, menu_open
    from get_item import get_post, get_event, get_special
    from check import attack_check

    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:

        print("test")

        get_special(cla)

        # kind_close = "c:\\my_games\\vam\\data_vam\\imgs\\clean_screen\\close"
        # kind_close_list = os.listdir(kind_close)
        #
        # for i in range(len(kind_close_list)):
        #     full_path = "c:\\my_games\\vam\\data_vam\\imgs\\clean_screen\\close\\" + str(kind_close_list[i])
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         print("close_list", kind_close_list[i], imgs_)

    except Exception as e:
        print(e)

