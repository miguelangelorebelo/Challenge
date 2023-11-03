# Continental MLE Challenge

### Author: Miguel Ângelo Pontes Rebelo

To see it in action simply run: \
read the NOTE in configs/database_config.py \
`make up`

Alternatively (if low on RAM): \
create new environment \
activate environment \
`pip install -r requirements.txt` \
`docker run -p 3306:3306 -d --name mariadb -eMARIADB_ROOT_PASSWORD=password mariadb:latest` \
`uvicorn main:app --reload`

This will use docker compose to build the containers and start them.

You can connect to the db:\
host: localhost \
port: 3306 \
user: root \
password: password (very secure)

To remove them (and the images):
`make down`

The process goes like this:

1. The first time it runs `create_db.py` script that creates the db and table in the MariaDB WH container.
2. Then runs `download_models.py` to download the pretrained models to store them locally.
3. Start the API in the port 8000.
4. The API docs is available at 5001/docs (docker) or 8000/docs (local)
5. The gradio app is available at 5001/gradio (docker) or 8000/gradio (local)

**Treats**:

- in utils a singleton pattern assures that the models are only loaded the first time, assuring fast responses for the
  following requests.
- A custom gradio flagger catches the flags _incorrect_ or _vague_ and stores them in a table, along with prompt, date,
  model, response.
- These models (dolly) need a special `ìnstruct_pipeline.py` script from the developers that, without downloading needs
  to be run remotely. But the `download_models.py` script gets it and stores it in the corresponding model folder.

I hope you like the project. It was fun to build it.
