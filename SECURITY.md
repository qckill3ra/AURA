# AURA Security Policy


## Philosophie

AURA fonctionne selon le principe :

Zero Trust.


## Interdit permanent

AURA ne doit jamais :

- Lire les mots de passe
- Accéder au coffre Vaultwarden
- Envoyer des données Internet
- Ouvrir un port réseau
- Supprimer des fichiers
- Modifier le firewall
- Désactiver les protections


## Validation obligatoire

Confirmation utilisateur nécessaire pour :

- Exécution de scripts
- Installation logiciel
- Modification système
- Modification réseau
- Accès fichiers sensibles


## Réseau

AURA fonctionne localement.

Les communications externes doivent passer par des services contrôlés.


## Audit

Toute action importante doit être journalisée.