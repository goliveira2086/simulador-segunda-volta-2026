import streamlit as st
import numpy as np
import pandas as pd
from modules.voters_functions import create_voter_group, create_scenario, plot_scenario_distribution

st.title("Bem vindo ao Simulador da segunda volta das Presidenciais de 2026!")

st.text(
    """
🎯 Objetivo do simulador
Este dashboard permite explorar cenários possíveis para a segunda volta das eleições presidenciais portuguesas de 2026. Através de probabilidades fornecidas pelo utilizador, o modelo simula a noite eleitoral 1000 vezes!

📊 Resultados apresentados
- A probabilidade de vitória de cada um.
- A distribuição de votos de cada candidato.

🛠️ Como usar o simulador

A magia acontece na barra lateral esquerda, onde o utilizador pode definir os parâmetros da simulação. Quando estiver satisfeito com as suas escolhas, basta pressionar o botão "OK" para executar a simulação.

A simulação parte dos o número de pessoas que votaram em cada candidato da primeira volta.
Para cada candidato da primeira volta, o dashboard deixa o utilizador definir:
- A probabilidade de esses eleitores voltarem a votar na segunda volta.
- A probabilidade de escolherem André Ventura na segunda volta.
- Para cada uma destas probabilidades, o utilizador pode definir o grau de confiança que tem na sua estimativa (quanto mais confiante, menor a variação em torno da probabilidade definida).

Além disso, o utilizador pode definir:
- Quantos abstencionistas da primeira volta irão votar na segunda.
- Qual a probabilidade de esses novos votantes escolherem André Ventura.
- O nível máximo de abstenção na segunda volta.
- A diferença máxima aceitável entre os dois candidatos (em pontos percentuais).

📈 Como interpretar os resultados
- Probabilidade de vitória: percentagem de simulações em que cada candidato vence.
- Distribuição da diferença de votos: mostra a variabilidade possível dada a incerteza introduzida.
- Impacto dos parâmetros: pequenas alterações nas probabilidades podem gerar grandes mudanças, especialmente quando a confiança é baixa

    """
    )
st.sidebar.header("Parâmetros do simulador")

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
    seguro_turnout_confidence=st.sidebar.selectbox(
        "Seguro - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="seguro_turnout_confidence",
    ),
    seguro_vote_for_candidate=st.sidebar.slider(
        "Seguro - Probabilidade de Votar no Ventura (%)", 0, 100, 0
    ),
    seguro_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Seguro - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="seguro_vote_for_candidate_confidence",
    ),
    ventura_turnout=st.sidebar.slider(
        "Ventura - Probabilidade de Votação (%)", 0, 100, 100
    ),
    ventura_turnout_confidence=st.sidebar.selectbox(
        "Ventura - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="ventura_turnout_confidence"
    ),
    ventura_vote_for_candidate=st.sidebar.slider(
        "Ventura - Probabilidade de Votar no Ventura (%)", 0, 100, 100
    ),
    ventura_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Ventura - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="ventura_vote_for_candidate_confidence"
    ),
    figueiredo_turnout=st.sidebar.slider(
        "Figueiredo - Probabilidade de Votação (%)", 0, 100, 50
    ),
    figueiredo_turnout_confidence=st.sidebar.selectbox(
        "Figueiredo - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="figueiredo_turnout_confidence"
    ),
    figueiredo_vote_for_candidate=st.sidebar.slider(
        "Figueiredo - Probabilidade de Votar no Ventura (%)", 0, 100, 100
    ),
    figueiredo_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Figueiredo - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="figueiredo_vote_for_candidate_confidence"
    ),
    gouveia_melo_turnout=st.sidebar.slider(
        "Gouveia Melo - Probabilidade de Votação (%)", 0, 100, 100
    ),
    gouveia_melo_turnout_confidence=st.sidebar.selectbox(
        "Gouveia Melo - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="gouveia_melo_turnout_confidence"
    ),
    gouveia_melo_vote_for_candidate=st.sidebar.slider(
        "Gouveia Melo - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    gouveia_melo_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Gouveia Melo - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="gouveia_melo_vote_for_candidate_confidence"
    ),
    marques_mendes_turnout=st.sidebar.slider(
        "Marques Mendes - Probabilidade de Votação (%)", 0, 100, 100
    ),
    marques_mendes_turnout_confidence=st.sidebar.selectbox(
        "Marques Mendes - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="marques_mendes_turnout_confidence"
    ),
    marques_mendes_vote_for_candidate=st.sidebar.slider(
        "Marques Mendes - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    marques_mendes_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Marques Mendes - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="marques_mendes_vote_for_candidate_confidence"
    ),
    martins_turnout=st.sidebar.slider(
        "Martins - Probabilidade de Votação (%)", 0, 100, 100
    ),
    martins_turnout_confidence=st.sidebar.selectbox(
        "Martins - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="martins_turnout_confidence"
    ),
    martins_vote_for_candidate=st.sidebar.slider(
        "Martins - Probabilidade de Votar no Ventura (%)", 0, 100, 0
    ),
    martins_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Martins - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="martins_vote_for_candidate_confidence"
    ),
    filipe_turnout=st.sidebar.slider(
        "Filipe - Probabilidade de Votação (%)",  0, 100, 100
    ),
    filipe_turnout_confidence=st.sidebar.selectbox(
        "Filipe - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="filipe_turnout_confidence"
    ),
    filipe_vote_for_candidate=st.sidebar.slider(
        "Filipe - Probabilidade de Votar no Ventura (%)", 0, 100, 0
    ),
    filipe_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Filipe - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="filipe_vote_for_candidate_confidence"
    ),
    vieira_turnout=st.sidebar.slider(
        "Vieira - Probabilidade de Votação (%)", 0, 100, 100
    ),
    vieira_turnout_confidence=st.sidebar.selectbox(
        "Vieira - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="vieira_turnout_confidence"
    ),
    vieira_vote_for_candidate=st.sidebar.slider(
        "Vieira - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    vieira_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Vieira - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="vieira_vote_for_candidate_confidence"
    ),
    pinto_vote_turnout=st.sidebar.slider(
        "Pinto - Probabilidade de Votação (%)", 0, 100, 100
    ),
    pinto_turnout_confidence=st.sidebar.selectbox(
        "Pinto - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="pinto_turnout_confidence"
    ),
    pinto_vote_for_candidate=st.sidebar.slider(
        "Pinto - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    pinto_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Pinto - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="pinto_vote_for_candidate_confidence"
    ),
    silva_turnout=st.sidebar.slider(
        "Silva - Probabilidade de Votação (%)",  0, 100, 100
    ),
    silva_turnout_confidence=st.sidebar.selectbox(
        "Silva - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="silva_turnout_confidence"
    ),
    silva_vote_for_candidate=st.sidebar.slider(
        "Silva - Probabilidade de Votar no Ventura (%)",  0, 100, 100
    ),
    silva_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Silva - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="silva_vote_for_candidate_confidence"
    ),
    correia_turnout=st.sidebar.slider(
        "Correia - Probabilidade de Votação (%)",  0, 100, 100
    ),
    correia_turnout_confidence=st.sidebar.selectbox(
        "Correia - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="correia_turnout_confidence"
    ),
    correia_vote_for_candidate=st.sidebar.slider(
        "Correia - Probabilidade de Votar no Ventura (%)",  0, 100, 50
    ),
    correia_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Correia - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="correia_vote_for_candidate_confidence"
    ),
    abstentionist_turnout=st.sidebar.slider(
        "Abstenção - Probabilidade de Votação (%)",  0, 100, 50
    ),
    abstentionist_turnout_confidence=st.sidebar.selectbox(
        "Abstenção - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="abstentionist_turnout_confidence"
    ),
    abstentionist_vote_for_candidate=st.sidebar.slider(
        "Abstenção - Probabilidade de Votar no Ventura (%)", 0, 100, 50
    ),
    abstentionist_vote_for_candidate_confidence=st.sidebar.selectbox(
        "Abstenção - Está confiante nesta probabilidade?",
        list(confidence_to_k.keys()), key="abstentionist_vote_for_candidate_confidence"
    ),
)

# Add maximum abstention selector
max_abstention = st.sidebar.slider(
    "Abstenção Máxima (%)", 0, 100, 30
) / 100
max_difference = st.sidebar.slider(
    "Diference máxima entre os candidatos (Pontos Percentuais)", 0, 100, 30
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

    st.subheader("Probabilidade de cada candidato vencer")
    st.write(f"Seguro: {(1-scenario_results["Ventura vence!"].mean()) * 100:.2f}%")
    st.write(f"Ventura: {scenario_results["Ventura vence!"].mean() * 100:.2f}%")
    
    st.subheader("Diferença de votos por Candidato")
    fig_1 = plot_scenario_distribution(scenario_results)
    st.pyplot(fig_1)
    
    st.session_state.run_simulation = False
else:
    st.info("Ajuste os parâmetros e pressione OK para executar a simulação.")