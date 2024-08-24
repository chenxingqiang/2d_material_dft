from lib.quantum_espresso import run_dos
import numpy as np
import matplotlib.pyplot as plt


def calculate_dos(material, scf_output):
    """
    计算态密度

    参数:
    material: 材料名称
    scf_output: 自洽计算输出文件
    """
    dos_output = run_dos(material, scf_output)
    energies, total_dos, partial_dos = parse_dos_output(dos_output)
    return energies, total_dos, partial_dos


def plot_dos(energies, total_dos, partial_dos, atom_labels, fermi_energy):
    plt.figure(figsize=(10, 6))
    plt.plot(energies - fermi_energy, total_dos, label="Total", color="black")

    for i, (atom, dos) in enumerate(partial_dos.items()):
        plt.plot(energies - fermi_energy, dos, label=atom_labels[i])

    plt.xlabel("Energy (eV)")
    plt.ylabel("Density of States")
    plt.title("Density of States")
    plt.axvline(x=0, color="r", linestyle="--", label="Fermi Level")
    plt.xlim(-6, 6)  # 根据实际情况调整
    plt.legend()
    plt.grid(True)
    plt.savefig("results/density_of_states.png")
    plt.close()


if __name__ == "__main__":
    # 示例: 计算并绘制MoS2的态密度
    energies, total_dos, partial_dos = calculate_dos(
        "mos2", "results/mos2/mos2.scf.out"
    )
    plot_dos(
        energies, total_dos, partial_dos, ["Mo-sp", "Mo-d", "S-sp"], fermi_energy=0
    )
