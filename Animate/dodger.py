import matplotlib.pyplot as plt, matplotlib.animation as ani
import sys, numpy as np, scipy.ndimage as ndi


def render(slides, isColor, fps, isSaved):
    f = plt.figure()
    reel = []
    for frame in slides:
        if isColor:
            reel.append([plt.imshow(frame)])
        else:
            reel.append([plt.imshow(frame, 'gray_r')])
    a = ani.ArtistAnimation(f, reel, interval=fps, blit=True, repeat_delay=500)
    plt.show()


def initialize_board(settings):
    if '-user' in settings:
        # Set spatial fields and fill blank canvas
        width = int(input('Enter width: '))
        height = int(input('Enter height: '))
        walls = int(input('Enter size of walls: '))
        blank = np.zeros((width, height))
        # Create boundaries
        blank[0:walls, :] = 1
        blank[:, 0:walls] = 1
        blank[:, height - walls:height] = 1
        blank[width - walls:width, :] = 1
        # Show it
        plt.imshow(blank, 'gray_r')
        plt.show()
        return blank
    else:
        blank = np.zeros((100, 100))
        blank[0:5, :] = 1
        blank[:, 0:5] = 1
        blank[:, 95:100] = 1
        blank[95:100, :] = 1
        # Add obstacles!
        board = add_enemies(3, blank)
        # Show it
        plt.imshow(board, 'gray_r')
        plt.show()
        return board


def add_enemies(N,board):
    for x in range(N):
        rxs = np.random.randint(0, board.shape[0], 1)
        rys = np.random.randint(0, board.shape[1], 1)

        board[rxs,rys] = 1
    return board



def main():
    config = initialize_board(sys.argv)


if __name__ == '__main__':
    main()


