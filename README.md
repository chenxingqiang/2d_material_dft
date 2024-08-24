# 2D Material DFT Calculations

This project performs Density Functional Theory (DFT) calculations on two-dimensional materials using Quantum ESPRESSO. It's designed to study the electronic properties of MoS2, NbSe2, Si, and Ge in their 2D forms.

## Features

- Performs DFT calculations for MoS2, NbSe2, 2D hexagonal Si, and 2D hexagonal Ge
- Calculates and plots band structures
- Calculates and plots density of states (DOS)
- Modular design for easy extension to other 2D materials

## Prerequisites

- CentOS 8 or compatible Linux distribution
- Python 3.6+
- Quantum ESPRESSO 7.0+
- MPI library (e.g., OpenMPI)
- LAPACK and BLAS libraries
- FFTW library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/chenxingqiang/2d_material_dft.git
   cd 2d_material_dft
   ```

2. Run the environment setup script:
   ```
   ./install_environment.sh
   ```

3. Activate the Python virtual environment:
   ```
   source qe_env/bin/activate
   ```

## Usage

1. Ensure you have the necessary pseudopotential files in the `pseudo` directory.

2. Prepare the input structure files (.cif) for each material in the `structures` directory.

3. Run the main calculation script:
   ```
   python main.py
   ```

4. Results will be saved in the `results` directory, organized by material.

To download the pseudopotential files required for the DFT calculations in your Python script, you can use the following shell script. This script utilizes `wget` to download the files from a repository like the Quantum ESPRESSO pseudopotential library.

### Shell Script to Download Pseudopotentials

```bash
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
```

### Instructions:

1. Save this script as `download_pseudopotentials.sh`.
2. Give the script execution permission:
   ```bash
   chmod +x download_pseudopotentials.sh
   ```
3. Run the script to download the required pseudopotential files:
   ```bash
   ./download_pseudopotentials.sh
   ```

This script will create a directory called `pseudopotentials` and download all the necessary `.UPF` files into it. Ensure that the URLs used in the script are correct and correspond to the versions of the pseudopotentials you need. If you're using a different source for the pseudopotentials, replace the URLs accordingly.

## Project Structure

```
2d_material_dft/
├── README.md
├── install_environment.sh
├── main.py
├── lib/
│   ├── quantum_espresso.py
│   └── utils.py
├── src/
│   ├── dft_calculation.py
│   ├── band_structure.py
│   ├── density_of_states.py
│   ├── visualization.py
│   └── run_calculation.py
├── tests/
│   ├── test_dft.py
│   ├── test_band_structure.py
│   └── test_dos.py
├── results/
│   ├── mos2/
│   ├── nbse2/
│   ├── si/
│   └── ge/
├── pseudo/
└── structures/
```

## Running Tests

To run the unit tests:

```
python -m unittest discover tests
```

## Results

The calculated results include:
- SCF calculation outputs
- Band structure plots
- Density of states plots

These can be found in the respective subdirectories under the `results` directory.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2023 turingai.Co,ltd. Hangzhou, China

### Acknowledgments

- This project is based on the research described in the following paper:

  S. Lebègue and O. Eriksson, "Electronic structure of two-dimensional crystals from ab initio theory," Physical Review B, vol. 79, no. 11, p. 115409, 2009. DOI: 10.1103/PhysRevB.79.115409

- Quantum ESPRESSO team for providing the DFT calculation software.

## References

[1] S. Lebègue and O. Eriksson, "Electronic structure of two-dimensional crystals from ab initio theory," Physical Review B, vol. 79, no. 11, p. 115409, 2009. [Online]. Available: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.79.115409

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2023 turingai.ltd

## Contact

For any queries, please open an issue in the GitHub repository.