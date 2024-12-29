def calculer_taille_lot(capital, risque_pourcentage, stop_loss_pips, valeur_par_pip):
    """
    Calcule la taille de lot pour un trade Forex.
    
    :param capital: Capital total en euros.
    :param risque_pourcentage: Pourcentage de risque sur le capital (ex: 1% = 0.01).
    :param stop_loss_pips: Distance du stop-loss en pips.
    :param valeur_par_pip: Valeur d'un pip pour 1 lot (en euros).
    :return: Taille de lot recommandée.
    """
    # Calcul du risque en euros
    risque_total = capital * risque_pourcentage
    
    # Taille du lot
    taille_lot = risque_total / (stop_loss_pips * valeur_par_pip)
    return taille_lot

def calculer_valeur_pip(pair, taux_change, taille_lot, devise_compte, taux_conversion=1.0):
    """
    Calcule la valeur d'un pip en fonction de la paire de devises et de la taille du lot.
    
    :param pair: La paire de devises tradée (ex: 'EUR/USD', 'USD/JPY').
    :param taux_change: Le taux de change actuel de la paire.
    :param taille_lot: Taille du lot (ex: 100000 pour 1 lot standard).
    :param devise_compte: Devise de ton compte (ex: 'EUR', 'USD').
    :param taux_conversion: Taux de conversion entre la devise cotée et la devise de compte (par défaut 1 si identique).
    :return: Valeur d'un pip dans la devise du compte.
    """
    if "JPY" in pair:
        pip = 0.01  # Pour les paires avec le JPY
    else:
        pip = 0.0001  # Pour les autres paires

    # Calcul de la valeur d’un pip en devise cotée
    valeur_pip_devise_cotee = (pip / taux_change) * taille_lot

    # Conversion dans la devise de compte si nécessaire
    valeur_pip_devise_compte = valeur_pip_devise_cotee * taux_conversion

    return valeur_pip_devise_compte


# Paramètres d'exemple
pair = "EUR/USD"          # Paire tradée
taux_change = 1.04266      # Taux de change actuel
taille_lot = 100000       # Taille du lot (1 lot standard)
devise_compte = "EUR"     # Devise de ton compte
taux_conversion = 1.0     # Conversion EUR/USD (1 si même devise)

# Calcul de la valeur d’un pip
valeur_pip = calculer_valeur_pip(pair, taux_change, taille_lot, devise_compte, taux_conversion)

print(f"La valeur d'un pip pour {pair} avec {taille_lot} unités est de {valeur_pip:.2f} {devise_compte}.")


# Paramètres de l'exemple
capital = 100000  # Capital total en euros
risque_pourcentage = 0.01  # 1% de risque
stop_loss_pips = 30  # Stop-loss à 50 pips
valeur_par_pip = valeur_pip  # Valeur d'un pip pour 1 lot (EUR/USD)

# Calcul
taille_lot = calculer_taille_lot(capital, risque_pourcentage, stop_loss_pips, valeur_par_pip)

print(f"Taille de lot recommandée : {taille_lot:.2f} lot(s)")

