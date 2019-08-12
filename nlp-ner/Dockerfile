FROM python:3.6

WORKDIR '/app'
       # Dependencies
COPY . .
# update pip
RUN python3.6 -m pip install pip --upgrade
RUN pip install spacy==2.1.3
RUN pip install -r requirements.txt

# Spacy models model
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_lg


CMD ["python", "main.py", "server.py"]
