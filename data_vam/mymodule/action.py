import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def menu_open(cla):
    print("menu_open")


def confirm_all(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("confirm_all")

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 5:
                is_action = True

            is_confirm = False

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\confirm_all\\confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("confirm_1", imgs_)
                is_confirm = True

            if is_confirm == True:
                QTest.qWait(1000)
            else:
                is_action = True
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def cancle_all(cla):
    print("cancle_all")
