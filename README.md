# Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Web scraper

- My webcam had broken so I attempted to source the images online. This meant that initially I built a web scraper (web_scraper.py). The web scraper contains a couple of functions for downloading and saving images from links provided, reliant on BeautifulSoup (used to parse HTML content from web metadata). 

![Screenshot from 2023-06-29 10-06-58](https://github.com/FrancesGorka/computer-vision-rock-paper-scissors/assets/27502612/9275956f-a447-4978-bcb2-9ba6b12b5e3b)

- I found that a limited number of images were installing due to the fact that google loads images once you scroll to the bottom of the window. So I built a chrome driver via Selenium that simulates scrolling within a webpage. Effectively each 1 second it will scroll, up to a limit of 20 scrolls. This is based on an estimate of no. of images downloaded per page. I was aiming for 1000 images.
- I attempted to tidy up the code by bringing the driver into the web scraper as a parameter, then the code broke. I decided I'd spend too much time on it, so used a friends computer to take pictures of my hands in the three gestures, in a variety of lightings and positions (around 200 each, a tiny number for a computer vision task).
- 
## Training the model

- I used "Teachable Machine" to train a machine learning model built with Keras (keras_model.h5).
