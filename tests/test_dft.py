import unittest
from src.dft_calculation import run_dft_calculation
import os


class TestDFTCalculation(unittest.TestCase):
    def test_mos2_calculation(self):
        run_dft_calculation(
            "mos2",
            "test_structures/mos2.cif",
            {
                "Mo": "Mo.pbe-spn-kjpaw_psl.1.0.0.UPF",
                "S": "S.pbe-n-kjpaw_psl.1.0.0.UPF",
            },
            [4, 4, 1],
            30,
        )
        self.assertTrue(os.path.exists("results/mos2/mos2.scf.out"))

    # 添加其他材料的测试...


if __name__ == "__main__":
    unittest.main()
