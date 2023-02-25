import spacy

# Garden path sentence list.
gardenPathSentences = [
    "The complex houses married and single soldiers and their families.",
    "The old man the boat.",
    "The horse raced past the barn fell.",
    "Fat people eat accumulates.",
    "The prime number few.",
    "Time flies like an arrow, but fruit flies like a banana.",
    "The man who whistles tunes pianos.",
    "The man returned to his house was happy.",
    "We painted the wall with cracks.",
    "I gave the kid the dog bit a band-aid.",
    "I've convinced her children are noisy.",
    "Southern European people like Italians like dishes like pasta."
]

# Load spacy.
nlp = spacy.load("en_core_web_sm")

for each in gardenPathSentences:
    print(each)
    
    # Tokenize each sentence
    nlp_tok = nlp(each)
    nlp_tok.text.split()
    tokenized = [token.orth_ for token in nlp_tok]
    print("tokenized: {}".format(tokenized))

    # Run entity recognition
    nlp_rec = nlp(each)
    entity_rec = [(i, i.label_, i.label) for i in nlp_rec.ents]
    print("entity_recognition: {}\n".format(entity_rec))

    if entity_rec:
        # Explain each entity, if found.
        for each_rec in entity_rec:
            entity_fac = spacy.explain(entity_rec[0][1])
            print("{}:{}".format(entity_rec[0][1], entity_fac))
    

"""
Many of the entity recognitions returned an empty list, except for 'Southern European people like Italians like dishes like pasta.'


What was the entity and its explanation that you looked up?
- NORP: Nationalities or religious or political groups

Did the entity make sense in terms of the word associated with it?
- Yes, as Italians and Southern European People are nationalities.

The complex houses married and single soldiers and their families.
tokenized: ['The', 'complex', 'houses', 'married', 'and', 'single', 'soldiers', 'and', 'their', 'families', '.']
entity_recognition: []

The old man the boat.
tokenized: ['The', 'old', 'man', 'the', 'boat', '.']
entity_recognition: []

The horse raced past the barn fell.
tokenized: ['The', 'horse', 'raced', 'past', 'the', 'barn', 'fell', '.']
entity_recognition: []

Fat people eat accumulates.
tokenized: ['Fat', 'people', 'eat', 'accumulates', '.']
entity_recognition: []

The prime number few.
tokenized: ['The', 'prime', 'number', 'few', '.']
entity_recognition: []

Time flies like an arrow, but fruit flies like a banana.
tokenized: ['Time', 'flies', 'like', 'an', 'arrow', ',', 'but', 'fruit', 'flies', 'like', 'a', 'banana', '.']
entity_recognition: []

The man who whistles tunes pianos.
tokenized: ['The', 'man', 'who', 'whistles', 'tunes', 'pianos', '.']
entity_recognition: []

The man returned to his house was happy.
tokenized: ['The', 'man', 'returned', 'to', 'his', 'house', 'was', 'happy', '.']
entity_recognition: []

We painted the wall with cracks.
tokenized: ['We', 'painted', 'the', 'wall', 'with', 'cracks', '.']
entity_recognition: []

I gave the kid the dog bit a band-aid.
tokenized: ['I', 'gave', 'the', 'kid', 'the', 'dog', 'bit', 'a', 'band', '-', 'aid', '.']
entity_recognition: []

I've convinced her children are noisy.
tokenized: ['I', "'ve", 'convinced', 'her', 'children', 'are', 'noisy', '.']
entity_recognition: []

Southern European people like Italians like dishes like pasta.
tokenized: ['Southern', 'European', 'people', 'like', 'Italians', 'like', 'dishes', 'like', 'pasta', '.']
entity_recognition: [(Southern European, 'NORP', 381), (Italians, 'NORP', 381)]

The dog that I had really loved bones.
tokenized: ['The', 'dog', 'that', 'I', 'had', 'really', 'loved', 'bones', '.']
entity_recognition: []
"""
