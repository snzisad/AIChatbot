# Chat with AI 
This project was developed for the fourth lab of cloud service course. In this repository, I have used docker, django, gunicorn, etc.

## How to run

Install docker
```bash
https://docs.docker.com/engine/install/ubuntu/
```

Install Python
```bash
sudo apt update
sudo apt install python3
```

Install PIP
```bash
sudo apt install python3-pip
```

Copy ENV file
```bash
cp .env.example .env
```

Generate django secret key
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Generate open ai key
```bash
https://beta.openai.com/account/api-keys
```

Copy and paste django secret key and open ai api key in .env file

Run project
```bash
sudo docker compose up --build
```

Run project in the background
```bash
sudo docker compose up -d
```

Stop the docker that is running in the background
```bash
sudo docker compose down
```
