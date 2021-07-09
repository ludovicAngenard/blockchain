# blockchain

## Prérequis
Installation de Python 3 ou supérieur
Besoin de la bibliothèque :
  * json
  * os
  * hashlib
Si besoin utilisez la commande ```pip install <nom de la bibliothèque>```

## Contenu

Dans le cadre d'une blockchain, des utilisateurs (Wallet) peuvent être instanciés ainsi qu'une chaine (Chaine). Vous pouvez donc échanger des tokens grâces à des transactions. Les blocks sont liés entre eux et contiennent les transactions. La taille maximale d'un block est de 256000 bytes. Les blocks tout comme les wallets seront enregistrés respectivement dans /classes/content/bloc et /classes/content/wallets.

## utilisation

Pour créer une transaction vous avez juste besoin d'utiliser la méthode classes/Chain#add_transaction(Transaction(Wallet, Wallet, montant)) dans main.py.
Voici un exemple :
```
wallet1 = Wallet(MAX_TOKEN_NUMBER)
wallet2 = Wallet(MAX_TOKEN_NUMBER)

chain = Chain()

chain.add_transaction(Transaction(wallet1,wallet2, 50))

