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
        return is_dead
    except Exception as e:
        print(e)


def dead_recovery(cla):
    import numpy as np
    import cv2

    from check import maul_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from potion import maul_potion

    try:
        print("dead_recovery")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("post", imgs_)


            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\boohwal_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("boohwal_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(5):
                        result_maul = maul_check(cla)
                        if result_maul == True:
                            maul_potion(cla)
                            break
                        QTest.qWait(500)

            QTest.qWait(500)
    except Exception as e:
        print(e)
