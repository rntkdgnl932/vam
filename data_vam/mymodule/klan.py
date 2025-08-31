import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def klan_start(cla):
    from boonhae_collection import boonhae_collection_start
    try:
        print("klan_start")

        klan_donation(cla)

    except Exception as e:
        print(e)

def klan_donation(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
    from clean_screen import clean_screen_start

    try:
        print("klan_donation")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\klan.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("klan", imgs_)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\klan\\donation_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 970, 870, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("donation_btn", imgs_)

                    for i in range(15):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\klan\\lack_donation_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 80, 570, 130, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("lack_donation_notice", imgs_)
                            is_open = True
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\klan\\donation_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 320, 540, 400, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("donation_title", imgs_)
                                click_pos_2(400, 640, cla)
                            else:
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\klan\\donation_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(670, 970, 870, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("donation_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                        QTest.qWait(200)

                else:
                    is_open = True

                if is_open == True:
                    clean_screen_start(cla)

            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\klan.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("klan", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)