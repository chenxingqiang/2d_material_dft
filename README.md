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

## Acknowledgments

- This project is based on the research paper: "Electronic structure of two-dimensional crystals from ab initio theory" by S. Lebègue and O. Eriksson.
- Quantum ESPRESSO team for providing the DFT calculation software.

## Contact

For any queries, please open an issue in the GitHub repository.