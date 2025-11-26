import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

get_ready = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\get_ready\\"
get_ready_list = os.listdir(get_ready)
get_e_ready = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\e_point\\"
get_e_ready_list = os.listdir(get_e_ready)
get_e_title = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\title\\"
get_e_title_list = os.listdir(get_e_title)

checked = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\checked\\"


def get_start(cla):
    from boonhae_collection import boonhae_collection_start
    from klan import klan_donation
    try:
        print("get_start")

        boonhae_collection_start(cla)

        get_post(cla)
        get_upjuk(cla)
        get_event(cla)
        get_special(cla)
        get_sangjum_start(cla)
        get_inmool(cla)
        get_chosanghwa(cla)
        get_acave(cla)
        get_malyuc(cla)
        get_guild(cla)

        klan_donation(cla)


    except Exception as e:
        print(e)

def get_post(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open_pure
    from clean_screen import clean_screen_start

    try:
        print("get_post")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("post", imgs_)

                is_open = True

                for i in range(4):
                    x_reg = 60 + (i * 110)
                    click_pos_2(x_reg, 95, cla)
                    QTest.qWait(500)

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\post\\anymore_post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 50, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore_post", imgs_)
                    else:
                        # full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\post\\post_point_1.PNG"
                        # img_array = np.fromfile(full_path, np.uint8)
                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        # imgs_ = imgs_set_(40, 50, 960, 110, cla, img, 0.8)
                        # if imgs_ is not None and imgs_ != False:
                        #     print("post_point_1", imgs_)
                        #     click_pos_reg(imgs_.x - 40, imgs_.y + 10, cla)

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\post\\all_get_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 50, 960, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("all_get_btn", imgs_)

                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            QTest.qWait(500)
                            skip_start(cla)
                clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\post.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("post", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_upjuk(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open_pure
    from clean_screen import clean_screen_start, skip_check


    try:
        print("get_upjuk")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\upjuk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 30, 960, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("upjuk", imgs_)


                is_point = False
                for i in range(len(get_e_ready_list)):
                    full_path = str(get_e_ready) + str(get_e_ready_list[i])
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 60, 850, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("get_e_ready_list", get_e_ready_list[i], imgs_)
                        is_point = True
                        break
                if is_point == True:




                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\post\\all_get_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 50, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("all_get_btn", imgs_)
                        for i in range(4):
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            QTest.qWait(500)
                else:
                    result_skip = skip_check(cla)
                    if result_skip == True:
                        skip_start(cla)
                    else:
                        is_open = True
                        clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\upjuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("upjuk", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)

def get_event(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import drag_pos, click_pos_reg, imgs_set_
    from action import menu_open_pure
    from clean_screen import clean_screen_start







    try:
        print("get_event")


        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 15:
                is_open = True

            last_event = False

            is_event = False

            for i in range(len(get_e_title_list)):
                full_path = str(get_e_title) + str(get_e_title_list[i])
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(270, 300, 860, 760, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_e_title_list", get_e_title_list[i], imgs_)
                    is_event = True

                    break

            if is_event == True:
                is_point = False

                e_x_reg = 0
                e_y_reg = 0

                point_kind = "none"

                for n in range(2):

                    for i in range(len(get_e_ready_list)):
                        full_path = str(get_e_ready) + str(get_e_ready_list[i])
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(240, 310, 300, 750, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("get_e_ready_list", get_e_ready_list[i], imgs_)
                            click_pos_reg(imgs_.x - 50, imgs_.y + 20, cla)
                            is_point = True

                            point_kind = get_e_ready_list[i]

                            e_x_reg = imgs_.x
                            e_y_reg = imgs_.y

                            break



                if is_point == True:
                    # 번호 붙여서 ㄱㄱ

                    for i in range(len(get_e_title_list)):
                        full_path = str(get_e_title) + str(get_e_title_list[i])
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(270, 300, 860, 760, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("get_e_title_list", get_e_title_list[i], imgs_)
                            get_event_start(cla, get_e_title_list[i], e_x_reg, e_y_reg, point_kind)
                            QTest.qWait(500)
                            break



                else:

                    if is_point == False:

                        ##############################################
                        ######### 마지막 이벤트 확인하기  ###################
                        ##############################################

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\last_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(105, 685, 290, 750, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("last_checked", imgs_)
                            last_event = True
                        else:
                            drag_pos(220, 720, 220, 350, cla)

                    QTest.qWait(500)


                    if last_event == True:
                        is_open = True
                        clean_screen_start(cla)
            else:

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\event.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("event", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_event_start(cla, data, e_x_reg, e_y_reg, point_kind):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for, drag_pos
    from action import confirm_all
    from clean_screen import clean_screen_start

    plus = 0

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    reg = 15

    try:
        print("get_event_start", data)


        num_ready = data.split(".")
        num = num_ready[0]

        # 삭제 : 9, 10

        # 1 : 위대한시작!영웅의서약(seven_five_eight) o

        # 2 : 100일전야제!밤의출석이벤트(fourteen) o

        # 3 : 피의강화(eight) o

        # 4 : 리턴트리니티랭킹이벤트(right) o

        # 5 : 데일리출석(tewnty_one) o

        # 6 : 트리니티사용!(eight) o

        # 7 : 쉬마의특명!영웅의서약(seven_five_eight) o

        # 8 : 블랙코인미션이벤트(eight) o

        # 9 :

        # 10 :

        # 11 :

        # 12 :

        # 13 :

        # 14 :

        # 15 :

        ##############################################
        ######### 마지막 이벤트 확인하기  ###################
        ##############################################


        # new

        # ? : 피의결속!출석이벤트(seven) 9

        # ? : 100일전야제준비이벤트(eight) 10

        # ? : 영역침공이벤트(pass) 11

        # ? : 막아라!영역침공(eight) 12

        # ? :

        # ? :

        # ? :

        ##############################################
        ######### 마지막 이벤트 확인하기  ###################
        ##############################################
        # 삭제 : 3, 4,

        kind = "none"

        if num == "1" or num == "7":
            kind = "seven_five_eight"

        elif num == "5":
            kind = "tewnty_one"

        elif num == "2":
            kind = "common"

        elif num == "0":
            kind = "random"

        elif num == "9" or num == "0" or num == "0":
            kind = "seven"

        elif num == "10" or num == "6" or num == "3" or num == "8" or num == "12":
            kind = "eight"

        elif num == "4":
            kind = "right"

        elif num == "11" or num == "0":
            kind = "pass"

        print("kind", kind)

        is_open = False

        if kind == "pass":
            is_open = True

        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 15:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\title\\" + str(data)
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(270, 300, 860, 760, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("get_e_title_list", str(data), imgs_)
                QTest.qWait(500)

                is_point = False
                # 왼쪽 포인트
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\e_point\\" + str(point_kind)
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(e_x_reg - plus - reg, e_y_reg - reg, e_x_reg - plus + reg, e_y_reg + reg, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_event_start: get_e_ready_list", str(point_kind), imgs_)
                    click_pos_reg(imgs_.x - 50, imgs_.y + 20, cla)
                    is_point = True

                if is_point == True:
                    QTest.qWait(500)
                    # seven_five_eight point
                    if kind == "seven_five_eight":
                        for i in range(len(get_e_ready_list)):
                            full_path = str(get_e_ready) + str(get_e_ready_list[i])
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(290, 400, 850, 450, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("get_e_ready_list", get_e_ready_list[i], imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                                QTest.qWait(500)
                                break
                        # common point

                        for i in range(5):
                            x_click = 430
                            if i > 2:
                                x_click = 700
                            y_click = 480 + (i * 70)
                            if i > 2:
                                y_click = 480 + ((i - 3) * 70)
                            click_pos_2(x_click, y_click, cla)
                            time.sleep(0.5)
                            skip_start(cla)
                            time.sleep(0.5)
                        for i in range(8):
                            x_click = 440 + (i*55)
                            y_click = 690
                            click_pos_2(x_click, y_click, cla)
                            time.sleep(0.5)
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\close_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(550, 80, 610, 145, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("close_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:

                                skip_start(cla)
                            time.sleep(0.5)
                    else:
                        print("kindkindkindkindkind", kind)
                        if kind != "common":
                            path = checked + str(kind)


                            is_checked = False

                            if kind == "seven":
                                get_checked_list = os.listdir(path)
                                reg_x = 350
                                reg_y = 650

                                for i in range(len(get_checked_list)):
                                    full_path = str(checked) + str(kind) + "\\" +str(get_checked_list[i])
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_for = imgs_set_for(280, 550, 850, 700, cla, img, 0.85)
                                    if imgs_for is not None and imgs_for != False:

                                        if len(imgs_for) > 0:
                                            print("get_ready_list", get_checked_list[i], imgs_for)

                                            for_x = imgs_for[len(imgs_for) - 1][0]
                                            for_y = imgs_for[len(imgs_for) - 1][1]

                                            click_pos_reg(for_x + 70, for_y, cla)
                                            QTest.qWait(1000)

                                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\close_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(550, 80, 610, 145, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("close_1", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                            else:

                                                skip_start(cla)
                                            is_checked = True

                            elif kind == "eight":
                                reg_x = 430
                                reg_y = 460

                                for i in range(8):
                                    x_click = 430
                                    if i > 3:
                                        x_click = 700
                                    y_click = 460 + (i * 70)
                                    if i > 3:
                                        y_click = 460 + ((i - 4) * 70)
                                    click_pos_2(x_click, y_click, cla)
                                    time.sleep(0.5)
                                    skip_start(cla)
                                    time.sleep(0.5)

                            elif kind == "right":
                                reg_x = 430
                                reg_y = 460

                                for i in range(4):
                                    x_click = 700
                                    y_click = 515 + (i * 70)
                                    click_pos_2(x_click, y_click, cla)
                                    time.sleep(0.5)
                                    skip_start(cla)
                                    time.sleep(0.5)

                                drag_pos(700, 720, 700, 500, cla)
                                time.sleep(0.5)
                                drag_pos(700, 720, 700, 500, cla)
                                time.sleep(0.5)

                                for i in range(2):
                                    x_click = 700
                                    y_click = 630 + (i * 70)
                                    click_pos_2(x_click, y_click, cla)
                                    time.sleep(0.5)
                                    skip_start(cla)
                                    time.sleep(0.5)


                            elif kind == "tewnty_one":
                                get_checked_list = os.listdir(path)
                                reg_x = 350
                                reg_y = 500
                                for i in range(len(get_checked_list)):
                                    full_path = str(checked) + str(kind) + "\\" +str(get_checked_list[i])
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_for = imgs_set_for(300, 440, 850, 750, cla, img, 0.85)
                                    if imgs_for is not None and imgs_for != False:

                                        if len(imgs_for) > 0:
                                            print("get_ready_list", get_checked_list[i], imgs_for)

                                            for_x = imgs_for[len(imgs_for) - 1][0]
                                            for_y = imgs_for[len(imgs_for) - 1][1]

                                            if for_x > 750:
                                                if for_y < 540:
                                                    reg_y = 600
                                                elif for_y < 630:
                                                    reg_y = 700
                                                else:
                                                    break
                                            else:
                                                click_pos_reg(for_x + 70, for_y, cla)
                                                QTest.qWait(1000)
                                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\close_1.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(550, 80, 610, 145, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("close_1", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    break
                                                else:

                                                    skip_start(cla)
                                                is_checked = True

                            elif kind == "random":
                                reg_x = 340
                                reg_y = 460

                                is_checked = True

                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\checked\\random\\close_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(550, 80, 620, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("close_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    QTest.qWait(500)

                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\checked\\random\\click_ready.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 560, 680, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("click_ready", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    anymore_notice = False
                                    for i in range(10):
                                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\checked\\random\\anymore_notice.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(370, 80, 560, 140, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("anymore_notice", imgs_)
                                            anymore_notice = True
                                            break
                                        QTest.qWait(100)
                                    if anymore_notice == True:
                                        # 왼쪽 포인트
                                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\e_point\\" + str(
                                            point_kind)
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(e_x_reg - plus - reg, e_y_reg - reg, e_x_reg - plus + reg, e_y_reg + reg,
                                                          cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("get_event_start: get_e_ready_list", str(point_kind), imgs_)
                                            # 420, 455, 540, 720, 825

                                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\checked\\random\\close_btn.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(550, 80, 620, 140, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("close_btn", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                QTest.qWait(500)

                                            click_list = [420, 460, 540, 725, 825]

                                            for i in range(len(click_list)):
                                                click_pos_2(click_list[i], 695, cla)
                                                QTest.qWait(500)
                                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\checked\\random\\close_btn.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(550, 80, 620, 140, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("close_btn", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    QTest.qWait(500)


                                    else:
                                        skip_start(cla)
                                else:
                                    click_pos_2(760, 400, cla)
                                    QTest.qWait(500)
                                    confirm_all(cla)
                            print("is_checked", is_checked)
                            if is_checked == False:
                                click_pos_2(reg_x, reg_y, cla)
                                QTest.qWait(1000)
                                skip_start(cla)


                        else:
                            # common point
                            for i in range(len(get_ready_list)):
                                full_path = str(get_ready) + str(get_ready_list[i])
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("get_ready_list", get_ready_list[i], imgs_)
                                    click_pos_reg(imgs_.x - 15, imgs_.y, cla)
                                    QTest.qWait(1000)
                                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\close_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(550, 80, 610, 145, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("close_1", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:

                                        skip_start(cla)
                else:
                    is_open = True
            else:

                is_title = False

                for i in range(len(get_e_title_list)):
                    full_path = str(get_e_title) + str(get_e_title_list[i])
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 300, 860, 760, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("get_e_title_list", get_e_title_list[i], imgs_)
                        is_title = True
                        break
                if is_title == False:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\close_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(550, 80, 610, 145, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("close_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        skip_start(cla)
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\title\\" + str(data)
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 300, 860, 760, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("get_event_start ready", str(data), imgs_)
                    else:
                        is_open = True
            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_special(cla):
    print("get_event")
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open_pure
    from clean_screen import clean_screen_start


    try:
        print("get_special")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\server.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 320, 340, 360, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("server", imgs_)


                is_point = False
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\e_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 310, 300, 750, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("e_point_1", imgs_)
                    click_pos_reg(imgs_.x - 50, imgs_.y + 20, cla)
                    is_point = True
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\e_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(240, 310, 300, 750, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("e_point_2", imgs_)
                        click_pos_reg(imgs_.x - 50, imgs_.y + 20, cla)
                        is_point = True

                if is_point == True:
                    QTest.qWait(500)
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\special\\all_get_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("all_get_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(1000)
                        skip_start(cla)

                else:
                    is_open = True
                    clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\special.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("special", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)



def get_sangjum_gyohwan(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open_pure
    from clean_screen import clean_screen_start


    try:
        print("get_sangjum_gyohwan")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : sangjum", imgs_)

                for i in range(10):

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 80, 480, 140, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("clicked", imgs_)

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\sohwangwuan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 100, 960, 700, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("sohwangwuan", imgs_)
                            is_open = True
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\gold.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 100, 170, 900, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("gold", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                    else:
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\gyohwan_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 60, 850, 150, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("gyohwan_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(200)

            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\sangjum.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sangjum", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)

def get_sangjum_start(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open_pure
    from clean_screen import clean_screen_start


    try:
        print("get_sangjum_start")



        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : sangjum", imgs_)

                for i in range(10):
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 80, 480, 140, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("clicked", imgs_)

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\sohwangwuan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 100, 960, 700, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("sohwangwuan", imgs_)
                            is_open = True

                            get_sangjum_scan(cla)

                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\gold.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 100, 170, 900, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("gold", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                    else:
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\gyohwan_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 60, 850, 150, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("gyohwan_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(200)
                if is_open == True:
                    clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\sangjum.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sangjum", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_sangjum_scan(cla):
    import numpy as np
    import cv2

    from function_game import drag_pos, imgs_set_

    try:
        print("get_sangjum_start")

        # 사기
        for z in range(2):
            if z == 1:
                drag_pos(830, 300, 300, 300, cla)
            for y in range(2):
                y_reg_1 = 200 + (220 * y)
                y_reg_2 = y_reg_1 + 80
                for i in range(4):

                    if z == 1 and y == 1 and i == 3:
                        break

                    x_reg_1 = 232 + (195 * i) - 40
                    x_reg_2 = x_reg_1 + 140

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\lock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg_1, y_reg_1, x_reg_2, y_reg_2, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print(y + 1, "번째 줄", i + 1, "번째 있다.")
                        print("lock", imgs_)
                    else:
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1, y_reg_1, x_reg_2, y_reg_2, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print(y + 1, "번째 줄", i + 1, "번째 있다.")
                            print("complete", imgs_)
                        else:
                            print(y + 1, "번째 줄", i + 1, "번째 없다.................")
                            get_sangpoom(x_reg_1, y_reg_1, cla)
            QTest.qWait(100)
    except Exception as e:
        print(e)


def get_sangpoom(x_reg, y_reg, cla):
    import numpy as np
    import cv2

    from clean_screen import skip_check, skip_start
    from function_game import imgs_set_, click_pos_2, click_pos_reg, text_check_get_num, change_number
    try:
        print("get_sangpoom", x_reg, y_reg)
        for i in range(7):
            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\clean_screen\\close\\close_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 290, 770, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\max.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(210, 320, 735, 705, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("max", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\sangjum\\money.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(210, 320, 735, 705, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("money", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)

                for x in range(5):
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\clean_screen\\close\\close_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 290, 770, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)
                        break
                    else:
                        result_skip = skip_check(cla)
                        if result_skip == True:
                            skip_start(cla)
                    QTest.qWait(200)
                break
            else:
                click_pos_2(x_reg, y_reg, cla)
            QTest.qWait(500)
    except Exception as e:
        print(e)



def get_inmool(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start, skip_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open_pure
    from clean_screen import clean_screen_start


    try:
        print("get_inmool")



        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\inmool.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : inmool", imgs_)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\inmool\\point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 150, 300, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                    QTest.qWait(500)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\inmool\\click_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 900, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("click_ready", imgs_)
                    click_pos_reg(imgs_.x + 20, imgs_.y, cla)
                    QTest.qWait(500)
                result_skip = skip_check(cla)
                if result_skip == True:
                    skip_start(cla)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\inmool\\point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(150, 300, 960, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("point_2", imgs_)
                    click_pos_reg(imgs_.x - 30, imgs_.y - 30, cla)
                    QTest.qWait(500)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\inmool\\inmool_infomation.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 340, 540, 400, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("inmool_infomation", imgs_)
                    click_pos_2(745, 675, cla)
                    QTest.qWait(500)

                result_skip = skip_check(cla)
                if result_skip == True:
                    skip_start(cla)

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\inmool\\point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 150, 300, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("point_1", imgs_)



                else:
                    is_open = True

                if is_open == True:
                    clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\inmool.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("inmool", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_chosanghwa(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start, skip_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open_pure
    from clean_screen import clean_screen_start

    try:
        print("get_chosanghwa")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 7:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\chosanghwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : chosanghwa", imgs_)

                is_point = False

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\chosanghwa\\point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 100, 900, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    is_point = True
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    QTest.qWait(500)
                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\chosanghwa\\point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 60, 100, 900, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        is_point = True
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        QTest.qWait(500)
                if is_point == True:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\chosanghwa\\point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 60, 280, 400, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                        QTest.qWait(500)

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\chosanghwa\\bogwon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 900, 960, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("bogwon", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\chosanghwa\\get.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 900, 960, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("get", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)


                    result_skip = skip_check(cla)
                    if result_skip == True:
                        skip_start(cla)



                else:
                    is_open = True

                if is_open == True:
                    clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\chosanghwa.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("chosanghwa", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)




def get_acave(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start, skip_check
    from function_game import imgs_set_reg, click_pos_reg, imgs_set_, click_pos_2
    from action import menu_open_pure
    from clean_screen import clean_screen_start

    try:
        print("get_acave")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 12:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\acave.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : acave", imgs_)

                is_point = False

                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\bottom_point__1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(180, 790, 800, 900, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("bottom_point__1", imgs_)
                    is_point = True
                    click_pos_reg(imgs_.x - 15, imgs_.y - 30, cla)
                    QTest.qWait(500)

                if is_point == True:

                    for i in range(5):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\yundagi.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 150, 150, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("yundagi", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\hero.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 30, 150, 150, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("hero", imgs_)
                                break
                        QTest.qWait(300)


                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\left_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 100, 160, 990, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                        QTest.qWait(500)

                        for i in range(5):
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\get_click_ready_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 100, 550, 990, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                QTest.qWait(500)
                                click_pos_2(850, 1010, cla)
                                QTest.qWait(500)
                                click_pos_2(850, 1010, cla)
                                QTest.qWait(500)
                                click_pos_2(850, 1010, cla)
                                QTest.qWait(500)
                            else:
                                break
                            QTest.qWait(500)
                        for i in range(5):
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\complete_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(770, 980, 930, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                result_skip = skip_check(cla)
                                if result_skip == True:
                                    skip_start(cla)
                                    break
                                else:
                                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\get_click_ready_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(470, 100, 550, 990, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                        QTest.qWait(500)
                                        click_pos_2(850, 1010, cla)
                            QTest.qWait(500)
                    else:

                        click_pos_2(105, 1010, cla)


                        for i in range(5):
                            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\yundagi.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 30, 150, 150, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("yundagi", imgs_)
                                break
                            else:
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\hero.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 30, 150, 150, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("hero", imgs_)
                                    break
                            QTest.qWait(300)

                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\left_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(100, 100, 160, 990, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                            QTest.qWait(500)

                            for i in range(5):
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\get_click_ready_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 100, 550, 990, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                    QTest.qWait(500)
                                    click_pos_2(850, 1010, cla)
                                    QTest.qWait(500)
                                    click_pos_2(850, 1010, cla)
                                    QTest.qWait(500)
                                    click_pos_2(850, 1010, cla)
                                    QTest.qWait(500)
                                else:
                                    break
                                QTest.qWait(500)

                            for i in range(5):
                                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\complete_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(770, 980, 930, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    result_skip = skip_check(cla)
                                    if result_skip == True:
                                        skip_start(cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\acave\\get_click_ready_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 100, 550, 990, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                                            QTest.qWait(500)
                                            click_pos_2(850, 1010, cla)
                                QTest.qWait(500)
                        else:
                            is_open = True
                    result_skip = skip_check(cla)
                    if result_skip == True:
                        skip_start(cla)



                else:
                    is_open = True

                if is_open == True:
                    clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\acave.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("acave", imgs_)

                    x_reg = imgs_.x
                    y_reg = imgs_.y

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_reg(x_reg, y_reg - 50, x_reg + 30, y_reg, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point_1", imgs_)

                        click_pos_reg(x_reg, y_reg, cla)

                        QTest.qWait(500)
                    else:
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_reg(x_reg, y_reg - 50, x_reg + 30, y_reg, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point_2", imgs_)
                            click_pos_reg(x_reg, y_reg, cla)

                            QTest.qWait(500)
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_malyuc(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start, skip_check
    from function_game import click_pos_reg, imgs_set_, click_pos_2, imgs_set_reg
    from action import menu_open_pure
    from clean_screen import clean_screen_start

    try:
        print("get_malyuc")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 12:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\malyuc.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : malyuc", imgs_)


                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\malyuc\\point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(70, 60, 500, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("point_1", imgs_)
                    x_point = imgs_.x
                    y_point = imgs_.y
                    click_pos_reg(x_point - 15, y_point + 15, cla)
                    QTest.qWait(500)


                    for i in range(20):
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\malyuc\\point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_point - 20, y_point - 20, x_point + 20, y_point + 20, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(830, 1010, cla)
                            QTest.qWait(700)
                        else:
                            break
                else:
                    is_open = True
            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\malyuc.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("malyuc", imgs_)

                    x_reg = imgs_.x
                    y_reg = imgs_.y

                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_reg(x_reg, y_reg - 50, x_reg + 30, y_reg, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("point_1", imgs_)

                        click_pos_reg(x_reg, y_reg, cla)

                        QTest.qWait(500)
                    else:
                        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_reg(x_reg, y_reg - 50, x_reg + 30, y_reg, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("point_2", imgs_)
                            click_pos_reg(x_reg, y_reg, cla)

                            QTest.qWait(500)
                        else:
                            is_open = True
                else:
                    menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_guild(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start, skip_check
    from function_game import click_pos_reg, imgs_set_, click_pos_2, imgs_set_reg
    from action import menu_open_pure
    from clean_screen import clean_screen_start

    try:
        print("get_guild")

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count > 12:
                is_open = True

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\guild\\donation_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("donation_title", imgs_)

                for i in range(5):
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\guild\\anymore_donation.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 80, 600, 140, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        is_open = True
                        break
                    else:
                        click_pos_2(250, 640, cla)
                    QTest.qWait(100)

            else:
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\title\\guild.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 30, 960, 150, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("title : guild", imgs_)


                    click_pos_2(810, 1010, cla)



                else:
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("guild", imgs_)

                        x_reg = imgs_.x
                        y_reg = imgs_.y
                        click_pos_reg(x_reg, y_reg, cla)
                    else:
                        menu_open_pure(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_event_sub(cla):
    print("get_event_sub")