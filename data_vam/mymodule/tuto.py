import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2


    from clean_screen import all_skip
    from check import out_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_

    try:
        print("tuto_start")
        story_start(cla)

        all_skip(cla)

        result_out = out_check(cla)
        if result_out == True:

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\tuto\\q_clear.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 60, 920, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("q_clear", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\tuto\\quest_check\\quest_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 780, 960, 880, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("quest_btn", imgs_)

                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\tuto\\sub_q_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 100, 720, 200, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("sub_q_1", imgs_)
                        click_pos_reg(imgs_.x + 100, imgs_.y + 5, cla)
                    else:
                        click_pos_2(800, 100, cla)
    except Exception as e:
        print(e)


def story_start(cla):
    import numpy as np
    import cv2
    from check import bag_open_check, menu_open_check
    from action import confirm_all
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from potion import maul_potion

    try:
        print("story_start")

        result_bag_open = bag_open_check(cla)
        if result_bag_open == True:
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\action\\bag_open\\skill_book.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("skill_book", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)
                confirm_all(cla)
            click_pos_2(880, 50, cla)
        else:
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\tuto\\jangchak_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("jangchak_btn", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)
            else:
                result_menu_open = menu_open_check(cla)
                if result_menu_open == True:
                    click_pos_2(930, 45, cla)


        # 잡화상점
        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\jabhwa.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 30, 960, 300, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jabhwa", imgs_)
            maul_potion(cla)

        # 잡화상점
        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\quest.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 30, 960, 300, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest", imgs_)
            confirm_all(cla)

    except Exception as e:
        print(e)

