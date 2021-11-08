import matplotlib.pyplot as plt
import numpy
from matplotlib.colors import LinearSegmentedColormap
from seaborn import heatmap as hmap

from Config.colorbar import *

colors = [(0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0), (1, 0, 0)]
colormap = LinearSegmentedColormap.from_list('cmap_name', colors, N=1000)

# 繪製熱圖
def heatmap(path: str, map2d: numpy.ndarray, show: bool = True) -> None:
    """
    Save heatmap from map2d
    :param path: save path
    :param map2d: metadata of heatmap
    :param show: show or not show heatmap
    :return: None
    """
    sizeX, sizeY = map2d.shape
    plt.figure(figsize=(sizeX, sizeY), dpi=100)
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
    ax.invert_yaxis()  # y方向反向

    # plt.savefig(path + 'heatmap.png')
    if show:
        plt.show(block=False)
        plt.pause(0.5)
        plt.close("all")
