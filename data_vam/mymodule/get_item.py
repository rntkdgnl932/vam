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

        get_post(cla)
        get_upjuk(cla)


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
    print("get_event")
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


def get_event_sub(cla):
    print("get_event_sub")