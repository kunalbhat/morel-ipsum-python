# Imports
import os
import random
import dictionary
from flask import Flask, url_for, render_template, request

# Setup Flask
app = Flask(__name__)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

# Generate route
@app.route('/generate')
def generate(morel=None):

    morelipsum = []

    # Generate a sentence
    def generateSentence():
      # Randomize sentence length
      words = random.randint(4, 8)

      # Initialize sentence string
      sentence = ""

      # Randomly select a word from the dictionary
      # and append to the sentence string
      for word in range(words):
        word = random.choice(dictionary.dictionary)

        sentence += word + " "

      # Trim trailing whitespace and capitalize sentence
      sentence = sentence.strip().capitalize() + "."

      return sentence

    # Generate a paragraph
    def generateParagraph(count):

      for x in range(count):
          sentences = random.randint(2, 4)

          # Reset paragraph
          paragraph = ""

          for sentence in range(sentences):
              sentence = generateSentence()

              paragraph += sentence + " "

          # Trim trailing whitespace
          paragraph = paragraph.strip()

          morelipsum.append(paragraph)

      return morelipsum

    # Call a generate function
    morel = generate_paragraph(10)

    return render_template('generate.html', morel=morel)

if __name__ == "__app__":
    app.run()

