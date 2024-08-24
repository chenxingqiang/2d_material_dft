import os
from lib.quantum_espresso import run_pw


def run_dft_calculation(
    material, structure_file, pseudopotentials, kpoints, cutoff_energy
):
    """
    运行DFT计算

    参数:
    material: 材料名称 (mos2, nbse2, si, 或 ge)
    structure_file: 结构文件路径
    pseudopotentials: 赝势文件字典
    kpoints: k点网格
    cutoff_energy: 平面波截断能
    """
    input_params = {
        "calculation": "scf",
        "prefix": material,
        "pseudo_dir": "./pseudo",
        "outdir": f"./results/{material}",
        "ibrav": 0,
        "nat": 3 if material in ["mos2", "nbse2"] else 2,
        "ntyp": 2 if material in ["mos2", "nbse2"] else 1,
        "ecutwfc": cutoff_energy,
        "ecutrho": cutoff_energy * 4,
        "occupations": "smearing",
        "smearing": "gaussian",
        "degauss": 0.01,
        "mixing_beta": 0.7,
        "conv_thr": 1.0e-8,
    }

    run_pw(input_params, structure_file, pseudopotentials, kpoints)


if __name__ == "__main__":
    # 示例: 运行MoS2的DFT计算
    run_dft_calculation(
        "mos2",
        "structures/mos2.cif",
        {"Mo": "Mo.pbe-spn-kjpaw_psl.1.0.0.UPF", "S": "S.pbe-n-kjpaw_psl.1.0.0.UPF"},
        [40, 40, 1],
        500,
    )
