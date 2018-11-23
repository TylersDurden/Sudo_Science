# *CELLULAR_AUTOMATA* 
The definition of an Automata is something **self-operating**. 
In the case of Cellular Automata, the self operation is one on
a flat space of numbers (bit plane). 

By defining a 'neighborhood' around each pixel (of various sizes! 
and configurations), and specifying rules about the results of 
doing some matrix multiplication of the 'neighborhood' rules on 
the original bit-plane space, ***an unlimited variety of possible 
behavior can be engineered.*** 

## Conway's Game of Life 
Probably the most popular incarnation of a cellular automata, the
Conway Game of Life simulation is a great example to start with to
understand the fundamentals of the cellular automata. 

The rules are simple: 

* If the cell is ALIVE [1], and has less than 2 neighbors, ***it dies*** 
* If the cell is ALIVE [1], and has less than 4 neighbors, ***it survives***
* If the cell is ALIVE [1], and has more than 3 neighbors, ***it dies***
* If the cell is DEAD [0], and has exactly 3 neighbors, ***it regenerates***

Points of clarifications: 
* A living cell is a pixel == 1.
* A dead cell is a pixel == 0.
* A cell dies if it changes from 1 to 0. 
* A cell regenerates if it changes from 0 to 1. 
* A cell that survives maintains it's state. 

#### Want to un a Conway of life simulation for yourself?
Grab the GOL.py source above and run:
 
 `python GOL.py`
 
  To get a pretty simple automata, select a 
  width and height of 100 pixels. 
  
  Choose a time step of 100 for slowest playback,
  or enter 50 for regular speed. 
  
## Some more detail on how this simulation works:
![Example](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Automata/CellularAutomata.png)

On the left is the bit plane universe of Conway's game, while
the right shows the 'neighborhood', or weight of cell/pixel when
convolved with a 3x3 matrix of ones. 

Watch this to see the Game of Life, and more complex automata, in [action](https://youtu.be/8Bcwa-s-jtM) 

