import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def clean_screen_start(cla):
    print("clean_screen_start")



def skip_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("skip_check")

        skip_start(cla)
        way_start(cla)

    except Exception as e:
        print(e)

def skip_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("skip_start")

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 10:
                is_action = True

            is_skip = False

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("skip_1", imgs_)
                is_skip = True

            if is_skip == True:
                QTest.qWait(1000)
            else:
                is_action = True
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def way_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("way_start")

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 10:
                is_action = True

            is_way = False

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click\\up_right_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("up_right_1", imgs_)
                click_pos_reg(imgs_.x + 30, imgs_.y - 30, cla)
                is_action_count = 0
                is_way = True
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click\\down_left_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("down_left_1", imgs_)
                    click_pos_reg(imgs_.x - 30, imgs_.y + 30, cla)
                    is_action_count = 0
                    is_way = True

            if is_way == True:
                QTest.qWait(1000)
            else:
                is_action_count += 1
            QTest.qWait(1000)

    except Exception as e:
        print(e)