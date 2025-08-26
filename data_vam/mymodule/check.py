import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def out_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("out_check")

        is_out = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\out\\talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 800, 100, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("talk", imgs_)

            is_out = True

        return is_out

    except Exception as e:
        print(e)





def loading_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("loading_check")

        is_loding = False

        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\loading\\loding_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 680, 300, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("loding_1", imgs_)
            is_loding = True

        return is_loding

    except Exception as e:
        print(e)


def loading_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("loading_check 30 680 300 900")

        is_loding = False
        is_loding_count = 0

        while is_loding is False:
            is_loding_count += 1
            if is_loding_count > 10:
                is_loding = True

            is_load = False

            full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\loading\\loding_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 680, 300, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("loding_1", imgs_)
                is_load = True

            if is_load == True:
                QTest.qWait(1000)
            else:
                is_loding = True
            QTest.qWait(1000)



    except Exception as e:
        print(e)



def jangsigan_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open
    from massenger import line_to_me

    try:
        print("jangsigan_check")


        full_path = "c:\\my_games\\vam\\data_vam\\imgs\\check\\longtime\\jangsigan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 400, 600, 640, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan", imgs_)
            line_to_me(cla, "장시간 미접속")

    except Exception as e:
        print(e)