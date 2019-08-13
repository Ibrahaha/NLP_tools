# NLP_tools
A container that includes state-of-the-art tools in NLP for Named Entity Recognition (SpaCy, Stanfordcorenlp, nltk ,Allennlp) and Coreference Resolution (neuralcoref). You can use NER and Coreference resolution both as servers or from containers' bash.

- **Operating system**: Linux · Windows (Cygwin, MinGW, Visual Studio) · macOS / OS X
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
>>> text = "My friend John Doe bought his computer from Amazon for $700 in 2013."
>>> doc = nlp(text)
>>> for ent in doc.ents:
      print(ent.text,ent.label_)
      
John Doe PERSON
Amazon ORG
700 MONEY
2013 DATE

```
