import numpy as np
import pandas as pd

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

def simulate_second_round(voter_groups, n_simulations=10000):
    np.random.seed(1143)
    results = []
    for _ in range(n_simulations):
        total_votes_candidate_1 = 0
        total_votes_candidate_2 = 0
        total_turnout = 0
        for group in voter_groups:
            turnout, votes = votes_from_one_group(
                group["first_turn_votes"],
                group["probability_to_turnout"],
                group["probability_to_vote_for_candidate"]
            )
            total_votes_candidate_1 += votes
            total_votes_candidate_2 += turnout - votes
            total_turnout += turnout        
        results.append((total_votes_candidate_1, total_votes_candidate_2, total_turnout))
    return results

def create_scenario(voters_groups, n_simulations=10000):
    results_scenario = simulate_second_round(voters_groups, n_simulations=n_simulations)
    results_scenario_df = pd.DataFrame(results_scenario, columns=["Ventura", "Seguro", "Turnout"])
    results_scenario_df["Ventura_Wins"] = results_scenario_df["Ventura"] > results_scenario_df["Seguro"]

    return results_scenario_df