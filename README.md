# batcher-banyan-network
An implementation of Batcher Banyan network simulation using python

## How to run a simulation
```bash
TBD
```

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

