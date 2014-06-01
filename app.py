import random

# Dictionary
dictionary = ['morel ipsum', 'crimini', 'portabella', 'maitake', 'shiitake', 'enoki',
              'oyster', 'beech', 'chanterelle', 'boletus edulis', 'cantharellus cibarius',
              'cantharellus tubaeformis', 'clitocybe nuda', 'cortinarius caperatus',
              'craterellus cornucopioides', 'grifola frondosa', 'gyromitra esculenta',
              'hericium erinaceus', 'hydnum repandum', 'lactarius deliciosus', 'morchella',
              'tricholoma matsutake', 'amanita caesarea', 'armillaria mellea', 'boletus badius',
              'chroogomphus rutilus', 'calvatia gigantea', 'calocybe gambosa', 'clavariaceae',
              'clavulinaceae', 'coprinus comatus', 'fistulina hepatica', 'cortinarius variicolor',
              'hygrophorus chrysodon', 'lactarius salmonicolor', 'lactarius volemus', 'lactarius subdulcis',
              'laetiporus sulphureus', 'leccinum aurantiacum', 'leccinum scabrum', 'lepiota procera'
             ]

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
def generateParagraph():
  sentences = random.randint(2, 4)

  paragraph = ""

  for sentence in range(sentences):
    sentence = generateSentence()

    paragraph += sentence + " "

  # Trim trailing whitespace
  paragraph = paragraph.strip()

  return paragraph

# Call the generateSentence() function
print generateParagraph()

