from matplotlib.pylab import beta
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
        "first_turn_votes": 1738741 + 16163,
        "probability_to_turnout": seguro_turnout,
        "probability_to_vote_for_candidate": seguro_vote_for_candidate,
    }
    eleitor_portugal_ventura = {
        "first_turn_votes": 1297533 + 29115,
        "probability_to_turnout": ventura_turnout,
        "probability_to_vote_for_candidate": ventura_vote_for_candidate,
    }
    eleitor_portugal_figueiredo = {
        "first_turn_votes": 891788 + 10783,
        "probability_to_turnout": figueiredo_turnout,
        "probability_to_vote_for_candidate": figueiredo_vote_for_candidate,
    }
    eleitor_portugal_gouveia_melo = {
        "first_turn_votes": 691489 + 3602,
        "probability_to_turnout": gouveia_melo_turnout,
        "probability_to_vote_for_candidate": gouveira_melo_vote_for_candidate,
    }
    eleitor_portugal_marques_mendes = {
        "first_turn_votes": 631809 + 5585,
        "probability_to_turnout": marques_mendes_turnout,
        "probability_to_vote_for_candidate": marques_mendes_vote_for_candidate,
    }
    eleitor_portugal_martins = {
        "first_turn_votes": 114468 + 1835,
        "probability_to_turnout": martins_turnout,
        "probability_to_vote_for_candidate": martins_vote_for_candidate,
    }
    eleitor_portugal_filipe = {
        "first_turn_votes": 91889 + 700,
        "probability_to_turnout": filipe_turnout,
        "probability_to_vote_for_candidate": filipe_vote_for_candidate,
    }
    eleitor_portugal_vieira = {
        "first_turn_votes": 60266 + 633,
        "probability_to_turnout": vieira_turnout,
        "probability_to_vote_for_candidate": vieira_vote_for_candidate,
    }
    eleitor_portugal_pinto = {
        "first_turn_votes": 37671 + 865,
        "probability_to_turnout": pinto_vote_turnout,
        "probability_to_vote_for_candidate": pinto_vote_for_candidate,
    }
    eleitor_portugal_silva = {
        "first_turn_votes": 10674 + 219,
        "probability_to_turnout": silva_turnout,
        "probability_to_vote_for_candidate": silva_vote_for_candidate,
    }
    eleitor_portugal_correia = {
        "first_turn_votes": 4594 + 28,
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

def calculate_beta_parameters(mean, std_dev):
    """
    Calculate alpha and beta parameters of a beta distribution from mean and standard deviation.
    
    Parameters:
    mean (float): Mean of the beta distribution (between 0 and 1).
    std_dev (float): Standard deviation of the beta distribution.
    
    Returns:
    tuple: (alpha, beta) parameters for the beta distribution.
    """
    if mean <= 0 or mean >= 1:
        raise ValueError("Mean must be between 0 and 1")
    
    # Variance from standard deviation
    variance = std_dev ** 2
    
    # Beta distribution relationships:
    # mean = alpha / (alpha + beta)
    # variance = (alpha * beta) / ((alpha + beta)^2 * (alpha + beta + 1))
    
    # Solving for alpha and beta:
    temp = (mean * (1 - mean) / variance) - 1
    alpha = mean * temp
    beta = (1 - mean) * temp
    
    return alpha, beta


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
    adjusted_probability_to_turnout = np.where(probability_to_turnout <= 0, 0.001, probability_to_turnout)
    adjusted_probability_to_turnout = np.where(adjusted_probability_to_turnout >= 1, 0.999, adjusted_probability_to_turnout)
    alpha, beta = calculate_beta_parameters(
        mean=adjusted_probability_to_turnout,
        std_dev=adjusted_probability_to_turnout * 0.1,
        )
    actual_probability_to_turnout = np.random.beta(alpha, beta, size=1)[0]
    turnout = np.random.binomial(nbr_voters_first_turn, actual_probability_to_turnout)

    # Simulate votes for the candidate
    adjusted_probability_to_vote_for_candidate = np.where(probability_to_vote_for_candidate <= 0, 0.001, probability_to_vote_for_candidate)
    adjusted_probability_to_vote_for_candidate = np.where(adjusted_probability_to_vote_for_candidate >= 1, 0.999, adjusted_probability_to_vote_for_candidate)
    alpha, beta = calculate_beta_parameters(
        mean=adjusted_probability_to_vote_for_candidate,
        std_dev=adjusted_probability_to_vote_for_candidate * 0.1,
        )
    actual_probability_to_vote_for_candidate = np.random.beta(alpha, beta, size=1)[0]
    votes = np.random.binomial(turnout, actual_probability_to_vote_for_candidate)

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
