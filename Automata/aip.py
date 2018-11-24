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
        ax[1].imshow(imat[:, :, 2])
        ax[1].set_title('Color Ch.3')
        ax[2].set_title('Subtracting Ch.3 from Ch.1 > Grayscale')
        ax[2].imshow(imat[:, :, 2]-imat[:,:,0]/3,'gray_r')
        plt.show()
        for size in sizes.keys():
            if sizes[size]:
                print "(Image is " + size + ' sized)'
    return dims, [avg1, avg2, avg3], sizes


def main():

    # Possible Test Images
    bubbs = '../Images/bubbles.jpeg'
    earth = '../Images/earth.jpg'

    verbose = False
    if '-v' in sys.argv:
        print "Initial Memory Overhead is: "+str(float(check_mem_usage()*10/10000))+'Kb'
        verbose = True

    # Read in a Test Image
    test_image = plt.imread(earth)
    dims, avgs, itype = pre_screen(test_image, verbose)

    



if __name__ == '__main__':
    main()