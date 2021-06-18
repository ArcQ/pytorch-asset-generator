import math
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import (line, polygon, disk,
                          circle_perimeter,
                          ellipse, ellipse_perimeter,
                          bezier_curve, circle)


class Drawer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        fig, (ax) = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
        self.ax = ax

    @staticmethod
    def __blend(cur_img, rrcc, new_rgb, opacity):
        img = cur_img.copy()
        rr, cc = rrcc

        def get_blended(orig_v, new_v, __opacity):
            return (orig_v * (1 - __opacity)) + (new_v * __opacity / 255)

        for i in range(3):
            img[rr, cc, i] = get_blended(img[rr, cc, i], new_rgb[i], opacity)
        return img

    def init_img(self):
        img = np.zeros((self.x, self.y, 3), dtype=np.double)
        img.fill(1)
        return img

    def draw_ellipse(self, img, ellipse_args, color, opacity):
        rrcc = ellipse(r=ellipse_args[0], c=ellipse_args[1], r_radius=ellipse_args[2], c_radius=ellipse_args[3],
                       shape=img.shape, rotation=ellipse_args[4])
        return self.__blend(img, rrcc, color, opacity)

    def draw_polygon(self, img, rrcc_tup, color, opacity):
        rrcc_arr = np.array(rrcc_tup)
        rrcc = polygon(rrcc_arr[:, 0], rrcc_arr[:, 1], img.shape)
        return self.__blend(img, rrcc, color, opacity)

    def show(self, img):
        self.ax.imshow(img)
        plt.show()
