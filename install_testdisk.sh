#!/bin/bash

# Vérification si Homebrew est déjà installé
if ! command -v brew &>/dev/null; then
    echo "Installation de Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew est déjà installé."
fi

# Installation de TestDisk via Homebrew
echo "Installation de TestDisk..."
brew install testdisk

echo "Installation terminée."

