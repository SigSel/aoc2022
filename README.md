# aoc2022

Solutions for Advent of Code 2022 assembled as a Python package with the entry point `aoc2022`. If you have any suggestings for improvements feel free to submit a PR :santa:

Example use for day 1:
```console
(clever_env_name_goes_here) beeg@yoshi:~$ ls inputs/
day1_input.txt
(clever_env_name_goes_here) beeg@yoshi:~$ aoc2022 --day 1
Solution for the first puzzle of day 1: 
67622
Solution for the second puzzle of day 1:
201491
```

## Setup

Untill soltuions for all the days have been implemented I will recommend to install the package in developer mode. In that way reinstall is not needed when pulling new changes :bug:

To do so you need exectue the following steps:
1. Clone the repo
* ```git clone https://github.com/SigSel/aoc2022.git```
2. Go into the folder using
* ```cd aoc2022```
3. It is recommended to use a virtual environment (if you don't want to, you can skip to step 4). You can either do this using the command line or with your IDE of choice (if it has support for that). To create it using the command line you can execute the following commands:
* Make sure virtualenv is installed 
  * ```pip install virtualenv```
* Create your virtual environment 
  * ```python -m virtualenv clever_env_name_goes_here```
* Activate your virtual environment 
  * ```source clever_env_name_goes_here/bin/activate``` for Linux
  * ```clever_env_name_goes_here\Scripts\activate.bat``` on Windows

4. Install the package in developer mode. Note: You have to be in the same folder as the setup.py file
* ```pip install -e .```
* or ```pip install -e .[dev]``` to install in developer mode

Then you are free to make changes and use the package!<br>
When you are finished with what you want to do you can deactivate the virtual environment using
* ``` deactivate ```

## Use
When you have installed the package, you can call the package entry point from the command line using `aoc2022` combined with the argument `--day` (example at the top of README). To be able to get the solutions for your own entries, you need to have a folder called `inputs` in the same place where you run the command. Inside this folder you need to put your input in `.txt` file named `dayx_input.txt` where `x` is the day you want to solve for. Note: all days are not supported yet :)<br>
The end point is hooked up to the ![__main__.py](aoc2022/__main__.py) file.
