from src.run_calculation import run_mos2, run_nbse2, run_si, run_ge


def main():
    print("Starting 2D material DFT calculations...")

    print("Calculating MoS2...")
    run_mos2()

    print("Calculating NbSe2...")
    run_nbse2()

    print("Calculating Si...")
    run_si()

    print("Calculating Ge...")
    run_ge()

    print("All calculations completed.")


if __name__ == "__main__":
    main()
