import spacy
from spacy import displacy

# Build a natural language model
nlp = spacy.load('en_core_web_sm')

if __name__ == '__main__':
    text = "Talend was founded by Bertrand Diard and Fabrice Bonan in 2005. They managed it until the company  was introduced to the stock market."
    doc = nlp(text)
    displacy.serve(doc, style="ent")
