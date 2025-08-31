import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def get_start(cla):
    from boonhae_collection import boonhae_collection_start
    from klan import klan_donation
    try:
        print("get_start")

        get_post(cla)
        get_upjuk(cla)
        get_event(cla)
        get_special(cla)
        get_sangjum_start(cla)
        get_inmool(cla)
        get_chosanghwa(cla)
        get_acave(cla)

        klan_donation(cla)
        boonhae_collection_start(cla)

    except Exception as e:
        print(e)

def get_post(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
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
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_upjuk(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
    from clean_screen import clean_screen_start

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

                is_open = True

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
                full_path = "c:\\my_games\\vam\\data_vam\\imgs\\menu\\upjuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("upjuk", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)

def get_event(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
    from clean_screen import clean_screen_start



    get_ready = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\event\\get_ready\\"
    get_ready_list = os.listdir(get_ready)



    try:
        print("get_event")

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

                    for i in range(len(get_ready_list)):
                        full_path = str(get_ready) + str(get_ready_list[i])
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("get_ready_list", get_ready_list[i], imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y, cla)
                            QTest.qWait(1000)
                            skip_start(cla)

                else:
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
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)




def get_special(cla):
    print("get_event")
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
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
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)



def get_sangjum_gyohwan(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
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
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\clicked.PNG"
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
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)

def get_sangjum_start(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
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
                    full_path = "c:\\my_games\\vam\\data_vam\\imgs\\get_item\\clicked.PNG"
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
                    menu_open(cla)

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
    from action import menu_open
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
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)


def get_chosanghwa(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start, skip_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_
    from action import menu_open
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
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)




def get_acave(cla):
    import numpy as np
    import cv2

    from clean_screen import skip_start, skip_check
    from function_game import imgs_set_reg, click_pos_reg, imgs_set_, click_pos_2
    from action import menu_open
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
                    click_pos_reg(imgs_.x - 15, imgs_.y - 300, cla)
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
                    menu_open(cla)

            QTest.qWait(500)
    except Exception as e:
        print(e)

def get_event_sub(cla):
    print("get_event_sub")