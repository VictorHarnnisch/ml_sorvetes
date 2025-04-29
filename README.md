# ml_sorvetes
🍦 Modelo ML no Azure para prever vendas de sorvete baseado na temperatura.
# 🍦📊 Previsão de Vendas de Sorvete com Azure Machine Learning - Projeto Gelato Mágico

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte de um desafio prático, aplicando conceitos fundamentais de Machine Learning para resolver um problema de negócio do mundo real: a previsão de vendas de sorvetes.

O cenário proposto envolve a sorveteria fictícia **Gelato Mágico**, que busca otimizar sua produção diária de sorvetes. A quantidade de vendas está fortemente correlacionada com a temperatura ambiente, mas a falta de uma previsão precisa leva a desperdícios em dias de baixa demanda ou perda de vendas em dias de alta demanda.

Utilizando o **Azure Machine Learning**, este projeto visa construir um modelo preditivo que ajude a Gelato Mágico a estimar quantas unidades de sorvete serão vendidas com base na previsão de temperatura, permitindo um planejamento de produção mais eficiente, reduzindo custos e maximizando lucros.

## 🎯 Objetivos

O principal objetivo é desenvolver um **modelo de regressão preditiva** capaz de:

✅ **Treinar um modelo de Machine Learning** que aprenda a relação entre a temperatura do dia e o número de sorvetes vendidos.
✅ **Registrar e gerenciar o ciclo de vida do modelo** de forma organizada utilizando o **MLflow**.
✅ **Implementar o modelo treinado** para que possa realizar previsões em tempo real ou em lote, utilizando os recursos de *cloud computing* do Azure.
✅ **Criar um pipeline estruturado** no Azure Machine Learning para automatizar as etapas de treinamento e teste do modelo, garantindo a reprodutibilidade e facilitando futuras iterações.

## 🛠️ Tecnologias Utilizadas (Exemplo)

* **Cloud Platform:** Microsoft Azure
* **Serviço de ML:** Azure Machine Learning
* **Gerenciamento de Modelos:** MLflow
* **Linguagem:** Python
* **Bibliotecas Principais:** Scikit-learn, Pandas, NumPy (a depender da sua implementação)

## 🚀 Como Funciona (Visão Geral)

1.  **Coleta de Dados:** Utilização de dados históricos de vendas e temperatura (neste caso, pode ser um dataset simulado ou fornecido).
2.  **Pré-processamento:** Limpeza e preparação dos dados para o treinamento.
3.  **Treinamento do Modelo:** Escolha e treinamento de um algoritmo de regressão (ex: Regressão Linear, Árvore de Decisão, etc.).
4.  **Avaliação:** Verificação da performance do modelo com métricas apropriadas (ex: RMSE, MAE, R²).
5.  **Registro com MLflow:** Log de parâmetros, métricas e artefatos do modelo no Azure ML.
6.  **Deploy (Implementação):** Publicação do modelo como um serviço web (endpoint) no Azure para consumo.
7.  **Pipeline:** Criação de um fluxo automatizado no Azure ML para re-treinamento e avaliação contínua.


