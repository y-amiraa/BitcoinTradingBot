Bitcoin Trading Bot

This project is an automated trading bot developed in Python that implements a trend-following strategy for Bitcoin. The program uses the Yahoo Finance API to retrieve real-time market data and processes this information using object-oriented programming.

The bot operates by analyzing hourly closing prices. The execution logic compares the current price (retrieved via iloc[-1]) to the previous price (iloc[-2]). A buy signal is generated when the price increases if no position is currently open. Conversely, a sell signal is generated when the price decreases if the asset is already held. This internal state management prevents redundant orders and secures the transaction cycle.

The application also includes a visualization component using the Matplotlib library. At the end of the execution, the bot generates a chart displaying the price curve along with the specific market entry and exit points. This project requires the installation of pandas, yfinance, and matplotlib to function.

This script is a simulation tool for educational purposes and does not constitute financial advice.




Ce projet est un bot de trading automatisé développé en Python qui utilise une stratégie de suivi de tendance sur le Bitcoin. Le programme utilise l'API Yahoo Finance pour récupérer des données de marché en temps réel et traite ces informations via la programmation orientée objet.

Le fonctionnement repose sur l'analyse des prix de clôture toutes les heures. La logique d'exécution compare le prix actuel (récupéré via iloc[-1]) au prix précédent (iloc[-2]). Un signal d'achat est généré quand le prix augmente si aucune position n'est ouverte. Inversement, un signal de vente est généré quand le prix baisse si un actif est déjà détenu. Cette gestion d'état interne permet d'éviter les ordres redondants et de sécuriser le cycle de transaction.

L'application intègre également une partie visualisation avec la bibliothèque Matplotlib. À la fin de l'exécution, le bot génère un graphique affichant la courbe de prix ainsi que les points d'entrée et de sortie du marché. Ce projet nécessite l'installation des bibliothèques pandas, yfinance et matplotlib pour fonctionner.

Ce script est un outil de simulation à but éducatif et ne constitue pas un conseil en investissement.
