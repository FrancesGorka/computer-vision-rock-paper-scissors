# Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Web scraper

- My webcam had broken so I attempted to source the images online. This meant that initially I built a web scraper (web_scraper.py). The web scraper contains a couple of functions for downloading and saving images from links provided, reliant on BeautifulSoup (used to parse HTML content from web metadata). 

![Screenshot from 2023-06-29 10-06-58](https://github.com/FrancesGorka/computer-vision-rock-paper-scissors/assets/27502612/9275956f-a447-4978-bcb2-9ba6b12b5e3b)

- I found that a limited number of images were installing due to the fact that google loads images once you scroll to the bottom of the window. So I built a chrome driver via Selenium that simulates scrolling within a webpage. Effectively each 1 second it will scroll, up to a limit of 20 scrolls. This is based on an estimate of no. of images downloaded per page. I was aiming for 1000 images.
- I attempted to tidy up the code by bringing the driver into the web scraper as a parameter, then the code broke. I decided I'd spend too much time on it, so used a friends computer to take pictures of my hands in the three gestures, in a variety of lightings and positions (around 200 each, a tiny number for a computer vision task).
- 
## Training the model

- I used "Teachable Machine" to train a machine learning model built with Keras (keras_model.h5). It's not likely to be particularly accurate as I only trained it with ~200 images for each class.

## RPS-Template: Running the model

This file contains a function camera_prediction() which runs the pre-trained model and returns the prediction: 
- The model is loaded and then the camera is initialised. 
- A numpy array is created of shape (1, 224, 224, 3) which corresponds to a single image with height 224, width 224, and 3 channels (RGB). 
- The frame image is repeatedly read, resized, normalised and stored in the empty numpy array. This stops after 10s.
- The model then creates a prediction based on the values in the numpy array. This is a probability vector for how likely it is the captured image is scissors, paper and rock respectively.

## Creating the manual game

This file defines three functions:
- one function creates a variable for the computer's choice between rock, paper and scissors. This is chosen randomly
- one function creates a variable for the user's choice. This is dependent upon user input. Currently there are no error messages for incorrect input.
- The final function calls both of these functions and then uses if/elif/else statements to articulate a winner and print win/loss messages

The final function is called within the file.

![Screenshot from 2023-06-30 22-50-16.png](/home/frances/Pictures/Screenshot from 2023-06-30 22-50-16.png)

## Creating the camera input game

- This file creates a version of the manual input game whereby the user inputs their choice. In this case, the choice is identified by the webcam.
- The function get_prediction imports and calls the camera_prediction from RPS_Template, which uses a computer vision model to create a probability vector corresponding to choices of scissors, paper and rock
- the maximum value (most likely option) in this probability vector becomes the user's choice. The computer choice is random.
- The get_winner function finds the winner according to the combination of computer and user choice.
- The play() function uses the aforementioned three functions to create a game, returning the winner.
- best_of_three tracks winners and stops the game when either the user or computer reaches 3 wins.
