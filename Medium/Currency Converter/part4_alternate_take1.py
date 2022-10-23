# I DID NOT DO THE MODULES FOR THE DICTIONARY SO I DID NOT KNOW TO USE THEM. I WISH I HAD DONE IT FIRST.

exchange_rate = {'RUB': {'name': 'RUB', 'one_conicoin': 2.98},
                 'ARS': {'name': 'ARS', 'one_conicoin': 0.82},
                 'HNL': {'name': 'HNL', 'one_conicoin': 0.17},
                 'AUD': {'name': 'AUD', 'one_conicoin': 1.9622},
                 'MAD': {'name': 'MAD', 'one_conicoin': 0.208}}

conicoins = float(input())
for coins in exchange_rate:
    print(f"I will get {round(exchange_rate[coins]['one_conicoin'] * conicoins, 2)} {exchange_rate[coins]['name']} from the sale of {conicoins} conicoins.")