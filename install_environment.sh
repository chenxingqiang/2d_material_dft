#!/bin/bash

# 更新系统包
sudo dnf update -y

# 安装必要的依赖
sudo dnf install -y gcc gcc-gfortran openmpi openmpi-devel lapack-devel blas-devel fftw-devel make wget python3 python3-devel

# 安装 Quantum ESPRESSO
wget https://github.com/QEF/q-e/archive/qe-7.0.tar.gz
tar -xzvf qe-7.0.tar.gz
cd q-e-qe-7.0
./configure
make all
sudo make install
cd ..

# 创建 Python 虚拟环境
python3 -m venv qe_env
source qe_env/bin/activate

# 安装 Python 依赖
pip install numpy matplotlib ase

echo "Environment setup completed!"
