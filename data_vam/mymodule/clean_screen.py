import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


kind_skip = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip"
kind_skip_list = os.listdir(kind_skip)

kind_way = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click"
kind_way_list = os.listdir(kind_way)

kind_close = "c:\\my_games\\vam\\data_vam\\imgs\\clean_screen\\close"
kind_close_list = os.listdir(kind_close)


def clean_screen_start(cla):
    from schedule import myQuest_play_check
    from action import juljun_off
    from check import out_check, juljun_check

    try:
        print("clean_screen_start")
        result_out = out_check(cla)
        if result_out == False:

            is_out = False
            is_out_count = 0

            while is_out is False:
                is_out_count += 1
                if is_out_count > 7:
                    is_out = True

                result_out = out_check(cla)
                if result_out == False:
                    result_juljun = juljun_check(cla)
                    if result_juljun == True:
                        juljun_off(cla)
                    else:
                        close_click(cla)
                        QTest.qWait(100)
                        all_skip(cla)
                        QTest.qWait(100)
                else:
                    break
                QTest.qWait(100)
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

            for i in range(len(kind_close_list)):
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\clean_screen\\close\\" + str(kind_close_list[i])
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("close_list", kind_close_list[i], imgs_)


                    if kind_close_list[i] == "server.PNG":
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\server.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 320, 340, 360, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(833, 333, cla)
                            is_close = True
                    else:
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

    from schedule import myQuest_play_check

    try:
        print("skip_check")

        result_schedule = myQuest_play_check(cla, "check")
        result_schedule_ = result_schedule[0][2]

        result_skip = skip_check(cla)
        if result_skip == True:
            skip_start(cla)
        else:

            if result_schedule_ == "튜토육성":

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

        for i in range(len(kind_skip_list)):

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip\\" + str(kind_skip_list[i])
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("skip_list", kind_skip_list[i], imgs_)
                is_skip = True
                break
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

            for i in range(len(kind_skip_list)):

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip\\" + str(kind_skip_list[i])
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("skip_list", kind_skip_list[i], imgs_)
                    is_skip = True

                    result_way = way_check(cla)

                    if result_way == True:
                        way_start(cla)
                    else:
                        print("클릭하자", imgs_.x, imgs_.y)
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

        for i in range(len(kind_way_list)):

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click\\" + str(kind_way_list[i])
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("kind_way_list", kind_way_list[i], imgs_)
                is_way = True
                break

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

            for i in range(len(kind_way_list)):

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click\\" + str(kind_way_list[i])
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("kind_way_list", kind_way_list[i], imgs_)
                    is_way = True

                    # up_right_1, down_right_1...

                    # x
                    # left = - 25, - 30
                    # right = + 25, + 30

                    # y
                    # up = - 25, - 30
                    # down = + 25, + 30
                    #
                    result_des = kind_way_list[i].split("_")
                    if result_des[0] == "up":
                        y_reg_1 = -25
                        y_reg_2 = -30
                    elif result_des[0] == "down":
                        y_reg_1 = +25
                        y_reg_2 = +30

                    if result_des[1] == "left":
                        x_reg_1 = -25
                        x_reg_2 = -30
                    elif result_des[1] == "right":
                        x_reg_1 = +25
                        x_reg_2 = +30


                    click_pos_reg(imgs_.x + x_reg_1, imgs_.y + y_reg_1, cla)
                    QTest.qWait(100)
                    click_pos_reg(imgs_.x + x_reg_2, imgs_.y + y_reg_2, cla)
                    is_action_count = 0

                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\way_click_bag.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("way_click_bag", imgs_)
                        click_pos_2(880, 50, cla)


            if is_way == True:
                QTest.qWait(1000)
            else:
                result_confirm = confirm_all(cla)
                if result_confirm == True:
                    is_action_count = 0
                else:
                    is_action_count += 2
            QTest.qWait(1000)

    except Exception as e:
        print(e)