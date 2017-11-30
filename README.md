# movie-theater-seating
Written by [Colby Thomas](http://www.coloradocolby.com)
## The Problem
Implement an algorithm for assigning seats within a movie theater to fulfill reservation requests.

Assume the movie theater has the seating arrangement of 10 rows x 20 seats, as illustrated to the right.

Design and write a seat assignment program to maximize both **customer satisfaction** and **theater utilization**.

## Installation
This project requires the [Python v3.6.0](https://www.python.org/downloads/release/python-360/)

To clone this repository directly, execute the following command from the terminal

`git clone https://github.com/coloradocolby/MovieTheaterSeating`

## Use it
If you're familiar with how to run python scripts from the terminal, then you can probably skip this section. If you're new to game, this should help.

### Step 1
Navigate to the folder previously downloaded


`cd ~/path/to/MovieTheaterSeating`


### Step 2
**NOTE:** This python scripts takes in 2-3 parameters. The third parameter is *optional**

`python3 main.py [path/to/inputFile] [showtheater OR runtests]*`

## Execute Tests
The following test cases have been written and can be executed using the following command:

`python3 main.py [path/to/inputFile] runtests`

* **Sufficient Number of Seats** - determines whether there are enough seats to fill reservation demand
* **Valid Reservation Format** - checks that the input file is in the expected format
