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
    from check import out_check
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
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_dead = True
        else:
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\boohwal_btn_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("boohwal_btn_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_dead = True
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\recovery_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 300, 300, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("recovery_btn", imgs_)
                    is_dead = True

        if is_dead == True:
            for i in range(10):
                result_out = out_check(cla)
                if result_out == True:

                    break
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\boohwal_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("boohwal_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\boohwal_btn_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("boohwal_btn_2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                QTest.qWait(1000)
            dead_recovery(cla)
        return is_dead
    except Exception as e:
        print(e)


def dead_recovery(cla):
    import numpy as np
    import cv2

    from schedule import myQuest_play_add, myQuest_play_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from potion import maul_potion
    from check import out_check

    try:
        print("dead_recovery")



        if v_.recovery == True:
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\recovery_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 300, 300, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("recovery_btn", imgs_)
                dead_recovery_btn(cla)



        maul_potion(cla)

        result_schedule = myQuest_play_check(cla, "check")
        result_schedule_ = result_schedule[0][2]

        if result_schedule_ == "튜토육성":
            myQuest_play_add(cla, result_schedule_)


    except Exception as e:
        print(e)


def dead_recovery_btn(cla):



    import numpy as np
    import cv2
    import pyautogui
    import random

    from action import attack_on, juljun_on, menu_open, confirm_all, go_random
    from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for
    from clean_screen import close_click
    from potion import maul_potion
    from check import confirm_all_check
    # kind_skip = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip"
    # kind_skip_list = os.listdir(kind_skip)

    try:
        print("dead_recovery_btn")

        is_check = False
        is_check_count = 0

        while is_check is False:
            is_check_count += 1
            if is_check_count > 10:
                is_check = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\recovery_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 300, 250, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("recovery_title", imgs_)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\dia.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 300, 250, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dia", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\free_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 950, 300, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("free_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(100)

                    for i in range(5):
                        result_confirm = confirm_all_check(cla)
                        if result_confirm == True:
                            confirm_all(cla)
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\lack_boohwal_ticket_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 60, 600, 150, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("lack_boohwal_ticket_notice", imgs_)
                                is_check = True
                                break
                        QTest.qWait(200)
                else:
                    is_check = True
                    v_.recovery = False

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\recovery_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 300, 250, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("recovery_title", imgs_)
                else:
                    is_check = True


            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\recovery_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 300, 300, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("recovery_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            if is_check == True:
                for i in range(5):
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dead_die\\recovery_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 300, 250, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("recovery_title", imgs_)
                        close_click(cla)
                    else:
                        break
                    QTest.qWait(200)

            QTest.qWait(500)


    except Exception as e:
        print(e)

