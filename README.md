# Kata: Idiomatic python

kata to practice some python idioms. Based on the book _Writing Idiomatic Python_ of Jeff Knupp.

## Running the kata 

This kata assumes you have basic knowledge of python and unit testing.
The main objective is to practice python within pair programming and debate about different type of resolutions that come to minds due to the variety of reources the language provide.
The steps to accomplish the kata are:
1. Initial Status: All Test are in red ( except linter test)
2. Work in pair programming or alone to put all the tests in green. Having in mind that `tests` module is immutable.
3. Delete the code.

## Code Structure

The code is divided in two modules:
+ `Kata`: Module that contains the logic of a Task Board, where the key concept is that we can add tasks to columns within a board and classify boards using tags. 
The rest of the logic will be describe via unit tests. This module is the one in wich we code to complete the kata. 
+ `Tests`: MOdule containg the specification of the Board's logic using unit test and [pytest library](https://doc.pytest.org/). This module is immutable when we are accomplishing the kata.

## Environment

In order to run the code we can use:
1. The Makefile have predefined commands that runs in a docker container:
  * `make build`: to build the container
  * `make shell`: to run an interactive bash console inside the container.
  * `make test`: to run all the tests

2. Virtualenv:
Create and activate
```
python3 -m venv venv
source venv/bin/activate
EXPORT PYTHONPATH=<your_path>
```

Deactive
```
deactivate
```