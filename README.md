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

### Named Entities in SpaCy
The SpaCy Named Entity Recognition model trained on the `OntoNotes 5` corpus supports the following entity types:
| Type         |  Description
|-----------|--|-------------------------------------------------------                      
|`PERSON`      |People, including fictional.
|`NORP`	   |Nationalities or religious or political groups.
|`FAC`	   |Buildings, airports, highways, bridges, etc.
|`ORG`	   |Companies, agencies, institutions, etc.
|`GPE`	   |Countries, cities, states.
|`LOC`	   |Non-GPE locations, mountain ranges, bodies of water.
|`PRODUCT`	   |Objects, vehicles, foods, etc. (Not services.)
|`EVENT`	   |Named hurricanes, battles, wars, sports events, etc.
|`WORK_OF_ART` |	Titles of books, songs, etc.
|`LAW`	   |Named documents made into laws.
|`LANGUAGE`	   |Any named language.
|`DATE`	   |Absolute or relative dates or periods.
|`TIME`	   |Times smaller than a day.
|`PERCENT`	   |Percentage, including ”%“.
|`MONEY`	   |Monetary values, including unit.
|`QUANTITY`	   |Measurements, as of weight or distance.
|`ORDINAL`	   |“first”, “second”, etc.
|`CARDINAL`	   |Numerals that do not fall under another type.

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
### Using NeuralCoref

NeuralCoref will resolve the coreferences and annotate them as [extension attributes](https://spacy.io/usage/processing-pipelines#custom-components-extensions) in the spaCy `Doc`,  `Span` and `Token` objects under the `._.` dictionary.

Here is the list of the annotations:

|  Attribute                |  Type              |  Description
|---------------------------|--------------------|-----------------------------------------------------
|`doc._.has_coref`          |boolean             |Has any coreference has been resolved in the Doc
|`doc._.coref_clusters`     |list of `Cluster`   |All the clusters of corefering mentions in the doc
|`doc._.coref_resolved`     |unicode             |Unicode representation of the doc where each corefering mention is replaced by the main mention in the associated cluster.
|`doc._.coref_scores`       |Dict of Dict        |Scores of the coreference resolution between mentions.
|`span._.is_coref`          |boolean             |Whether the span has at least one corefering mention
|`span._.coref_cluster`     |`Cluster`           |Cluster of mentions that corefer with the span
|`span._.coref_scores`      |Dict                |Scores of the coreference resolution of & span with other mentions (if applicable).
|`token._.in_coref`         |boolean             |Whether the token is inside at least one corefering mention
|`token._.coref_clusters`   |list of `Cluster`   |All the clusters of corefering mentions that contains the token

A `Cluster` is a cluster of coreferring mentions which has 3 attributes and a few methods to simplify the navigation inside a cluster:

|  Attribute or method   |  Type / Return type |  Description
|------------------------|---------------------|-----------------------------------------------------
|`i`                     |int                  |Index of the cluster in the Doc
|`main`                  |`Span`               |Span of the most representative mention in the cluster
|`mentions`              |list of `Span`       |List of all the mentions in the cluster
|`__getitem__`           |return `Span`        |Access a mention in the cluster
|`__iter__`              |yields `Span`        |Iterate over mentions in the cluster
|`__len__`               |return int           |Number of mentions in the cluster
