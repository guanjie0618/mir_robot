#!/usr/bin/env python3

import rospy
import tf

from time import sleep
from drawnow import drawnow
from matplotlib import pyplot as plt

from Config.colorbar import *
from Node import DataSaver, Painter
from Node.Painter import colormap
from Sensors.simulation.lib import device
from Utils import timeit, root_path
from Utils.Alert import PLAY_mission_completed
from Utils.Map2d import signal_map
from Utils.Statistical import min_error as function

import matplotlib.pyplot as plt
import numpy
from matplotlib.colors import LinearSegmentedColormap
from seaborn import heatmap as hmap

colors = [(0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0), (1, 0, 0)]
colormap = LinearSegmentedColormap.from_list('cmap_name', colors, N=1000)

# list of data
x, y, data = [], [], []

if __name__ == '__main__':
    # initialize node
    rospy.init_node('tf_listener')
    # print in console that the node is running
    rospy.loginfo('started listener node !')
    # create tf listener
    listener = tf.TransformListener()
    # set the node to run 1 time per second (1 hz)
    rate = rospy.Rate(1.0)

    plt.ion()
    plt.figure(figsize=(5, 5), dpi=100)

    # 計算測量時間、初始化儀控
    with timeit(), device() as sensor:  # init sensor

        # loop forever until roscore or this node is down
        while not rospy.is_shutdown():
            try:
                # listen to transform
                (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
                # print the transform
                rospy.loginfo('---------')
                rospy.loginfo('Translation: ' + str(trans))
                rospy.loginfo('Rotation: ' + str(rot))
                power = sensor.read_power()
                bot_y, bot_x = trans[1], trans[0]
                y.append(bot_y)
                x.append(bot_x)
                data.append(power)
                print(f'({x[-1]:.3f}, {y[-1]:.3f}): {data[-1]:.3f}')

                # 建立熱圖用2d陣列
                map2d = signal_map.map2darray(y, x, data, 0.3, error_function=function) # robot_width_value = 0.3
                # 建立儲存資料夾
                path = root_path()

                # 繪製熱圖
                # Painter.heatmap(path, map2d)
                plt.clf()

                sizeX, sizeY = map2d.shape
                font_size = max(sizeX, sizeY) + 10
                ax = hmap(map2d,
                        annot=False, annot_kws={"fontsize": 15},  # 格子中的字
                        cmap=colormap, vmin=vmin, vmax=vmax,  # colorbar 設定
                        square=True,
                        cbar_kws={
                            'label': 'Power'
                        })
                ax.figure.axes[-1].yaxis.label.set_size(font_size)
                colorBar = ax.collections[0].colorbar
                colorBar.ax.tick_params(labelsize=font_size)
                ax.invert_yaxis()

                # plt.show(block=False)
                plt.pause(0.1)
                # plt.close("all")

                # 儲存檔案
                # DataSaver.map(path, map2d)  # 2d陣列
                # DataSaver.map_original_data(path, y, x, data)  # 原始x, y, data資料

            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue
            # sleep to control the node frequency
            rate.sleep()

        plt.ioff()