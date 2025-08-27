import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

kind_confirm = "c:\\my_games\\vam\\data_vam\\imgs\\action\\confirm_all"
kind_confirm_list = os.listdir(kind_confirm)

def menu_open(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start
    from check import out_check, maul_check, move_check, move_ing
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import go_maul

    try:
        print("menu_open")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("menu : post", imgs_)

                is_open = True

            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(930, 45, cla)
                else:
                    clean_screen_start(cla)



            QTest.qWait(200)
    except Exception as e:
        print(e)



def confirm_all(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("confirm_all")

        is_action = False
        is_action_count = 0

        is_confirm = True

        while is_action is False:
            is_action_count += 1
            if is_action_count > 3:
                is_action = True

            is_confirm = False

            for i in range(len(kind_confirm_list)):

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\confirm_all\\" + str(kind_confirm_list[i])
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1", imgs_)
                    is_confirm = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            if is_confirm == True:
                QTest.qWait(1000)
            else:
                is_action = True
            QTest.qWait(100)
        return is_confirm
    except Exception as e:
        print(e)


def cancle_all(cla):
    print("cancle_all")



def go_maul(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start
    from check import out_check, loading_check, loading_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_


    try:
        print("go_maul")

        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count +=1
            if is_data_count > 7:
                is_data = True

            result_out = out_check(cla)
            if result_out == True:

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\go_maul\\jabhwa.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 300, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jabhwa", imgs_)
                    is_data = True
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\go_maul\\jangbi.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 30, 960, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jangbi", imgs_)
                        is_data = True
                    else:

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\go_maul\\guihwan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(890, 960, 960, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("guihwan", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for i in range(5):
                                result_loading = loading_check(cla)
                                if result_loading == True:
                                    loading_start(cla)
                                    break
                                QTest.qWait(100)
            else:
                clean_screen_start(cla)
            QTest.qWait(200)
    except Exception as e:
        print(e)


def juljun_off(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start
    from check import out_check, juljun_check
    from function_game import drag_pos


    try:
        print("juljun_off")

        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True

            result_out = out_check(cla)
            if result_out == True:
                is_data = True
            else:
                result_juljun = juljun_check(cla)
                if result_juljun == True:
                    drag_pos(425, 535, 800, 535, cla)
                    QTest.qWait(200)
            QTest.qWait(200)
    except Exception as e:
        print(e)

def juljun_on(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start
    from check import out_check, juljun_check
    from function_game import click_pos_2


    try:
        print("juljun_on")

        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True

            result_juljun = juljun_check(cla)
            if result_juljun == True:
                is_data = True
            else:
                clean_screen_start(cla)
                click_pos_2(15, 915, cla)
                for i in range(5):
                    result_juljun = juljun_check(cla)
                    if result_juljun == True:
                        break
                    QTest.qWait(200)

    except Exception as e:
        print(e)



def attack_on(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start
    from check import out_check, juljun_check
    from function_game import click_pos_2


    try:
        print("attack_on")

        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True

            result_out = out_check(cla)
            if result_out == True:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\attack_check\\out_attack.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 900, 960, 1000, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_data = True
                else:
                    click_pos_2(930, 830, cla)
            else:
                clean_screen_start(cla)
                click_pos_2(930, 830, cla)
                for i in range(5):
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\attack_check\\out_attack.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 900, 960, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        is_data = True
                        break
                    QTest.qWait(200)

    except Exception as e:
        print(e)










