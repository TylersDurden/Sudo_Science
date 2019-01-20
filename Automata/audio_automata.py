import matplotlib.pyplot as plt, matplotlib.animation as animation
import time, numpy as np, scipy.ndimage as ndi


def render(matrices, isColor, speed):
    """
    Render the frames provided at the given playback
    speed. Capable of supporting color or black and
    white frames.
    :param matrices:
    :param isColor:
    :param speed:
    :return:
    """
    reel = []
    f = plt.figure()
    for frames in matrices:
        if isColor:
            reel.append([plt.imshow(frames)])
        else:
            reel.append([plt.imshow(frames, 'gray_r')])
    a = animation.ArtistAnimation(f, reel, interval=speed, blit=True, repeat_delay=500)
    plt.show()


def special_render(seed,matrices, isColor, speed):
    """
    Special_Render with render the frames proviced,
    while showing the original image on the side in
    a second subplot window.
    :param seed:
    :param matrices:
    :param isColor:
    :param speed:
    :return:
    """
    reel = []
    f, (ax0, ax1) = plt.subplots(1,2)
    for frame in matrices:
        if isColor:
            reel.append([ax0.imshow(seed)])
            reel.append([ax1.imshow(frame)])
        else:
            reel.append([ax0.imshow(seed,'gray_r')])
            reel.append([ax1.imshow(frame,'gray_r')])
    a = animation.ArtistAnimation(f, reel,interval=speed,blit=True,repeat_delay=500)
    plt.show()


