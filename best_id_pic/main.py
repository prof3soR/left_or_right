import os
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Folder containing images
IMAGE_FOLDER = 'static/images'

# List to store image filenames
image_list = []

# Populate image_list with filenames from IMAGE_FOLDER
for filename in os.listdir(IMAGE_FOLDER):
    if filename.endswith('.jpg'):
        image_list.append(filename)

# Dictionary to store votes for each image
votes = {filename: 0 for filename in image_list}


@app.route('/')
def index():
    # Check if there are images left to display
    if len(image_list) == 0:
        return "No more images to display."

    # Select two random images without replacement
    random_images = random.sample(image_list, 2)

    # Render the HTML template with the random images
    return render_template('index.html', image1=random_images[0], image2=random_images[1])


@app.route('/vote', methods=['POST'])
def vote():
    # Get the filename of the voted image
    voted_image = request.form['voted_image']

    # Increment the vote for the voted image
    votes[voted_image] += 1

    # Remove the voted image from image_list
    image_list.remove(voted_image)

    # Redirect to the homepage to display the next pair of images
    return index()


if __name__ == '__main__':
    app.run(debug=True)
