import sys, time, numpy as np, scipy.ndimage as ndi
import matplotlib.pyplot as plt, matplotlib.animation as animation


def render(matrices, isColor, speed):
    reel = []
    f = plt.figure()
    for frames in matrices:
        if isColor:
            reel.append([plt.imshow(frames)])
        else:
            reel.append([plt.imshow(frames, 'gray_r')])
    a = animation.ArtistAnimation(f, reel, interval=speed, blit=True, repeat_delay=500)
    plt.show()


def burn(initial_state, ngen, filta):
    gen = 0
    generations = []
    while gen < ngen:
        generations.append(initial_state)
        world = ndi.convolve(initial_state, filta)
        initial_state = fractal_flames(initial_state.flatten(), world).reshape(initial_state.shape)
        gen += 1
    return generations


def fractal_flames(nextstate, world):
    ii = 0

    for cell in world.flatten():
        if 6 == cell or cell == 8 or cell == 17:
            nextstate[ii] += 1
        if cell == 9 or cell == 3 or cell == 12:
            nextstate[ii] = 1
        if cell == 3 or cell == 5 or cell == 7:
            nextstate[ii] = 0
        ii += 1
    return nextstate


def build_log(dims):
    width = dims[0]
    height = dims[1]
    canvas = np.zeros((width, height)).flatten()
    nblocks = int(height / 4) * width
    for pixel in range(nblocks):
        if pixel%2==0:
            canvas[pixel] = 1
    return np.rot90(np.rot90(canvas.reshape((width, height))))

def main():
    spark = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    nFrames = 220
    if len(sys.argv) < 2:
        gas = build_log([100, 100])

        s0 = time.time()
        flames = burn(gas, nFrames, spark)
        print str(nFrames) + " Frame Simulation finished [" + str(time.time() - s0) + "s]"
        render(flames, False, 70)
    else:
        nFrames = 255
        if '-block' in sys.argv:
            gas = np.zeros((200,200))
            gas[100:110,100:110] = 1
            s0 = time.time()
            flames = burn(gas, nFrames, spark)
            print str(nFrames) + " Frame Simulation finished [" + str(time.time() - s0) + "s]"
            render(flames, False, 35)



if __name__ == '__main__':
    main()
