



import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')





def quest_start(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start
    from check import out_check, juljun_check, quest_check, move_ing
    from function_game import click_pos_2, click_pos_reg, imgs_set_, change_number, text_check_get_num , int_put_, in_number_check
    from action import go_maul
    from potion import potion_check
    try:
        print("quest_start", data)

        # 메인, 서브, 일일일

        result_juljun = juljun_check(cla)

        if result_juljun == True:
            result_quest = quest_check(cla)
            if result_quest == True:

                v_.quest_count += 1
                if v_.quest_count % 60 == 1:
                    print(f"{v_.quest_count}번 체크!")
                    potion_check(cla)
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\potion\\potion_setting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 410, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_setting", imgs_)
                        click_pos_2(600, 385, cla)
            else:
                quest_get(cla, data)
        else:
            quest_get(cla, data)

    except Exception as e:
        print(e)


def quest_get(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from clean_screen import clean_screen_start, skip_check, skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for
    from schedule import myQuest_play_add
    from action import menu_open, juljun_on
    # kind_skip = "c:\\my_games\\vam\\data_vam\\imgs\\skip\\skip"
    # kind_skip_list = os.listdir(kind_skip)

    try:
        print("quest_get", data)

        result_data = data.split("_")

        result_now = result_data[1] # 메인, 서브, 일일

        end_get = False
        complete = False

        is_quest = False
        is_quest_count = 0

        while is_quest is False:
            is_quest_count += 1
            if is_quest_count > 7:
                is_quest = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest", imgs_)


                x_reg_1 = 0
                x_reg_2 = 120



                if result_now == "메인":
                    x_reg_1 = 0
                    x_reg_2 = 110

                elif result_now == "서브":
                    x_reg_1 = 120
                    x_reg_2 = 230

                elif result_now == "일일":
                    x_reg_1 = 230
                    x_reg_2 = 340

                x_click = (x_reg_1 + x_reg_2) / 2


                for i in range(5):
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg_1, 80, x_reg_2, 140, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("clicked", imgs_)
                        break
                    else:
                        click_pos_2(x_click, 90, cla)
                    QTest.qWait(500)
                if result_now != "일일":
                    for i in range(30):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\quest.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\bosang.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 150, 800, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("bosang", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                QTest.qWait(300)
                                click_pos_2(910, 1010, cla)
                                QTest.qWait(300)
                                click_pos_2(910, 1010, cla)
                                QTest.qWait(300)
                            result_skip = skip_check(cla)
                            if result_skip == True:
                                skip_start(cla)

                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\jadong_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(780, 980, 960, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("jadong_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\soolock_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 980, 960, 1040, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("soolock_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    complete = True
                                    break
                        else:
                            end_get = True
                            break
                        QTest.qWait(500)
                else:


                    # 일일일
                    for i in range(30):

                        stand_y = 1040

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\complete_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 150, 800, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("complete_checked", imgs_)

                            stand_y = imgs_.y



                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\quest.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\bosang.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 150, 800, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("bosang", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                QTest.qWait(300)
                                click_pos_2(910, 1010, cla)
                                QTest.qWait(300)
                                click_pos_2(910, 1010, cla)
                                QTest.qWait(300)
                            result_skip = skip_check(cla)
                            if result_skip == True:
                                skip_start(cla)

                            else:
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\daily_trinity.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_for(450, 150, 700, stand_y - 20, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("daily_trinity", imgs_)

                                    x_reg = imgs_[len(imgs_) - 1][0]
                                    y_reg = imgs_[len(imgs_) - 1][1]

                                    print("result", x_reg, y_reg)
                                    click_pos_reg(x_reg - 200, y_reg, cla)
                                    QTest.qWait(500)

                                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\soolock_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(780, 980, 960, 1040, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("soolock_btn", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        QTest.qWait(100)

                                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\anymore_quest.PNG" #########더 이상 못 받을때
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(350, 80, 600, 140, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("anymore_quest", imgs_)
                                            end_get = True
                                            break
                        else:
                            break
                        QTest.qWait(300)
                is_quest = True
                if complete == True:
                    myQuest_play_add(cla, data)
                    clean_screen_start(cla)
                else:
                    if end_get == True:

                        for m in range(7):
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(600, 30, 960, 250, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\daily_trinity.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(450, 150, 700, 1020, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 200, imgs_.y, cla)
                                    QTest.qWait(200)
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\soolock_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 980, 960, 1040, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("soolock_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    QTest.qWait(200)
                                else:
                                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\jadong_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(780, 980, 960, 1040, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jadong_btn", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        QTest.qWait(200)

                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\quest\\anymore_quest.PNG"  #########더 이상 못 받을때
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 80, 600, 140, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("anymore_quest", imgs_)
                                    myQuest_play_add(cla, data)
                                    clean_screen_start(cla)
                                    break

                            else:

                                juljun_on(cla)

                                break
                            QTest.qWait(300)


            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu quest", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)