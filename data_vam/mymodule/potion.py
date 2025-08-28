import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def potion_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start
    from check import out_check, juljun_check, move_check, move_ing
    from function_game import click_pos_2, click_pos_reg, imgs_set_, change_number, text_check_get_num , int_put_, in_number_check
    from action import go_maul

    try:
        print("potion_check")

        result_out = out_check(cla)

        result_juljun = juljun_check(cla)
        x_reg = 230
        if result_out != True and result_juljun != True:
            clean_screen_start(cla)
        else:
            if result_out == True:
                x_reg = 230
            elif result_juljun == True:
                x_reg = 470

        is_zero = False
        potion_zero = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\potion_zero\\"
        potion_zero_list = os.listdir(potion_zero)

        for i in range(len(potion_zero_list)):
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\potion_zero\\" + potion_zero_list[i]
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 970, 250, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("potion_zero_list", potion_zero_list[i], imgs_)
                is_zero = True
                break
        if is_zero == True:
            maul_potion(cla)
        else:
            is_check = False
            is_check_count = 0

            while is_check is False:
                is_check_count += 1
                if is_check_count > 5:
                    is_check = True


                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\potion_setting.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 350, 550, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("potion_setting", imgs_)

                    result_num_ready = text_check_get_num(404, 673, 440, 685, cla)
                    print("result_num_ready", result_num_ready)
                    result_num = change_number(result_num_ready)
                    print("result_num", result_num)

                    int_num = int_put_(result_num)

                    result_bool = in_number_check(int_num)
                    if result_bool == True:

                        is_check = True

                        if int(int_num) < 100:
                            v_.potion_count += 1

                            if v_.potion_count > 2:
                                maul_potion(cla)

                else:
                    click_pos_2(x_reg, 1000, cla)
                    QTest.qWait(1000)

    except Exception as e:
        print(e)



def maul_potion(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from boonhae_collection import boonhae_collection_start
    from check import out_check, maul_check, move_check, move_ing
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import go_maul

    try:
        print("maul_potion")

        is_buy = False
        is_buy_count = 0
        while is_buy is False:
            is_buy_count +=1
            if is_buy_count > 7:
                is_buy = True
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 300, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("jabhwa", imgs_)
                ilgwal_buy(cla)

                # boonhae_collection_start(cla)

                is_buy = True
                v_.potion_count = 0
            else:

                result_maul = maul_check(cla)
                if result_maul == False:
                    go_maul(cla)
                else:
                    click_pos_2(765, 890, cla)
                    QTest.qWait(200)
                    result_move = move_check(cla)
                    if result_move == True:
                        move_ing(cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\jabhwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 30, 960, 300, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        QTest.qWait(500)
            QTest.qWait(200)
    except Exception as e:
        print(e)


def ilgwal_buy(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import all_skip
    from check import out_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_, drag_pos
    from clean_screen import clean_screen_start

    try:
        print("ilgwal_buy")

        is_buy = False
        is_buy_count = 0
        while is_buy is False:
            is_buy_count += 1
            if is_buy_count > 20:
                is_buy = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\not_selected_notice.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 30, 700, 300, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("not_selected_notice", imgs_)
                is_buy = True
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\anymore_buy_notice.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 30, 700, 300, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("anymore_buy_notice", imgs_)
                    is_buy = True
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\not_ilgwal_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 30, 700, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("not_ilgwal_notice", imgs_)

                        ilgwal_setting(cla)

                    else:

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\ilgwal_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 700, 640, 750, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("ilgwal_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for i in range(5):
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\ilgwal_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 700, 640, 750, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("ilgwal_btn", imgs_)
                                    drag_pos(430, 580, 430, 300, cla)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    is_buy = True
                                    break
                                else:
                                    click_pos_2(200, 1000, cla)
                                QTest.qWait(500)

                        else:
                            click_pos_2(200, 1000, cla)

            if is_buy == True:
                clean_screen_start(cla)

            QTest.qWait(200)


    except Exception as e:
        print(e)


def ilgwal_setting(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import all_skip
    from check import out_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_

    try:
        print("ilgwal_setting")

        is_buy = False
        is_buy_count = 0
        while is_buy is False:
            is_buy_count += 1
            if is_buy_count > 20:
                is_buy = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\ilgwal_list_update_notice.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 30, 700, 300, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("ilgwal_list_update_notice", imgs_)
                is_buy = True
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\ilgwal_list.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 60, 150, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("ilgwal_list", imgs_)

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\zero.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 100, 200, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("zero", imgs_)
                        click_pos_reg(imgs_.x + 80, imgs_.y, cla)

                    else:
                        click_pos_2(200, 1000, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\ilgwal_list_update_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 30, 700, 300, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("ilgwal_list_update_notice", imgs_)
                                is_buy = True
                                break
                            QTest.qWait(100)

                else:
                    click_pos_2(70, 1000, cla)
                    QTest.qWait(500)
            QTest.qWait(500)

    except Exception as e:
        print(e)
