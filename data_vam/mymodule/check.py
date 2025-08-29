import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def out_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_

    try:
        print("out_check")

        is_out = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\out\\talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 800, 100, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("talk", imgs_)

            result_menu = menu_open_check(cla)
            if result_menu == False:
                is_out = True

        return is_out

    except Exception as e:
        print(e)





def loading_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("loading_check")

        is_loding = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\loading\\loding_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 680, 300, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("loding_1", imgs_)
            is_loding = True

        return is_loding

    except Exception as e:
        print(e)


def loading_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("loading_check 30 680 300 900")

        is_loding = False
        is_loding_count = 0

        while is_loding is False:
            is_loding_count += 1
            if is_loding_count > 10:
                is_loding = True

            is_load = False

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\loading\\loding_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 680, 300, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("loding_1", imgs_)
                is_load = True

            if is_load == True:
                is_loding_count = 0
                QTest.qWait(1000)
            else:
                is_loding_count += 1
            QTest.qWait(1000)



    except Exception as e:
        print(e)



def jangsigan_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open
    from massenger import line_to_me

    try:
        print("jangsigan_check")


        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\longtime\\jangsigan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 400, 600, 640, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan", imgs_)
            line_to_me(cla, "장시간 미접속")

    except Exception as e:
        print(e)


def move_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("move_check")

        is_move = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\move\\move_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(460, 840, 550, 880, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("move_2", imgs_)
            is_move = True

        return is_move

    except Exception as e:
        print(e)

def move_ing(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("move_ing")

        is_move = True
        is_move_count = 0
        while is_move is True:
            is_move_count += 1
            if is_move_count > 7:
                is_move = False
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\move\\move_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(460, 840, 550, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("move_2", imgs_)
                is_move_count = 0
            else:
                is_move_count += 1
            QTest.qWait(200)
        return is_move

    except Exception as e:
        print(e)


def bag_open_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("bag_open_check")

        is_bag = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\bag_open\\ilhwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            is_bag = True

        return is_bag
    except Exception as e:
        print(e)



def maul_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import all_skip
    from check import out_check, loading_check, loading_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_


    try:
        print("maul_check")

        is_data = False
        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\go_maul\\jabhwa.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 800, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jabhwa", imgs_)
            is_data = True
        else:
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\go_maul\\jangbi.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 800, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("jangbi", imgs_)
                is_data = True
        return is_data
    except Exception as e:
        print(e)


def juljun_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import all_skip
    from check import out_check, loading_check, loading_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_


    try:
        print("juljun_check")

        is_data = False
        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\juljun\\juljun_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 30, 650, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("juljun_ing", imgs_)
            is_data = True


            # v_.dun_list = ["simyun", "yousan", "gongbang"]

            v_.now_dun_name = "none"

            for i in range(len(v_.dun_list)):
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dungeon\\" + str(v_.dun_list[i]) + "\\juljun_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 60, 150, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_dun_list", str(v_.dun_list[i]), imgs_)
                    v_.now_dun_name = str(v_.dun_list[i])

        else:
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\juljun\\juljun_check_potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 30, 650, 100, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("juljun_check_potion", imgs_)
                is_data = True

        return is_data
    except Exception as e:
        print(e)


def menu_open_check(cla):
    import numpy as np
    import cv2

    from function_game import click_pos_2, click_pos_reg, imgs_set_

    try:
        print("menu_open_check")

        is_open = False
        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\post.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("menu : post", imgs_)

            is_open = True

        return is_open
    except Exception as e:
        print(e)


def attack_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import all_skip
    from check import out_check, maul_check, move_check, move_ing
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import go_maul

    try:
        print("attack_check")

        is_attack = False

        result_out = out_check(cla)
        if result_out == True:

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\attack_check\\out_attack.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 900, 960, 1000, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("out_attack", imgs_)

                is_attack = True
        else:
            result_juljun = juljun_check(cla)

            if result_juljun == True:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\attack_check\\juljun_attack.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 900, 550, 1000, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_attack", imgs_)
                    is_attack = True
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\attack_check\\juljun_attack_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 900, 550, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("juljun_attack_potion", imgs_)
                        is_attack = True

        return is_attack
    except Exception as e:
        print(e)


def auto_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("auto_check")

        is_on = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\auto\\auto_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 800, 960, 860, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("auto_on", imgs_)
            is_on = True
        else:
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\auto\\auto_off.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 800, 960, 860, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("auto_off", imgs_)
                is_on = True

        return is_on

    except Exception as e:
        print(e)


def confirm_all_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    kind_confirm = "c:\\my_games\\vam\\data_vam\\imgs\\action\\confirm_all"
    kind_confirm_list = os.listdir(kind_confirm)
    try:
        print("confirm_all_check")

        is_confirm = False

        for i in range(len(kind_confirm_list)):

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\confirm_all\\" + str(kind_confirm_list[i])
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1000, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("confirm_1", imgs_)
                is_confirm = True
                break

        return is_confirm
    except Exception as e:
        print(e)