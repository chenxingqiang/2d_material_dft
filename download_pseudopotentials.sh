#!/bin/bash

# Create a directory for pseudopotentials
mkdir -p pseudopotentials

# Download pseudopotentials for MoS2
wget -O pseudopotentials/Mo.pbe-spn-kjpaw_psl.1.0.0.UPF "https://www.quantum-espresso.org/upf_files/Mo.pbe-spn-kjpaw_psl.1.0.0.UPF"
wget -O pseudopotentials/S.pbe-n-kjpaw_psl.1.0.0.UPF "https://www.quantum-espresso.org/upf_files/S.pbe-n-kjpaw_psl.1.0.0.UPF"

# Download pseudopotentials for NbSe2
wget -O pseudopotentials/Nb.pbe-spn-kjpaw_psl.1.0.0.UPF "https://www.quantum-espresso.org/upf_files/Nb.pbe-spn-kjpaw_psl.1.0.0.UPF"
wget -O pseudopotentials/Se.pbe-n-kjpaw_psl.1.0.0.UPF "https://www.quantum-espresso.org/upf_files/Se.pbe-n-kjpaw_psl.1.0.0.UPF"

# Download pseudopotentials for Si
wget -O pseudopotentials/Si.pbe-n-kjpaw_psl.1.0.0.UPF "https://www.quantum-espresso.org/upf_files/Si.pbe-n-kjpaw_psl.1.0.0.UPF"

# Download pseudopotentials for Ge
wget -O pseudopotentials/Ge.pbe-n-kjpaw_psl.1.0.0.UPF "https://www.quantum-espresso.org/upf_files/Ge.pbe-n-kjpaw_psl.1.0.0.UPF"

echo "Pseudopotentials downloaded successfully to the pseudopotentials directory."