# The Secret Santa project


## Introduction

Every year, we organize a Secret Santa in my family. I've written a tiny piece of code to randomly generate the gifter / giftee pairs.


## How to use


### Install Poetry

This project uses Poetry. The first step to use the code is to [install Poetry](https://python-poetry.org/docs/#installation).

Poetry usually executes the code though a virtual environment. I recommand to setup Poetry so that it creates virtual environment within the project :

```bash
poetry config virtualenvs.in-project true
```

We can now create the virtual environment using:

```bash
poetry install
```


### Edit the list of participants

You can edit the list of participants which is located in the file `participants.txt`.


### Run Secret Santa !

To run the Secret Santa code and get the list of gifter / giftee pairs, simply run:

```bash
poetry run python secret_santa.py
```

The results will be displayed in the terminal.

Note that the code is deterministic and results won't change when you re-run the code. In order to change the gift attribution (for next year for instance), simply change the `SEED` constant to another value in the file `secret_santa.py`.
