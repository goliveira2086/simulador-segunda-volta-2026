import numpy as np
import pandas as pd


def create_voter_group(
    seguro_turnout,
    seguro_vote_for_candidate,
    ventura_turnout,
    ventura_vote_for_candidate,
    figueiredo_turnout,
    figueiredo_vote_for_candidate,
    gouveia_melo_turnout,
    gouveira_melo_vote_for_candidate,
    marques_mendes_turnout,
    marques_mendes_vote_for_candidate,
    martins_turnout,
    martins_vote_for_candidate,
    filipe_turnout,
    filipe_vote_for_candidate,
    vieira_turnout,
    vieira_vote_for_candidate,
    pinto_vote_turnout,
    pinto_vote_for_candidate,
    silva_turnout,
    silva_vote_for_candidate,
    correia_turnout,
    correia_vote_for_candidate,
    abstentionist_turnout,
    abstentionist_vote_for_candidate,
):
    portugal_all_voters = 9262653 + 1754549
    portugal_valid_votes = 5696638 + 70419
    portugal_blank_votes = 60899 + 327
    portugal_null_votes = 64817 + 564
    portugal_abstentionists = portugal_all_voters - (
        portugal_valid_votes + portugal_blank_votes + portugal_null_votes
    )

    # Create dictionaries for each voter group
    eleitor_portugal_seguro = {
        "first_turn_votes": 1738741,
        "probability_to_turnout": seguro_turnout,
        "probability_to_vote_for_candidate": seguro_vote_for_candidate,
    }
    eleitor_portugal_ventura = {
        "first_turn_votes": 1297533,
        "probability_to_turnout": ventura_turnout,
        "probability_to_vote_for_candidate": ventura_vote_for_candidate,
    }
    eleitor_portugal_figueiredo = {
        "first_turn_votes": 891788,
        "probability_to_turnout": figueiredo_turnout,
        "probability_to_vote_for_candidate": figueiredo_vote_for_candidate,
    }
    eleitor_portugal_gouveia_melo = {
        "first_turn_votes": 691489,
        "probability_to_turnout": gouveia_melo_turnout,
        "probability_to_vote_for_candidate": gouveira_melo_vote_for_candidate,
    }
    eleitor_portugal_marques_mendes = {
        "first_turn_votes": 631809,
        "probability_to_turnout": marques_mendes_turnout,
        "probability_to_vote_for_candidate": marques_mendes_vote_for_candidate,
    }
    eleitor_portugal_martins = {
        "first_turn_votes": 114468,
        "probability_to_turnout": martins_turnout,
        "probability_to_vote_for_candidate": martins_vote_for_candidate,
    }
    eleitor_portugal_filipe = {
        "first_turn_votes": 91889,
        "probability_to_turnout": filipe_turnout,
        "probability_to_vote_for_candidate": filipe_vote_for_candidate,
    }
    eleitor_portugal_vieira = {
        "first_turn_votes": 60266,
        "probability_to_turnout": vieira_turnout,
        "probability_to_vote_for_candidate": vieira_vote_for_candidate,
    }
    eleitor_portugal_pinto = {
        "first_turn_votes": 37671,
        "probability_to_turnout": pinto_vote_turnout,
        "probability_to_vote_for_candidate": pinto_vote_for_candidate,
    }
    eleitor_portugal_silva = {
        "first_turn_votes": 10674,
        "probability_to_turnout": silva_turnout,
        "probability_to_vote_for_candidate": silva_vote_for_candidate,
    }
    eleitor_portugal_correia = {
        "first_turn_votes": 4594,
        "probability_to_turnout": correia_turnout,
        "probability_to_vote_for_candidate": correia_vote_for_candidate,
    }
    eleitor_portugal_abstencionista = {
        "first_turn_votes": portugal_abstentionists,
        "probability_to_turnout": abstentionist_turnout,
        "probability_to_vote_for_candidate": abstentionist_vote_for_candidate,
    }

    # Create list with all voter groups
    voters_groups = [
        eleitor_portugal_seguro,
        eleitor_portugal_ventura,
        eleitor_portugal_figueiredo,
        eleitor_portugal_gouveia_melo,
        eleitor_portugal_marques_mendes,
        eleitor_portugal_martins,
        eleitor_portugal_filipe,
        eleitor_portugal_vieira,
        eleitor_portugal_pinto,
        eleitor_portugal_silva,
        eleitor_portugal_correia,
        eleitor_portugal_abstencionista,
    ]

    return voters_groups


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
                group["probability_to_vote_for_candidate"],
            )
            total_votes_candidate_1 += votes
            total_votes_candidate_2 += turnout - votes
            total_turnout += turnout
        results.append(
            (total_votes_candidate_1, total_votes_candidate_2, total_turnout)
        )
    return results


def create_scenario(voters_groups, n_simulations=10000):
    results_scenario = simulate_second_round(voters_groups, n_simulations=n_simulations)
    results_scenario_df = pd.DataFrame(
        results_scenario, columns=["Ventura", "Seguro", "Turnout"]
    )
    results_scenario_df["Ventura_Wins"] = (
        results_scenario_df["Ventura"] > results_scenario_df["Seguro"]
    )

    return results_scenario_df
