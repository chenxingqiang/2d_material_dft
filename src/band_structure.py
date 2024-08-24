from lib.quantum_espresso import run_bands
import numpy as np
import matplotlib.pyplot as plt


def calculate_band_structure(material, nscf_output, kpath):
    """
    计算能带结构

    参数:
    material: 材料名称
    nscf_output: 非自洽计算输出文件
    kpath: k点路径
    """
    bands_output = run_bands(material, nscf_output, kpath)
    energies, k_points = parse_bands_output(bands_output)
    return energies, k_points


def plot_band_structure(energies, k_points, k_labels, fermi_energy):
    plt.figure(figsize=(10, 6))
    for band in energies.T:
        plt.plot(k_points, band - fermi_energy, color="blue")

    plt.xlabel("k-points")
    plt.ylabel("Energy (eV)")
    plt.title("Band Structure")
    plt.axhline(y=0, color="r", linestyle="--", label="Fermi Level")
    plt.ylim(-6, 6)  # 根据实际情况调整
    plt.xticks(k_points[:: len(k_points) // len(k_labels)], k_labels)
    plt.legend()
    plt.grid(True)
    plt.savefig("results/band_structure.png")
    plt.close()


if __name__ == "__main__":
    # 示例: 计算并绘制MoS2的能带结构
    energies, k_points = calculate_band_structure(
        "mos2", "results/mos2/mos2.nscf.out", ["G", "M", "K", "G"]
    )
    plot_band_structure(energies, k_points, ["Γ", "M", "K", "Γ"], fermi_energy=0)
