import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def clean_screen_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("clean_screen_start")



    except Exception as e:
        print(e)


def close_click(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("close_click")

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 5:
                is_action = True

            is_close = False

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\clean_screen\\close_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("close_1", imgs_)
                is_close = True
                click_pos_reg(imgs_.x, imgs_.y, cla)

            if is_close == True:
                is_action_count = 0
                QTest.qWait(1000)
            else:
                is_action_count += 1
                QTest.qWait(200)

    except Exception as e:
        print(e)

def all_skip(cla):
    import numpy as np
    import cv2
    from action import confirm_all

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("skip_check")

        result_skip = skip_check(cla)
        if result_skip == True:
            skip_start(cla)
        else:
            result_way = way_start(cla)
            if result_way == True:
                way_start(cla)
            else:
                confirm_all(cla)

    except Exception as e:
        print(e)


def skip_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("skip_check")

        is_skip = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            is_skip = True
        return is_skip
    except Exception as e:
        print(e)

def skip_start(cla):
    import numpy as np
    import cv2
    from action import confirm_all

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

                result_way = way_check(cla)

                if result_way == True:
                    way_start(cla)
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)


            if is_skip == True:
                QTest.qWait(1000)
            else:
                result_confirm = confirm_all(cla)
                if result_confirm == False:
                    is_action = True
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def way_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("way_check")

        is_way = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click\\up_right_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("up_right_1", imgs_)
            is_way = True
        else:
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click\\down_left_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("down_left_1", imgs_)
                is_way = True
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click\\down_right_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("down_right_1", imgs_)
                    is_way = True
        return is_way
    except Exception as e:
        print(e)

def way_start(cla):
    import numpy as np
    import cv2
    from action import confirm_all

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
                click_pos_reg(imgs_.x + 25, imgs_.y - 25, cla)
                QTest.qWait(100)
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
                    click_pos_reg(imgs_.x - 25, imgs_.y + 25, cla)
                    QTest.qWait(100)
                    click_pos_reg(imgs_.x - 30, imgs_.y + 30, cla)
                    is_action_count = 0
                    is_way = True
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click\\down_right_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("down_right_1", imgs_)
                        click_pos_reg(imgs_.x + 25, imgs_.y + 25, cla)
                        QTest.qWait(100)
                        click_pos_reg(imgs_.x + 30, imgs_.y + 30, cla)
                        is_action_count = 0
                        is_way = True

            if is_way == True:
                QTest.qWait(1000)
            else:
                result_confirm = confirm_all(cla)
                if result_confirm == True:
                    is_action_count = 0
                else:
                    is_action_count += 1
            QTest.qWait(1000)

    except Exception as e:
        print(e)