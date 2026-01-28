from matplotlib.pylab import beta
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_voter_group(
    seguro_turnout,
    seguro_turnout_confidence,
    seguro_vote_for_candidate,
    seguro_vote_for_candidate_confidence,
    ventura_turnout,
    ventura_turnout_confidence,
    ventura_vote_for_candidate,
    ventura_vote_for_candidate_confidence,
    figueiredo_turnout,
    figueiredo_turnout_confidence,
    figueiredo_vote_for_candidate,
    figueiredo_vote_for_candidate_confidence,
    gouveia_melo_turnout,
    gouveia_melo_turnout_confidence,
    gouveia_melo_vote_for_candidate,
    gouveia_melo_vote_for_candidate_confidence,
    marques_mendes_turnout,
    marques_mendes_turnout_confidence,
    marques_mendes_vote_for_candidate,
    marques_mendes_vote_for_candidate_confidence,
    martins_turnout,
    martins_turnout_confidence,
    martins_vote_for_candidate,
    martins_vote_for_candidate_confidence,
    filipe_turnout,
    filipe_turnout_confidence,
    filipe_vote_for_candidate,
    filipe_vote_for_candidate_confidence,
    vieira_turnout,
    vieira_turnout_confidence,
    vieira_vote_for_candidate,
    vieira_vote_for_candidate_confidence,
    pinto_vote_turnout,
    pinto_turnout_confidence,
    pinto_vote_for_candidate,
    pinto_vote_for_candidate_confidence,
    silva_turnout,
    silva_turnout_confidence,
    silva_vote_for_candidate,
    silva_vote_for_candidate_confidence,
    correia_turnout,
    correia_turnout_confidence,
    correia_vote_for_candidate,
    correia_vote_for_candidate_confidence,
    abstentionist_turnout,
    abstentionist_turnout_confidence,
    abstentionist_vote_for_candidate,
    abstentionist_vote_for_candidate_confidence,
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
        "probability_to_turnout_confidence": seguro_turnout_confidence,
        "probability_to_vote_for_candidate": seguro_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": seguro_vote_for_candidate_confidence,
    }
    eleitor_portugal_ventura = {
        "first_turn_votes": 1297533 + 29115,
        "probability_to_turnout": ventura_turnout,
        "probability_to_turnout_confidence": ventura_turnout_confidence,
        "probability_to_vote_for_candidate": ventura_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": ventura_vote_for_candidate_confidence,
    }
    eleitor_portugal_figueiredo = {
        "first_turn_votes": 891788 + 10783,
        "probability_to_turnout": figueiredo_turnout,
        "probability_to_turnout_confidence": figueiredo_turnout_confidence,
        "probability_to_vote_for_candidate": figueiredo_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": figueiredo_vote_for_candidate_confidence,
    }
    eleitor_portugal_gouveia_melo = {
        "first_turn_votes": 691489 + 3602,
        "probability_to_turnout": gouveia_melo_turnout,
        "probability_to_turnout_confidence": gouveia_melo_turnout_confidence,
        "probability_to_vote_for_candidate": gouveia_melo_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": gouveia_melo_vote_for_candidate_confidence,
    }
    eleitor_portugal_marques_mendes = {
        "first_turn_votes": 631809 + 5585,
        "probability_to_turnout": marques_mendes_turnout,
        "probability_to_turnout_confidence": marques_mendes_turnout_confidence,
        "probability_to_vote_for_candidate": marques_mendes_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": marques_mendes_vote_for_candidate_confidence,
    }
    eleitor_portugal_martins = {
        "first_turn_votes": 114468 + 1835,
        "probability_to_turnout": martins_turnout,
        "probability_to_turnout_confidence": martins_turnout_confidence,
        "probability_to_vote_for_candidate": martins_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": martins_vote_for_candidate_confidence,
    }
    eleitor_portugal_filipe = {
        "first_turn_votes": 91889 + 700,
        "probability_to_turnout": filipe_turnout,
        "probability_to_turnout_confidence": filipe_turnout_confidence,
        "probability_to_vote_for_candidate": filipe_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": filipe_vote_for_candidate_confidence,
    }
    eleitor_portugal_vieira = {
        "first_turn_votes": 60266 + 633,
        "probability_to_turnout": vieira_turnout,
        "probability_to_turnout_confidence": vieira_turnout_confidence,
        "probability_to_vote_for_candidate": vieira_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": vieira_vote_for_candidate_confidence,
    }
    eleitor_portugal_pinto = {
        "first_turn_votes": 37671 + 865,
        "probability_to_turnout": pinto_vote_turnout,
        "probability_to_turnout_confidence": pinto_turnout_confidence,
        "probability_to_vote_for_candidate": pinto_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": pinto_vote_for_candidate_confidence,
    }
    eleitor_portugal_silva = {
        "first_turn_votes": 10674 + 219,
        "probability_to_turnout": silva_turnout,
        "probability_to_turnout_confidence": silva_turnout_confidence,
        "probability_to_vote_for_candidate": silva_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": silva_vote_for_candidate_confidence,
    }
    eleitor_portugal_correia = {
        "first_turn_votes": 4594 + 28,
        "probability_to_turnout": correia_turnout,
        "probability_to_turnout_confidence": correia_turnout_confidence,
        "probability_to_vote_for_candidate": correia_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": correia_vote_for_candidate_confidence,
    }
    eleitor_portugal_abstencionista = {
        "first_turn_votes": portugal_abstentionists,
        "probability_to_turnout": abstentionist_turnout,
        "probability_to_turnout_confidence": abstentionist_turnout_confidence,
        "probability_to_vote_for_candidate": abstentionist_vote_for_candidate,
        "probability_to_vote_for_candidate_confidence": abstentionist_vote_for_candidate_confidence,
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
    nbr_voters_first_turn,
    probability_to_turnout,
    confidence_to_turnout,
    probability_to_vote_for_candidate,
    confidence_to_vote_for_candidate,
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
    # Confidence dictionary
    confidence_to_k = {
        "Muito incerto": 4,
        "Incerto": 10,
        "Confiante": 20,
        "Muito confiante": 50,
    }
        
    # Simulate turnout
    alpha = 0.0001 + probability_to_turnout * confidence_to_k[confidence_to_turnout]
    beta = 0.0001 + (1-probability_to_turnout) * confidence_to_k[confidence_to_turnout]
    actual_probability_to_turnout = np.random.beta(alpha, beta, size=1)[0]
    turnout = np.random.binomial(nbr_voters_first_turn, actual_probability_to_turnout)

    # Simulate votes for the candidate
    alpha = 0.0001 + probability_to_vote_for_candidate * confidence_to_k[confidence_to_vote_for_candidate]
    beta = 0.0001 + (1-probability_to_vote_for_candidate) * confidence_to_k[confidence_to_vote_for_candidate]
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
                group["probability_to_turnout"] / 100,
                group["probability_to_turnout_confidence"],
                group["probability_to_vote_for_candidate"] / 100,
                group["probability_to_vote_for_candidate_confidence"],
            )
            total_votes_candidate_1 += votes
            total_votes_candidate_2 += turnout - votes
            total_turnout += turnout
        results.append(
            (total_votes_candidate_1, total_votes_candidate_2, total_turnout)
        )
    return results


def create_scenario(
    voters_groups, max_abstention=0.3, max_difference=0.1, n_simulations=10000
):
    results_scenario = simulate_second_round(voters_groups, n_simulations=n_simulations)
    results_scenario_df = pd.DataFrame(
        results_scenario, columns=["Ventura", "Seguro", "Votantes"]
    )
    results_scenario_df["Ventura vence!"] = (
        results_scenario_df["Ventura"] > results_scenario_df["Seguro"]
    )

    # Apply maximum abstention filter
    portugal_all_voters = 9262653 + 1754549
    results_scenario_df["Abstenção"] = 1 - (
        results_scenario_df["Votantes"] / portugal_all_voters
    )
    id_flag = results_scenario_df["Abstenção"] <= max_abstention
    results_scenario_df = results_scenario_df.loc[id_flag, :].reset_index(drop=True)

    # Maximum difference filter
    results_scenario_df["Diferença relativa"] = abs(
        results_scenario_df["Ventura"] - results_scenario_df["Seguro"]
    ) / (results_scenario_df["Ventura"] + results_scenario_df["Seguro"])
    id_flag = results_scenario_df["Diferença relativa"] <= max_difference
    results_scenario_df = results_scenario_df.loc[id_flag, :].reset_index(drop=True)

    return results_scenario_df


def plot_scenario_distribution(scenario_results):
    """
    Create a KDE plot showing the distribution of the difference between Ventura and Seguro votes.

    Parameters:
    scenario_results (pd.DataFrame): DataFrame with columns ['Ventura', 'Seguro', 'Turnout']
    """
    # Calculate the difference (Ventura - Seguro)
    difference = scenario_results["Ventura"] - scenario_results["Seguro"]
    
    # Convert to millions
    difference_millions = difference / 1000000

    # Create the KDE plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(
        data=difference_millions,
        fill=True,
        ax=ax,
        color="steelblue"
    )

    plt.title("Distribuição da Diferença de Votos")
    plt.xlabel("Diferença de Votos (milhões)")
    plt.ylabel("Probabilidade")
    
    # Add vertical line at x=0
    plt.axvline(x=0, color='red', linestyle='--', linewidth=2, label='Diferença = 0')
    
    # Get y-axis limits to position text
    y_max = ax.get_ylim()[1]
    
    # Add text annotations
    ax.text(1, y_max * 0.9, 'Ventura\nmais votos →', 
        fontsize=10, ha='left', color='green', weight='bold')
    ax.text(-1, y_max * 0.9, '← Seguro\nmais votos', 
        fontsize=10, ha='right', color='blue', weight='bold')

    # Ensure symmetric x-limits around zero so 0 is always a tick
    x_min, x_max = ax.get_xlim()
    max_abs = max(abs(x_min), abs(x_max))
    # Set symmetric limits
    ax.set_xlim(-max_abs, max_abs)

    # Create symmetric ticks (odd number ensures 0 is included)
    ticks = np.linspace(-max_abs, max_abs, 11)
    # Display absolute values on the ticks
    tick_labels = [f'{abs(tick):.1f}' for tick in ticks]
    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels)

    plt.tight_layout()

    return fig