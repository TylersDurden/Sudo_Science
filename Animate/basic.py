import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as ani
import scipy.ndimage as ndi, scipy.cluster as cls


class Util:

    def __init__(self, difficulty, shape):
        self.maze = Util.create_maze(difficulty, [shape[0], shape[1]])
        self.search_space = Util.select_random_endpoints(self.maze)

    @staticmethod
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

    @staticmethod
    def add_block(x1, y1, width, height, canvas):
        if len(canvas.shape) == 2:
            x2 = x1 + width
            y2 = y1 + height
            canvas[x1:x2, y1:y2] = 10
        return canvas

    @staticmethod
    def create_maze(difficulty, size):
        maze = np.zeros((size[0], size[1]), dtype=int)
        dims = maze.shape
        for mine in range(difficulty):
            rx = np.random.randint(0, 1 + dims[0], 1)
            ry = np.random.randint(0, 1 + dims[1], 1)
            maze = Util.add_block(int(rx), int(ry), 6, 6, maze)
        plt.imshow(maze, 'gray_r')
        plt.title('Maze [Difficulty=' + str(difficulty) + ']')
        plt.show()
        return maze

    @staticmethod
    def select_random_endpoints(maze):
        valid_points = maze < 1
        legal = []
        II = 0
        nValid = 0
        for point in valid_points.flatten():
            if point:
                nValid += 1
                legal.append(II)
            II += 1
        nTotal = maze.shape[0] * maze.shape[1]
        print "** Maze is " + str(float(nValid * 100) / float(nTotal)) + "% Free of Mines ** "

        maze[0:5, 0:5] = -20
        maze[maze.shape[0] - 5:maze.shape[0], maze.shape[1] - 5:maze.shape[1]] = -20

        plt.imshow(maze, 'gray_r')
        plt.show()

        return maze

    @staticmethod
    def flatmap(matrix):
        ind2sub = {}
        ii = 0
        for y in range(matrix.shape[1]):
            for x in range(matrix.shape[0]):
                pt = [x,y]
                ind2sub[ii] = pt
                ii += 1
        return ind2sub


class searchAgent:
    start = [0,0]
    stop = [0,0]
    pos = []
    world = [[]]
    view = [[]]
    journey = []

    def __init__(self,Maze,SearchSpace):
        # Know that the starting point is the top left corner and
        # the end point is at bottom right corner. So to help get
        # out of initial well give this knowledge to agent (of endpoints)
        self.maze = Maze
        self.set_endpoints(SearchSpace)

        # Set the start and stop points for the search agent
        print "STARTING AT: " + str(Util.flatmap(self.maze)[self.start])
        print "STOPPING AT: " + str(Util.flatmap(self.maze)[self.stop])
        self.pos = Util.flatmap(self.maze)[self.start]
        self.start = self.pos
        self.stop = Util.flatmap(self.maze)[self.stop]

    def set_endpoints(self, maze):
        ii = 0
        for point in maze.flatten():
            if point < 0 and ii <=25:
                self.start = ii
            if point < 0 and ii>25:
                self.stop = ii
            ii += 1

    def search(self):
        search = []
        running = True
        self.world = ndi.convolve(self.maze, self.view, origin=0)
        while running or len(self.journey)>100:
            if self.pos == self.stop:
                running = False
            else:
                self.pos = self.update()
                search.append(self.maze)

        Util.render(search,False,40,False)

    def update(self):
        nextpos = []
        best = []
        ii = 0
        mapping = Util.flatmap(self.maze)
        for point in self.maze.flatten():
            [x, y] = mapping[ii]
            dx = self.pos[0] - x
            dy = self.pos[1] - y

            tx = self.stop[0] - self.pos[0]
            ty = self.stop[1] - self.pos[1]

            if point and dx==1 or dy==1 and (dx-tx) < tx or (dy-ty) < ty:
                best = mapping[ii]

            elif point and dx==1 or dy==1 and x != self.pos[0] or y!= self.pos[1]:
                best = mapping[ii]

            ii += 1

        nextpos = best
        self.journey.append(nextpos)
        self.maze[nextpos] = 0
        return nextpos

    def decision(self):
        maxcount = np.sum(self.view)


def main():

    Maze = Util(15,[100,100])
    search_space = Maze.search_space

    first_order_moves = [[1,1,1],
                         [1,1,1],
                         [1,1,1]]

    second_order_moves = [[2,2,2,2,2],
                          [2,1,1,1,2],
                          [2,1,0,1,2],
                          [2,1,1,1,2],
                          [2,2,2,2,2]]

    '''  PREVIEW  '''
    f, ax = plt.subplots(1,2,figsize=(10,5),sharey=True)
    ax[0].imshow(ndi.convolve(search_space,first_order_moves),'rainbow')
    ax[1].imshow(ndi.convolve(search_space,second_order_moves),'rainbow')
    plt.show()

    ''' SOLVE '''
    agent = searchAgent(Maze.maze, search_space)
    agent.view = first_order_moves

    print "The Journey: "
    print str(agent.start) + "->" + str(agent.stop)
    agent.search()
    print agent.journey


if __name__ == '__main__':
    main()
