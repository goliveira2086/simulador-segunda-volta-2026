import numpy as np


def votes_from_one_group(
    nbr_voters_first_turn, probability_to_turnout, probability_to_vote_for_candidate
):
    """
    Simulates the number of votes received by a candidate from a single voter group.

    Parameters:
    nbr_voters_first_turn (int): Number of voters in the group.
    probability_to_turnout (float): Probability that a voter turns out to vote.
    probability_to_vote_for_candidate (float): Probability that a voter votes for the candidate.

    Returns:
    int: Number of votes received by the candidate from this group.
    """
    # Simulate turnout
    turnout = np.random.binomial(nbr_voters_first_turn, probability_to_turnout)

    # Simulate votes for the candidate
    votes = np.random.binomial(turnout, probability_to_vote_for_candidate)

    return turnout, votes
