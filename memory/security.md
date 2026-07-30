# Security Rules

## Interdictions permanentes

- Lire les mots de passe
- Lire Vaultwarden
- Exporter des données hors du réseau local
- Supprimer des fichiers
- Modifier le pare-feu
- Désactiver Windows Defender
- Modifier OPNsense sans validation
- Modifier Proxmox sans validation
- Installer un logiciel automatiquement

---

## Confirmation obligatoire

- Exécuter PowerShell
- Exécuter Python
- Modifier un fichier
- Créer une tâche planifiée
- Redémarrer un service

---

## Toujours autorisé

- Lire les performances système
- Lire les journaux
- Lire les événements Windows
- Lire les informations matérielles
- Lire les alertes Wazuh

---

## Internet

Accès Internet :

INTERDIT

Tous les accès Internet doivent passer par un connecteur explicitement autorisé.