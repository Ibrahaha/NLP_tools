# NLP_tools
A container that includes state-of-the-art tools in NLP for Named Entity Recognition (SpaCy, Stanfordcorenlp, nltk ,Allennlp) and Coreference Resolution (neuralcoref). You can use NER and Coreference resolution both as servers or from containers' bash.

- **Operating system**: Linux · Windows · macOS / OS X
- **Package managers**: [Docker] [docker-compose]
- **Docker image version**: Python:3.6

## Build and Run Named Entity Recognition container
First, you need to be in the nlp-ner folder with your bash.
```bash
cd ./nlp-tools/nlp-ner
chmod +x build.sh
./build.sh
```
Once your container is build, you can run it.
```bash
docker run -it isouleymane/nlp-ner sh
```
When your container is ready, you directly have access to its bash. You can use `SpaCy`, `nltk`, `stanfordnlp` or `allennlp` to solve natural language processing tasks. For example, we can use `SpaCy` pre-trained language model `en_core_web_sm` for NER. 
```bash
# python
>>> import spacy
>>> nlp = spacy.load('en_core_web_sm')
>>> text = "John Doe bought his computer from Amazon for $700 in 2013."
>>> doc = nlp(text)
>>> for ent in doc.ents:
      print(ent.text,ent.label_)
      
John Doe PERSON
Amazon ORG
700 MONEY
2013 DATE

```
## Build and Run Coreference Resolution based on neuralcoref container
As for Named Entity Recognition, you need to be in the nlp-coref folder with your bash.
```bash
cd ./nlp-tools/nlp-coref
chmod +x build.sh
./build.sh
```
Once your container is build, you can run it.
```bash
docker run -it isouleymane/nlp-coref sh
```
### Adding NeuralCoref to the pipe of an English SpaCy Language
To load neuralcoref, we need to set up a pipe of an English SpaCy model as for NER task in SpaCy.
```bash
# python

>>> import spacy   # Load your usual SpaCy model (one of SpaCy English models)
>>> nlp = spacy.load('en')


>>> import neuralcoref # Add neural coref to SpaCy's pipe
>>> neuralcoref.add_to_pipe(nlp)

>>> doc = nlp(u'My sister has a dog. She loves him.') # You're done. You can now use NeuralCoref as you usually manipulate                      a SpaCy document annotations.

doc._.has_coref
doc._.coref_clusters
```
