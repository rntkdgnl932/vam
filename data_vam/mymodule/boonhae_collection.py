import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def boonhae_collection_start(cla):
    try:
        print("boonhae_collection_start")
        collection_start(cla)
        boonhae_start(cla)
    except Exception as e:
        print(e)


def collection_start(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start, skip_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open, confirm_all
    from clean_screen import clean_screen_start

    try:
        print("collection_start")

        # 세팅부터터
        collection_setting(cla)

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : collection", imgs_)



                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 670, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("point_1", imgs_)
                    click_pos_2(485, 95, cla)
                    QTest.qWait(200)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(200)

                    point_ready = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\point_2\\"
                    point_ready_list = os.listdir(point_ready)

                    for i in range(len(point_ready_list)):
                        full_path = str(point_ready) + str(point_ready_list[i])
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 100, 670, 990, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("point_ready_list", point_ready_list[i], imgs_)
                            click_pos_2(100, imgs_.y, cla)
                            QTest.qWait(500)

                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\ilgwal_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(810, 970, 960, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("ilgwal_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                QTest.qWait(500)
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\ilgwal_list_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 360, 530, 420, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("ilgwal_list_title", imgs_)
                                    click_pos_2(560, 620, cla)
                                    QTest.qWait(500)
                                confirm_all(cla)


                if is_open == True:
                    clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\collection.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("collection", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                else:
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def collection_setting(cla):
    import numpy as np
    import cv2
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open, confirm_all

    try:
        print("collection_setting")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 10:
                is_open = True

            setting_ready = False
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : collection", imgs_)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\list.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 340, 550, 400, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("list", imgs_)
                    setting_ready = True
                else:
                    click_pos_2(890, 90, cla)


                    for i in range(4):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\list.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 340, 550, 400, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            setting_ready = True
                        QTest.qWait(500)

            if setting_ready == True:

                # 점검 후 마무리
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 455, 460, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("일반 o", imgs_)
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 400, 545, 460, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("고급 o", imgs_)
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(590, 400, 645, 460, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("희귀 x", imgs_)
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(310, 447, 645, 490, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("영웅 이하 x", imgs_)
                                is_open = True

                if is_open == True:
                    for i in range(5):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\list.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 340, 550, 400, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("list", imgs_)
                            confirm_all(cla)
                        else:
                            break
                        QTest.qWait(200)
                else:
                    # 아래는 체크


                    # 일반
                    print("일반 체크중")
                    for i in range(3):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 455, 460, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 455, 460, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    # 고급
                    print("고급 체크중")
                    for i in range(3):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 400, 545, 460, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 400, 545, 460, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    # 고급까지만....(이하 다 지우기)
                    # 첫째줄
                    print("첫째줄 해제중")
                    for i in range(4):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(590, 400, 645, 460, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 400, 545, 460, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                break
                        QTest.qWait(500)
                    # 둘째줄
                    print("둘째줄 해제중")
                    for i in range(10):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(310, 447, 645, 490, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(310, 447, 645, 490, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                break
                        QTest.qWait(500)



            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\collection.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("collection", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                else:
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)




def boonhae_start(cla):
    import numpy as np
    import cv2
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open, confirm_all
    from clean_screen import clean_screen_start, skip_start, skip_check

    try:
        print("boonhae_setting")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 10:
                is_open = True

            setting_ready = False
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\bag.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(650, 30, 960, 250, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : bag", imgs_)
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\ilgwal_boonhae_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(465, 65, 600, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("ilgwal_boonhae_title", imgs_)
                    setting_ready = True
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\bag_ilgwalboonhae_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 900, 780, 960, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("bag_ilgwalboonhae_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                        for i in range(5):
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\ilgwal_boonhae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(465, 65, 600, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                setting_ready = True
                                break
                            QTest.qWait(400)

            if setting_ready == True:

                # 점검 후 마무리
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(375, 880, 420, 920, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("일반 o", imgs_)
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 880, 495, 920, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("고급 o", imgs_)
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae_collection.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(375, 915, 420, 960, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("컬렉션 o", imgs_)

                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae_collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 915, 490, 960, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("거래 o", imgs_)


                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(525, 880, 570, 920, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("희귀 o", imgs_)

                                else:
                                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(520, 915, 650, 960, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("거래, 암거래, 잡화 o", imgs_)

                                    else:
                                        print("거래, 암거래, 잡화 x", imgs_)
                                        is_open = True


                # 아래는 체크

                if is_open == True:

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_selected_boonhae_item_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 450, 650, 570, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("not_selected_boonhae_item_notice", imgs_)
                    else:
                        for i in range(5):
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\ilgwal_boonhae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(465, 65, 600, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("ilgwal_boonhae_title", imgs_)

                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\boonhae_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(830, 910, 900, 970, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("boonhae_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    QTest.qWait(500)
                                    result_skip = skip_check(cla)
                                    if result_skip == True:
                                        skip_start(cla)

                            else:
                                break
                            QTest.qWait(200)
                    clean_screen_start(cla)
                else:

                    # 일반
                    print("일반 체크중")
                    for i in range(3):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(375, 880, 420, 920, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked_boonhae.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(375, 880, 420, 920, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    # 고급
                    print("고급 체크중")
                    for i in range(3):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 880, 495, 920, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked_boonhae.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(450, 880, 495, 920, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    # 컬렉션
                    print("컬렉션 체크중")
                    for i in range(3):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae_collection.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(375, 915, 420, 960, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked_boonhae_collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(375, 915, 420, 960, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    # 거래
                    print("거래 체크중")
                    for i in range(3):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae_collection.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 915, 490, 960, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked_boonhae_collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 915, 490, 960, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    # 고급까지만....(이하 다 지우기)
                    # 첫째줄
                    print("첫째줄 해제중(희귀)")
                    for i in range(4):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(525, 880, 570, 920, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked_boonhae.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(525, 880, 570, 920, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                break
                        QTest.qWait(500)
                    # 둘째줄 암거래, 잡화 x
                    print("둘째줄 해제중")
                    for i in range(10):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\checked_boonhae.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(520, 915, 650, 960, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("checked", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\boonhae_collection\\not_checked_boonhae.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(520, 915, 650, 960, cla, img, 0.65)
                            if imgs_ is not None and imgs_ != False:
                                print("not_checked", imgs_)
                                break
                        QTest.qWait(500)



            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\bag.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bag", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                else:
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)