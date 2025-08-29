



import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')





def dun_start(cla, data):
    import numpy as np
    import cv2
    from check import juljun_check, attack_check
    from function_game import imgs_set_
    from potion import potion_check
    try:
        print("dun_start", data)

        # 던전_일반_창조의심연_1 // simyun
        # 던전_일반_빛바랜유산_1 // yousan
        # 던전_일반_고대의공방_1 // gongbang
        split_data = data.split("_")

        dun_2 = split_data[2]

        if dun_2 == "창조의심연":
            dun_name = "simyun"
        elif dun_2 == "빛바랜유산":
            dun_name = "yousan"
        elif dun_2 == "고대의공방":
            dun_name = "gongbang"

        result_juljun = juljun_check(cla)

        if result_juljun == True:

            # 해당 장소에 있는지....
            # 던전_일반_창조의심연_1_하
            # 던전_일반_빛바랜유산_1_중
            # 던전_일반_고대의공방_1_상
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dungeon\\" + str(dun_name) + "\\juljun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 60, 150, 150, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_title", str(dun_name), imgs_)

                result_attack = attack_check(cla)
                if result_attack == True:
                    potion_check(cla)
                else:
                    dun_spot(cla, data)
            else:
                if v_.now_dun_name == "none":
                    dun_spot(cla, data)
                else:
                    potion_check(cla)
        else:
            dun_spot(cla, data)

    except Exception as e:
        print(e)


def dun_spot(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from action import attack_on, juljun_on, menu_open, confirm_all, go_random
    from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for
    from clean_screen import clean_screen_start
    from potion import maul_potion
    from check import confirm_all_check
    # kind_skip = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip"
    # kind_skip_list = os.listdir(kind_skip)

    try:
        print("dun_spot")

        maul_potion(cla)

        # 던전_일반_창조의심연_1_하 // simyun
        # 던전_일반_빛바랜유산_1_중 // yousan
        # 던전_일반_고대의공방_1_상 // gongbang
        split_data = data.split("_")
        dun_1 = split_data[1]
        dun_2 = split_data[2]
        dun_3 = split_data[3]
        dun_4 = split_data[4]



        if dun_2 == "창조의심연":
            dun_name = "simyun"
            click_title_y = 160
        elif dun_2 == "빛바랜유산":
            dun_name = "yousan"
            click_title_y = 245
        elif dun_2 == "고대의공방":
            dun_name = "gongbang"
            click_title_y = 330
        # 145, 195....(+50...)

        click_step_y = 95 + (int(dun_3) * 50)


        is_check = False
        is_check_count = 0

        while is_check is False:
            is_check_count += 1
            if is_check_count > 15:
                is_check = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\dungeon.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon", imgs_)

                if dun_1 == "일반":
                    click_pos_2(60, 90, cla)
                elif dun_1 == "에픽":
                    click_pos_2(180, 90, cla)



                for i in range(9):
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("dungeon", imgs_)

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dungeon\\already_join_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(360, 70, 650, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("already_join_notice", str(dun_name), imgs_)
                            clean_screen_start(cla)
                            break
                        else:
                            result_confirm = confirm_all_check(cla)
                            if result_confirm == True:
                                confirm_all(cla)
                            else:

                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dungeon\\" + str(dun_name) + "\\click_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(185, 135, 385, 195, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("click_title", str(dun_name), imgs_)
                                    click_pos_2(840, click_step_y, cla)
                                else:
                                    click_pos_2(100, click_title_y, cla)
                    else:
                        break
                    QTest.qWait(1000)
                # 랜덤이동 추가
                QTest.qWait(1000)
                result_reg = dun_get_x_y(data)
                dun_spot_difficulty(cla, result_reg)
                attack_on(cla)
                juljun_on(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(660, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dungeon", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def dun_spot_difficulty(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from action import attack_on, juljun_on, menu_open, confirm_all, go_random
    from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for
    from clean_screen import clean_screen_start
    from potion import maul_potion
    from check import confirm_all_check
    # kind_skip = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip"
    # kind_skip_list = os.listdir(kind_skip)

    try:
        print("dun_spot_difficulty", data)



        is_check = False
        is_check_count = 0

        while is_check is False:
            is_check_count += 1
            if is_check_count > 15:
                is_check = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\dungeon_map.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon_map", imgs_)

                for i in range(10):
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\dungeon_map.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\dungeon\\82_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 100, 900, 950, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("82_move", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            click_pos_2(int(data[0]), int(data[1]), cla)
                    else:
                        is_check = True
                        break
                    QTest.qWait(1000)



            else:
                click_pos_2(100, 130, cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def dun_get_x_y(data):

    try:
        print("dun_spot_difficulty", data)

        # 던전_일반_창조의심연_1_하 // simyun
        # 던전_일반_빛바랜유산_1_중 // yousan
        # 던전_일반_고대의공방_1_상 // gongbang
        split_data = data.split("_")
        dun_1 = split_data[1]
        dun_2 = split_data[2]
        dun_3 = split_data[3]
        dun_4 = split_data[4]

        x_reg = 250
        y_reg = 410

        yet_data_1 = 250
        yet_data_2 = 410

        if dun_2 == "창조의심연":
            if dun_3 == "1":
                if dun_4 == "상":
                    x_reg = 545
                    y_reg = 645
                elif dun_4 == "중":
                    x_reg = 560
                    y_reg = 320
                elif dun_4 == "하":
                    x_reg = 251
                    y_reg = 410
            elif dun_3 == "2":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "3":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "4":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "5":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "6":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "7":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
        if dun_2 == "빛바랜유산":
            if dun_3 == "1":
                if dun_4 == "상":
                    x_reg = 251
                    y_reg = 410
                elif dun_4 == "중":
                    x_reg = 560
                    y_reg = 320
                elif dun_4 == "하":
                    x_reg = 600
                    y_reg = 580
            elif dun_3 == "2":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "3":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "4":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "5":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "6":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "7":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2

        if dun_2 == "고대의공방":
            if dun_3 == "1":
                if dun_4 == "상":
                    x_reg = 350
                    y_reg = 375
                elif dun_4 == "중":
                    x_reg = 735
                    y_reg = 355
                elif dun_4 == "하":
                    x_reg = 500
                    y_reg = 580
            elif dun_3 == "2":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "3":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "4":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "5":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "6":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
            elif dun_3 == "7":
                if dun_4 == "상":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "중":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
                elif dun_4 == "하":
                    x_reg = yet_data_1
                    y_reg = yet_data_2
        return x_reg, y_reg
    except Exception as e:
        print(e)