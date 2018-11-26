import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as ani
import scipy.ndimage as ndi, scipy.cluster as cls


def render(slides, isColor, fps, isSaved):
    f = plt.figure()
    reel = []
    for frame in slides:
        if isColor:
            reel.append([plt.imshow(frame)])
        else:
            reel.append([plt.imshow(frame, 'gray_r')])
    a = ani.ArtistAnimation(f,reel,interval=fps,blit=True,repeat_delay=500)
    plt.show()


def add_block(x1,y1,width,height,canvas):
    if len(canvas.shape) == 2:
        canvas[x1:(x1 + width), y1:(y1 + height)] = 1
    return canvas


slate = np.zeros((30, 30))
example = add_block(10,10,10,10,slate)


test = [[1,1,1],
        [1,1,1],
        [1,1,1]]

plt.imshow(ndi.convolve(example, test,origin=0), 'gray_r')
plt.show()
