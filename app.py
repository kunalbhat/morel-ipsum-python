# Setup Flask
from flask import Flask
app = Flask(__name__)

from flask import Flask, url_for, render_template

# Imports
import random

# App routing
@app.route("/")

# Index page
def index(morel=None):

    morelipsum = []

    # Dictionary
    dictionary = ['morel ipsum', 'crimini', 'portabella', 'maitake',
            'shiitake', 'enoki', 'oyster', 'beech', 'chanterelle', 'boletus edulis',
            'cantharellus cibarius', 'cantharellus tubaeformis',
            'clitocybe nuda', 'cortinarius caperatus', 'craterellus cornucopioides',
            'grifola frondosa', 'gyromitra esculenta', 'hericium erinaceus',
            'hydnum repandum', 'lactarius deliciosus', 'morchella', 'tricholoma matsutake',
            'amanita caesarea', 'armillaria mellea', 'boletus badius', 'chroogomphus rutilus',
            'calvatia gigantea', 'calocybe gambosa', 'clavariaceae',
            'clavulinaceae', 'coprinus comatus', 'fistulina hepatica',
            'cortinarius variicolor', 'hygrophorus chrysodon', 'lactarius salmonicolor',
            'lactarius volemus', 'lactarius subdulcis', 'laetiporus sulphureus',
            'leccinum aurantiacum', 'leccinum scabrum', 'lepiota procera',
            'amanita muscaria', 'coprinopsis atramentaria', 'gyromitra esculenta',
            'verpa bohemica', 'auricularia auricula-judae', 'suillus bovinus',
            'suillus granulatus', 'suillus luteus', 'suillus tomentosus',
            'tricholoma terreum', 'rhizopogon luteolus', 'russula', 'sparassis crispa' ]

    # Generate a sentence
    def generateSentence():
      # Randomize sentence length
      words = random.randint(4, 8)

      # Initialize sentence string
      sentence = ""

      # Randomly select a word from the dictionary
      # and append to the sentence string
      for word in range(words):
        word = random.choice(dictionary)

        sentence += word + " "

      # Trim trailing whitespace and capitalize sentence
      sentence = sentence.strip().capitalize() + "."

      return sentence

    # Generate a paragraph
    def generateParagraph(count):
      sentences = random.randint(2, 4)

      for x in range(count):
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
    morel = generateParagraph(10)

    return render_template('index.html', morel=morel)

if __name__ == "__main__":
    app.run()
