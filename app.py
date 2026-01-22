import streamlit as st
import numpy as np
import pandas as pd
from modules.voters_functions import create_voter_group, create_scenario, plot_scenario_correlation, plot_scenario_distribution

st.title("Simular Segunda Volta Eleitoral")

st.sidebar.header("Parâmetros da Simulação")
st.text("Ajuste os parâmetros abaixo para simular diferentes cenários eleitorais. Quando estiver pronto, pressione OK.")

# Initialize session state to track if we should run the simulation
if "run_simulation" not in st.session_state:
    st.session_state.run_simulation = False

# Collect parameters
voter_groups = create_voter_group(
    seguro_turnout=st.sidebar.slider(
        "Seguro - Probabilidade de Votação", 0.0, 1.0, 0.7
    ),
    seguro_vote_for_candidate=st.sidebar.slider(
        "Seguro - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
    ventura_turnout=st.sidebar.slider(
        "Ventura - Probabilidade de Votação", 0.0, 1.0, 0.7
    ),
    ventura_vote_for_candidate=st.sidebar.slider(
        "Ventura - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
    figueiredo_turnout=st.sidebar.slider(
        "Figueiredo - Probabilidade de Votação", 0.0, 1.0, 0.7
    ),
    figueiredo_vote_for_candidate=st.sidebar.slider(
        "Figueiredo - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
    gouveia_melo_turnout=st.sidebar.slider(
        "Gouveia Melo - Probabilidade de Votação", 0.0, 1.0, 0.7
    ),
    gouveira_melo_vote_for_candidate=st.sidebar.slider(
        "Gouveia Melo - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
    marques_mendes_turnout=st.sidebar.slider(
        "Marques Mendes - Probabilidade de Votação", 0.0, 1.0, 0.7
    ),
    marques_mendes_vote_for_candidate=st.sidebar.slider(
        "Marques Mendes - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
    martins_turnout=st.sidebar.slider(
        "Martins - Probabilidade de Votação", 0.0, 1.0, 0.5
    ),
    martins_vote_for_candidate=st.sidebar.slider(
        "Martins - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
    filipe_turnout=st.sidebar.slider(
        "Filipe - Probabilidade de Votação",  0.0, 1.0, 0.5
    ),
    filipe_vote_for_candidate=st.sidebar.slider(
        "Filipe - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
    vieira_turnout=st.sidebar.slider(
        "Vieira - Probabilidade de Votação", 0.0, 1.0, 0.5
    ),
    vieira_vote_for_candidate=st.sidebar.slider(
        "Vieira - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
    pinto_vote_turnout=st.sidebar.slider(
        "Pinto - Probabilidade de Votação", 0.0, 1.0, 0.5
    ),  # Adjusted to match the original value
    pinto_vote_for_candidate=st.sidebar.slider(
        "Pinto - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),  # Adjusted to match the original value
    silva_turnout=st.sidebar.slider(
        "Silva - Probabilidade de Votação",  0.0, 1.0, 0.5
    ),  # Adjusted to match the original value
    silva_vote_for_candidate=st.sidebar.slider(
        "Silva - Probabilidade de Votar no Candidato",  0.0, 1.0, 0.5
    ),  # Adjusted to match the original value
    correia_turnout=st.sidebar.slider(
        "Correia - Probabilidade de Votação",  0.0, 1.0, 0.5
    ),  # Adjusted to match the original value
    correia_vote_for_candidate=st.sidebar.slider(
        "Correia - Probabilidade de Votar no Candidato",  0.0, 1.0, 0.5
    ),  # Adjusted to match the original value
    abstentionist_turnout=st.sidebar.slider(
        "Abstenção - Probabilidade de Votação",  0.0, 1.0, 0.5
    ),
    abstentionist_vote_for_candidate=st.sidebar.slider(
        "Abstenção - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.5
    ),
)

# Add OK button to trigger simulation
if st.sidebar.button("OK", key="run_button"):
    st.session_state.run_simulation = True

# Only run simulation if OK button was pressed
if st.session_state.run_simulation:
    scenario_results = create_scenario(voter_groups)
    
    st.header("Resultados da Simulação")

    st.subheader("Probabilidade de Ventura Vencer")
    st.write(f"{scenario_results["Ventura vence!"].mean() * 100:.2f}%")
    
    st.subheader("Votos por Candidato")
    fig_1 = plot_scenario_distribution(scenario_results)
    st.pyplot(fig_1)

    fig_2 = plot_scenario_correlation(scenario_results)
    st.pyplot(fig_2)
    
    st.session_state.run_simulation = False
else:
    st.info("Ajuste os parâmetros e pressione OK para executar a simulação.")

