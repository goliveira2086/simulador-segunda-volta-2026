import streamlit as st
import numpy as np
import pandas as pd
from modules.voters_functions import create_voter_group, create_scenario

st.title("Simular Segunda Volta Eleitoral")

st.sidebar.header("Parâmetros da Simulação")
st.text("Ajuste os parâmetros abaixo para simular diferentes cenários eleitorais.")

# Create voter groups
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
        "Martins - Probabilidade de Votação", 0.25, 0.75, 0.4285714285714286
    ),
    martins_vote_for_candidate=st.sidebar.slider(
        "Martins - Probabilidade de Votar no Candidato", 0.25, 0.75, 0.4285714285714286
    ),
    filipe_turnout=st.sidebar.slider(
        "Filipe - Probabilidade de Votação", 0.25, 0.75, 0.4285714285714286
    ),
    filipe_vote_for_candidate=st.sidebar.slider(
        "Filipe - Probabilidade de Votar no Candidato", 0.25, 0.75, 0.4285714285714286
    ),
    vieira_turnout=st.sidebar.slider(
        "Vieira - Probabilidade de Votação", 0.25, 0.75, 0.4285714285714286
    ),
    vieira_vote_for_candidate=st.sidebar.slider(
        "Vieira - Probabilidade de Votar no Candidato", 0.25, 0.75, 0.4285714285714286
    ),
    pinto_vote_turnout=st.sidebar.slider(
        "Pinto - Probabilidade de Votação",
        0.3333333333333333,
        0.6666666666666666,
        0.4999999999999999,
    ),  # Adjusted to match the original value
    pinto_vote_for_candidate=st.sidebar.slider(
        "Pinto - Probabilidade de Votar no Candidato",
        0.333333333333333,
        0.666666666,
        0.49999999,
    ),  # Adjusted to match the original value
    silva_turnout=st.sidebar.slider(
        "Silva - Probabilidade de Votação", 0.2, 0.8, 0.4
    ),  # Adjusted to match the original value
    silva_vote_for_candidate=st.sidebar.slider(
        "Silva - Probabilidade de Votar no Candidato", 0.2, 0.8, 0.4
    ),  # Adjusted to match the original value
    correia_turnout=st.sidebar.slider(
        "Correia - Probabilidade de Votação", 0.2, 0.8, 0.4
    ),  # Adjusted to match the original value
    correia_vote_for_candidate=st.sidebar.slider(
        "Correia - Probabilidade de Votar no Candidato", 0.2, 0.8, 0.4
    ),  # Adjusted to match the original value
    abstentionist_turnout=st.sidebar.slider(
        "Abstenção - Probabilidade de Votação", 0.0, 1.0, 0.0
    ),
    abstentionist_vote_for_candidate=st.sidebar.slider(
        "Abstenção - Probabilidade de Votar no Candidato", 0.0, 1.0, 0.0
    ),
)

# Create scenario based on voter groups
scenario_results = create_scenario(voter_groups)

st.header("Resultados da Simulação")
st.subheader("Votos por Candidato")
st.write(scenario_results.describe())
st.subheader("Probabilidade de Ventura Vencer")
st.write(f"{scenario_results["Ventura_Wins"].mean() * 100:.2f}%")
