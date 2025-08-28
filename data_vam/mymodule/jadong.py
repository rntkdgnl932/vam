



import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')





def jadong_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start
    from check import out_check, juljun_check, attack_check, move_ing
    from function_game import click_pos_2, click_pos_reg, imgs_set_, change_number, text_check_get_num , int_put_, in_number_check
    from action import go_maul
    from potion import potion_check
    try:
        print("jadong_start")

        result_juljun = juljun_check(cla)

        if result_juljun == True:
            result_attack = attack_check(cla)
            if result_attack == True:
                potion_check(cla)
            else:
                jadong_spot(cla)
        else:
            jadong_spot(cla)

    except Exception as e:
        print(e)


def jadong_spot(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from action import attack_on, juljun_on
    from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for
    from massenger import line_to_me
    from potion import maul_potion
    # kind_skip = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip"
    # kind_skip_list = os.listdir(kind_skip)

    try:
        print("jadong_spot")

        maul_potion(cla)


        is_check = False
        is_check_count = 0

        while is_check is False:
            is_check_count += 1
            if is_check_count > 5:
                is_check = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\jadong\\favorite.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 60, 150, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\jadong\\star.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_for(280, 110, 340, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("star", imgs_)

                        if len(imgs_) > 0:
                            #
                            ran_star_ready = random.randint(1, len(imgs_))
                            ran_star = ran_star_ready - 1
                            print("result", imgs_[ran_star][0])
                            print("result", imgs_[ran_star][1])
                            x_reg = int(imgs_[ran_star][0])
                            y_reg = int(imgs_[ran_star][1])

                            for i in range(10):
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\worldmap.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(x_reg - 100, y_reg, cla)
                                    QTest.qWait(500)
                                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\jadong\\soongan_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(340, 150, 650, 900, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    # 자동사냥하기
                                    attack_on(cla)
                                    juljun_on(cla)
                                    is_check = True
                                    break
                                QTest.qWait(500)
                        else:
                            why = "자동사냥터 정해야 한다."
                            line_to_me(cla, why)

                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\jadong\\star_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 50, 70, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("star_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                click_pos_2(100, 130, cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)