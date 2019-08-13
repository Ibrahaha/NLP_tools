# NLP_tools
A container that includes state-of-the-art tools in NLP for Named Entity Recognition (SpaCy, Stanfordcorenlp, nltk ,Allennlp) and Coreference Resolution (neuralcoref). You can use NER and Coreference resolution both as servers or from containers' bash.

- **Operating system**: Linux · Windows (Cygwin, MinGW, Visual Studio) · macOS / OS X
- **Package managers**: [Docker] [docker-compose]
- **Docker image version**: Python:3.6

## Build Named Entity Recognition container
First, you need to be in the nlp-ner folder with your bash.
```bash
cd ./nlp-tools/nlp-ner
chmod +x build.sh
./build.sh
```
Once your container is build, you can run it.
```bash
docker run -it -p 8080:5000 isouleymane/nlp-ner sh
```
