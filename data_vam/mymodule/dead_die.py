import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def get_start(cla):

    try:
        print("get_start")

        # get_post(cla)
        # get_upjuk(cla)


    except Exception as e:
        print(e)

def dead_check(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
    from clean_screen import clean_screen_start

    try:
        print("dead_check")

        is_dead = False
        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn", imgs_)
            is_dead = True

        if is_dead == True:
            dead_recovery(cla)
    except Exception as e:
        print(e)


def dead_recovery(cla):
    import numpy as np
    import cv2

    from schedule import myQuest_play_add, myQuest_play_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from potion import maul_potion

    try:
        print("dead_recovery")
        maul_potion(cla)

        result_schedule = myQuest_play_check(cla, "check")
        result_schedule_ = result_schedule[0][2]

        if result_schedule_ == "튜토육성":
            myQuest_play_add(cla, result_schedule_)


    except Exception as e:
        print(e)
