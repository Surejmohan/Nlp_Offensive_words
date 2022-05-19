# Nlp_Offensive_words

sudo docker build -t nlpapi .
sudo docker run -d -p 5000:5000 -it nlpapi


#Running Local

1) Creating Virtual environment
     python3 -m venv <env_name>
2) Activating environment (windows)
     ./env_name/Scripts/activate
3) Install Requirements
     pip3 install -r requirements.txt
4) Install pytorch  (windows)
    pip3 install torch torchvision torchaudio
5) Run Application
      python app.py
