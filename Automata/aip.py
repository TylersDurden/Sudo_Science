import sys, time, resource, numpy as np, scipy.ndimage as ndi
import matplotlib.pyplot as plt, matplotlib.animation as ani


def render(matrices, speedOfLife):
    f = plt.figure()
    reel = []
    for matrix in matrices:
        frame = plt.imshow(matrix,'gray_r')
        reel.append([frame])
    a = ani.ArtistAnimation(f, reel, interval=speedOfLife,blit=True,repeat_delay=1000)
    plt.show()


def check_mem_usage():
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return mem


def pre_screen(imat, isVerbose):
    dims = imat.shape
    avg1 = imat[:,:,0].mean()
    avg2 = imat[:,:,1].mean()
    avg3 = imat[:,:,2].mean()

    sizes = {'small': False, 'medium': False, 'large': False}
    if 200 < np.array(dims).max() < 500:
        sizes['medium'] = True
    if 200 > np.array(dims).max():
        sizes['small'] = True
    if 500 < np.array(dims).max():
        sizes['large'] = True

    if isVerbose:
        print "Dims: " + str(dims)
        print "Avg Pixel Values:\n" + "CH1: "+str(avg1)+" CH2: "+str(avg2)+" CH3: "+str(avg3)
        f, ax = plt.subplots(1, 3, sharey=True, figsize=(10, 5))
        ax[0].imshow(imat[:, :, 0])
        ax[0].set_title('Color Ch.1')
        ax[1].imshow(imat[:, :, 1])
        ax[1].set_title('Color Ch.1')
        ax[2].set_title('Color Ch.3 > Grayscale')
        ax[2].imshow(imat[:, :, 2],'gray_r')
        plt.show()
        for size in sizes.keys():
            if sizes[size]:
                print "* (Image is " + size + ' sized)'
    return dims, [avg1, avg2, avg3], sizes


def edgy(image, iavg, filter, ncycles):
    cycle = 0
    generations = []
    while cycle < ncycles:
        nextstate = np.array(image).copy()
        world = ndi.convolve(nextstate, filter, origin=0).flatten()
        ''' Modify image into next state '''
        image = edge(nextstate.flatten(), world,iavg).reshape(image.shape)
        # generations.append(world.reshape(image.shape))
        generations.append(image)
        cycle += 1
    return generations


def edge(state, world, avg):
    ii = 0
    for cell in world:
        if cell <= 6 and state[ii]>200:
            state[ii] = 10
        if cell > 6:
            state[ii] -= 10
        ii += 1
    return state


def main():
    verbose = False
    # Possible Test Images
    bubbs = '../Images/bubbles.jpeg'
    earth = '../Images/earth.jpg'

    # Intial Memory
    meminit = check_mem_usage()

    if '-v' in sys.argv:
        print "Initial Memory Overhead is: "+str(float(meminit*10/10000))+'Kb'
        verbose = True

    # Read in a Test Image
    test_image = plt.imread(earth)
    test_image2 = plt.imread(bubbs)
    dims, avgs, itype = pre_screen(test_image2, verbose)
    postload = check_mem_usage()

    if verbose:
        print "* ("+str(float((postload - meminit)*10/10000)) + "kb of additional RAM used)"

    box1 = np.array([[1,1,1],
                     [1,1,1],
                     [1,1,1]])
    box2 = np.array([[3,3,3,3,3],
                     [3,2,2,2,3],
                     [3,2,1,2,3],
                     [3,2,2,2,3],
                     [3,3,3,3,3]])


    test_avg = np.array(test_image2[:,:,0]).mean()
    test = test_image2[:, :, 0]
    t0 = time.time()
    reel = edgy(test,test_avg,box1,50)
    t1 = time.time()
    reel2 = edgy(test_image[:,:,0],test_image[:,:,2].mean(), box1, 50)
    t2 = time.time()
    print "Bubbles Simulation Finished in " + str(t1-t0)+"s"
    print "Earth Simulation Finished in " + str(t2-t1)+"s"
    print "*** Beginning Rendering"
    render(reel,100)
    t3 = time.time()
    render(reel2,100)
    t4 = time.time()

if __name__ == '__main__':
    main()