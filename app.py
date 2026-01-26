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
confidence_to_k = {
        "Muito incerto": 4,
        "Incerto": 10,
        "Confiante": 20,
        "Muito confiante": 50,
    }

voter_groups = create_voter_group(
    seguro_turnout=st.sidebar.slider(
        "Seguro - Probabilidade de Votação (%)", 0, 100, 100
    ),
    seguro_turnout_confidence=st.sidebar.slider(
        "Seguro - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    seguro_vote_for_candidate=st.sidebar.slider(
        "Seguro - Probabilidade de Votar no Ventura (%)", 0, 100, 0
    ),
    seguro_vote_for_candidate_confidence=st.sidebar.slider(
        "Seguro - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    ventura_turnout=st.sidebar.slider(
        "Ventura - Probabilidade de Votação (%)", 0, 100, 100
    ),
    ventura_turnout_confidence=st.sidebar.slider(
        "Ventura - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    ventura_vote_for_candidate=st.sidebar.slider(
        "Ventura - Probabilidade de Votar no Ventura (%)", 0, 100, 100
    ),
    ventura_vote_for_candidate_confidence=st.sidebar.slider(
        "Ventura - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    figueiredo_turnout=st.sidebar.slider(
        "Figueiredo - Probabilidade de Votação (%)", 0, 100, 50
    ),
    figueiredo_turnout_confidence=st.sidebar.slider(
        "Figueiredo - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    figueiredo_vote_for_candidate=st.sidebar.slider(
        "Figueiredo - Probabilidade de Votar no Ventura (%)", 0, 100, 100
    ),
    figueiredo_vote_for_candidate_confidence=st.sidebar.slider(
        "Figueiredo - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    gouveia_melo_turnout=st.sidebar.slider(
        "Gouveia Melo - Probabilidade de Votação (%)", 0, 100, 100
    ),
    gouveia_melo_turnout_confidence=st.sidebar.slider(
        "Gouveia Melo - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    gouveira_melo_vote_for_candidate=st.sidebar.slider(
        "Gouveia Melo - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    gouveia_melo_vote_for_candidate_confidence=st.sidebar.slider(
        "Gouveia Melo - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    marques_mendes_turnout=st.sidebar.slider(
        "Marques Mendes - Probabilidade de Votação (%)", 0, 100, 100
    ),
    marques_mendes_turnout_confidence=st.sidebar.slider(
        "Marques Mendes - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    marques_mendes_vote_for_candidate=st.sidebar.slider(
        "Marques Mendes - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    marques_mendes_vote_for_candidate_confidence=st.sidebar.slider(
        "Marques Mendes - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    martins_turnout=st.sidebar.slider(
        "Martins - Probabilidade de Votação (%)", 0, 100, 100
    ),
    martins_turnout_confidence=st.sidebar.slider(
        "Martins - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    martins_vote_for_candidate=st.sidebar.slider(
        "Martins - Probabilidade de Votar no Ventura (%)", 0, 100, 0
    ),
    martins_vote_for_candidate_confidence=st.sidebar.slider(
        "Martins - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    filipe_turnout=st.sidebar.slider(
        "Filipe - Probabilidade de Votação (%)",  0, 100, 100
    ),
    filipe_turnout_confidence=st.sidebar.slider(
        "Filipe - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    filipe_vote_for_candidate=st.sidebar.slider(
        "Filipe - Probabilidade de Votar no Ventura (%)", 0, 100, 0
    ),
    filipe_vote_for_candidate_confidence=st.sidebar.slider(
        "Filipe - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    vieira_turnout=st.sidebar.slider(
        "Vieira - Probabilidade de Votação (%)", 0, 100, 100
    ),
    vieira_turnout_confidence=st.sidebar.slider(
        "Vieira - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    vieira_vote_for_candidate=st.sidebar.slider(
        "Vieira - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    vieira_vote_for_candidate_confidence=st.sidebar.slider(
        "Vieira - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    pinto_vote_turnout=st.sidebar.slider(
        "Pinto - Probabilidade de Votação (%)", 0, 100, 100
    ),
    pinto_turnout_confidence=st.sidebar.slider(
        "Pinto - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    pinto_vote_for_candidate=st.sidebar.slider(
        "Pinto - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    pinto_vote_for_candidate_confidence=st.sidebar.slider(
        "Pinto - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    silva_turnout=st.sidebar.slider(
        "Silva - Probabilidade de Votação (%)",  0, 100, 100
    ),
    silva_turnout_confidence=st.sidebar.slider(
        "Silva - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    silva_vote_for_candidate=st.sidebar.slider(
        "Silva - Probabilidade de Votar no Ventura (%)",  0, 100, 100
    ),
    silva_vote_for_candidate_confidence=st.sidebar.slider(
        "Silva - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    correia_turnout=st.sidebar.slider(
        "Correia - Probabilidade de Votação (%)",  0, 100, 100
    ),
    correia_turnout_confidence=st.sidebar.slider(
        "Correia - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    correia_vote_for_candidate=st.sidebar.slider(
        "Correia - Probabilidade de Votar no Ventura (%)",  0, 100, 50
    ),
    correia_vote_for_candidate_confidence=st.sidebar.slider(
        "Correia - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    abstentionist_turnout=st.sidebar.slider(
        "Abstenção - Probabilidade de Votação (%)",  0, 100, 50
    ),
    abstentionist_turnout_confidence=st.sidebar.slider(
        "Abstenção - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
    abstentionist_vote_for_candidate=st.sidebar.slider(
        "Abstenção - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    abstentionist_vote_for_candidate_confidence=st.sidebar.slider(
        "Abstenção - Está confiante nesta probabilidade?",
        options=list(confidence_to_k.keys()),
        value="Confiante",
    ),
)
# Add maximum abstention selector
max_abstention = st.sidebar.slider(
    "Abstenção Máxima (%)", 0, 100, 30
) / 100
max_difference = st.sidebar.slider(
    "Diference Máxima Entre Candidatos (Pontos Percentuais)", 0, 100, 30
) / 100

# Add OK button to trigger simulation
if st.sidebar.button("OK", key="run_button"):
    st.session_state.run_simulation = True

# Only run simulation if OK button was pressed
if st.session_state.run_simulation:
    scenario_results = create_scenario(
        voter_groups,
        max_abstention=max_abstention,
        max_difference=max_difference,
                                       )
    
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

