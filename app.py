import random

# Dictionary
words = ['morel', 'crimini', 'portabella', 'maitake', 'shiitake', 'enoki',
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
  count = random.randint(8, 16)

  # Initialize sentence string
  sentence = ""

  # Randomly select a word from the dictionary
  # and append to the sentence string
  for x in range(count):
    word = random.choice(words)

    sentence += word + " "

  # Trim trailing whitespace and capitalize sentence
  sentence = sentence.strip().capitalize() + "."

  print sentence

# Call the generateSentence() function
generateSentence()

