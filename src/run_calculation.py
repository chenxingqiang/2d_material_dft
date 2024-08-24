import os
from lib.quantum_espresso import run_pw, generate_pw_input, parse_pw_output


# 解析CIF文件
def parse_cif(cif_content):
    lines = cif_content.split("\n")
    cell_params = []
    atomic_positions = []

    for line in lines:
        if line.startswith("_cell_length_a"):
            a = float(line.split()[-1])
        elif line.startswith("_cell_length_b"):
            b = float(line.split()[-1])
        elif line.startswith("_cell_length_c"):
            c = float(line.split()[-1])
        elif line.startswith("_cell_angle_alpha"):
            alpha = float(line.split()[-1])
        elif line.startswith("_cell_angle_beta"):
            beta = float(line.split()[-1])
        elif line.startswith("_cell_angle_gamma"):
            gamma = float(line.split()[-1])
        elif line.startswith("C") or line.startswith("Mg"):
            parts = line.split()
            if len(parts) == 8:
                atomic_positions.append(
                    (parts[0], float(parts[3]), float(parts[4]), float(parts[5]))
                )

    cell_params = f"{a:.6f} 0.0 0.0\n0.0 {b:.6f} 0.0\n0.0 0.0 {c:.6f}"
    return cell_params, atomic_positions


# 读取CIF内容
with open("molecule.cif", "r") as f:
    cif_content = f.read()

# 解析CIF文件
cell_parameters, atomic_positions = parse_cif(cif_content)

# 设置计算参数
pseudopotentials = [
    ("C", 12.0107, "C.pbe-n-kjpaw_psl.1.0.0.UPF"),
    ("Mg", 24.305, "Mg.pbe-n-kjpaw_psl.1.0.0.UPF"),
]
k_points = [2, 2, 2]
calculation_params = {
    "calculation": "scf",
    "prefix": "C60Mg3.966",
    "pseudo_dir": "./pseudo",
    "outdir": "./tmp",
    "ecutwfc": 60,
}

# 生成输入文件内容
input_content = generate_pw_input(
    cell_parameters, atomic_positions, pseudopotentials, k_points, calculation_params
)

# 将输入文件内容写入文件
with open("C60Mg3.966.in", "w") as f:
    f.write(input_content)

# 运行计算
run_pw("C60Mg3.966.in", "C60Mg3.966.out", num_processors=4)

# 解析输出文件
results = parse_pw_output("C60Mg3.966.out")

# 打印结果
print("计算结果:")
print(f"总能量: {results.get('total_energy', 'N/A')} Ry")
print(f"费米能级: {results.get('fermi_energy', 'N/A')} eV")
from src.dft_calculation import run_dft_calculation
from src.band_structure import calculate_band_structure, plot_band_structure
from src.density_of_states import calculate_dos, plot_dos


def run_mos2():
    # MoS2计算
    run_dft_calculation(
        "mos2",
        "structures/mos2.cif",
        {"Mo": "Mo.pbe-spn-kjpaw_psl.1.0.0.UPF", "S": "S.pbe-n-kjpaw_psl.1.0.0.UPF"},
        [40, 40, 1],
        500,
    )

    energies, k_points = calculate_band_structure(
        "mos2", "results/mos2/mos2.nscf.out", ["G", "M", "K", "G"]
    )
    plot_band_structure(energies, k_points, ["Γ", "M", "K", "Γ"], fermi_energy=0)

    energies, total_dos, partial_dos = calculate_dos(
        "mos2", "results/mos2/mos2.scf.out"
    )
    plot_dos(
        energies, total_dos, partial_dos, ["Mo-sp", "Mo-d", "S-sp"], fermi_energy=0
    )


def run_nbse2():
    # NbSe2计算
    run_dft_calculation(
        "nbse2",
        "structures/nbse2.cif",
        {"Nb": "Nb.pbe-spn-kjpaw_psl.1.0.0.UPF", "Se": "Se.pbe-n-kjpaw_psl.1.0.0.UPF"},
        [40, 40, 1],
        500,
    )

    # 能带和DOS计算同MoS2


def run_si():
    # Si计算
    run_dft_calculation(
        "si",
        "structures/si.cif",
        {"Si": "Si.pbe-n-kjpaw_psl.1.0.0.UPF"},
        [20, 20, 1],
        500,
    )

    # 能带和DOS计算同MoS2


def run_ge():
    # Ge计算
    run_dft_calculation(
        "ge",
        "structures/ge.cif",
        {"Ge": "Ge.pbe-n-kjpaw_psl.1.0.0.UPF"},
        [20, 20, 1],
        500,
    )

    # 能带和DOS计算同MoS2


if __name__ == "__main__":
    run_mos2()
    run_nbse2()
    run_si()
    run_ge()
