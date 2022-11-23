from copy import deepcopy
from dataclasses import dataclass
from typing import List, Sequence

import numpy as np


@dataclass
class GifterGiftee:
    """Class representing a gifter / giftee pair."""

    gifter: str
    giftee: str


def load_participants(path: str) -> List[str]:
    """
    Load the list of participants from the input file.

    :param path: path to the file containing the participants
    :return: list of participants
    """
    with open(path, "r") as file:
        return [row.strip() for row in file]


def shuffle_participants(participants: Sequence[str]) -> List[str]:
    """
    Shuffle the list of participants.

    :param participants: list of participants
    :return: new list of participants in another order
    """

    SEED = 0

    participants_shuffled = deepcopy(participants)
    np.random.seed(SEED)
    np.random.shuffle(participants_shuffled)
    return list(participants_shuffled)


def generate_gifters_giftees_list(participants: Sequence[str]) -> List[GifterGiftee]:
    """
    Generate the list of gifters / giftees.

    :param participants: list of participants
    :return: list of gifters / giftees
    """

    participants_shuffled = shuffle_participants(participants)
    return [
        GifterGiftee(participants_shuffled[i - 1], participants_shuffled[i])
        for i in range(len(participants_shuffled))
    ]


def display_participants(participants: Sequence[str]) -> None:
    """
    Display the list of participants.

    :param participants: list of participants
    """

    print("Participants\n")
    for p in participants:
        print(f"- {p}")
    print()


def display_gifters_giftees(gifters_giftees: Sequence[GifterGiftee]) -> None:
    """
    Display the list of gifters / giftees.

    :param participants: list of gifters / giftees
    """

    print("Gifters / giftees\n")
    for gg in gifters_giftees:
        print(f"- {gg.gifter:12s} will offer a present to {gg.giftee}")
    print()


def main():

    PATH = "participants.txt"

    participants = load_participants(PATH)
    display_participants(participants)

    gifters_giftees = generate_gifters_giftees_list(participants)
    display_gifters_giftees(gifters_giftees)


if __name__ == "__main__":
    main()
