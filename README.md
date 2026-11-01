<img width="911" height="474" alt="image" src="https://github.com/user-attachments/assets/0a9872f0-9557-4131-8bac-1a37e971f1b3" />


# HarbourInfo
A small Python program that outputs useful data for deciding where to launch a boat. 

# Context
This is some very basic code and not an attempt to design a full application. 



# Nuala I don’t know tech stuff, can you talk me through it

Yes.

## Python3

This is the coding language. 

You can download an IDE to write and run code. I like Pycharm. 

There are lots of different coding languages. Python3 is a “high level” one, which means there is a lot of work going on behind the scenes you do not need to do, and that allows you to focus on what you are actually trying to get on with. 

## API aka Application Programming Interface

The API in this case is openweathermap. Openweathermap is where all of the real time weather data is coming from. The program I have written interacts with openweathermap, by requesting a receiving data, doing some basic analysis of it, and then outputting that analysis.

## The different files

You are currently reading the README, and the license explains what people can or cannot do with what I have published here. Main is the main file with the code in. 

Requirements tells you/your computer what extra things you need to download. Remember I was just talking about Python3? Python3 comes with different packages (aka libraries) that do different things behind the scenes, so you do not need to manually write it all out. So those libraries need to go in the requirements file.

Gitignore is a list of files that do exist, but have not been uploaded here. In there, you will see a reference to a config file. This file contains the API key, which is like a password that is used to access the API – openweathermap. I do not want to share my password, which is why the config file is in gitignore. If you were running this yourself, you would go and get your own password and make your own config file, which is really simple to do.


# How the code works:

1. It starts by importing the things it needs into the file, which are in the requirements and config files.

2. It knows which API it’s dealing with and what the key is.

3. It collects information to figure out what to request from the API. It is doing this by asking the user a couple questions. The user would input this into the console of the IDE – ie, they are not editing the code, they are being asked a question in a separate window and answering it.

4. How it’s storing the data (it is storing it as location1 and location2)

5. How it’s comparing the locations' data that it is getting back from openweathermap.

6. How stores the comparison between location1 and location2.

7. It outputs it all into a file.

# Ok great so are you planning on expanding this into something normal people can actually use
Probably not, no :-)
