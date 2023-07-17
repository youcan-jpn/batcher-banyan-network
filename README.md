# batcher-banyan-network
An implementation of Batcher Banyan network simulation using python

## How to run a simulation
```bash
$ cd batcher-banyan-network
$ docker compose up -d --build
$ docker exec bbn poetry run python src/main.py
```
You can edit src/main.py to change configurations!

## How to develop
```bash
$ cd batcher-banyan-network
$ docker compose up -d --build
$ docker exec -it bbn bash
```

## How to format and lint
```bash
# (all commands should be run in the container)
$ poetry run isort .
$ poetry run black .
$ poetry run pflake8 .
```

