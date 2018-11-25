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
![Example](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Images/CellularAutomata.png)

On the left is the bit plane universe of Conway's game, while
the right shows the 'neighborhood', or weight of cell/pixel when
convolved with a 3x3 matrix of ones. 

Watch this to see the Game of Life, and more complex automata, in [action](https://youtu.be/8Bcwa-s-jtM) 

# More Complex Automata
You can do much more with automata than may at first seem apparent. 
One of the hidden powers automata inherently have is the ability to
apply a pattern of some sort to any bit plane globally. 

A great example of this is the bacteria.py program in the Automata/ folder. 
Run `python bacteria.py` and you will see all kinds of weird viral like structures.
One of which is this interesting network of blobs, initially seeded with random 1s and
0s. 

![BLOBBY](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Images/bacterial1.png)

On the other hand, giving a well defined initial state can also be interesting, as rules that 
are carefully designed can evolve into very interesting systems. 

## FractalFire.py
Take for example the `fractal_fire.py` design. It seeds the automata world initially with a window
that is 3/4 white with the remainder being a black bar at the bottom (like a log in the fire place). 
By applying a neighbordhood much like the Game of Life, only changing the rules, you can get a system
that spreads a somewhat unique and interesting pattern across the screen like flames. 

[Fractal_Fire](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Videos/fractalFire.mp4) 

## InkBlots.py
Perhaps even more interesting, or at least surprising, is the ability of automata to take the random noise
and reliably produce a similar kind of pattern. In the `simple.py` Automata, a random field of 0s and 1s is
given, but *will always* produce a similar kind of pattern where the random dots cluster together and form blobs
which continue to grow. In this simulation, I did two layers of this same technique, so the result is something that
not only clusters the blobs in space, but also clusters them by time. This allows the blobs that have managed to stay
together to grow faster than weaker blobs. The result is a swelling effect of already randomly clustered blobs. 
 
[Ink_Blots](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Videos/InkBlots.mp4)

# Automata Image Processing 
While it is fun to play in the theoretical space of bit planes, and simulate processes with mappings of
black and white squares, you can also yield pretty amazing results when you feed a well crafter Automata
actually images, or **vast** bitplanes of enormous dynamic range in the cellular automata world. 

First we have to consider whether or not to feed in a color image, or a black and white image, or a preprocessed image 
that is color or even black and white. Luckily, it is very easy to swap and modify image color schemes in python!
![ImageSubtraction](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Images/ColorSubtract.png)  

Because you can essentially have edge detection in a single iteration with the correct cellular automata rules and 
neighborhood definition, by maintaining state variables, or in the case of `aip.py` (Automata Image Processing) using
color itself as the state variable, attributes can be traced and manipulated with pretty simple code that can produce 
quite dramatic outputs.

Here are two examples:

![Planet](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Images/bubbs.png)
 
 
Video: 
[Bubbles](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Videos/AutomataImageProcessing.mp4)

Touched up Even more, I give you: [Bubbles!](https://raw.githubusercontent.com/TylersDurden/Sudo_Science/master/Videos/bubbles2.mp4)