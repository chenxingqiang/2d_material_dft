#!/bin/bash

# GitHub 仓库创建
echo "Creating GitHub repository..."
gh repo create chenxingqiang/2d_material_dft --public -y
git clone https://github.com/chenxingqiang/2d_material_dft.git
cd 2d_material_dft

# 创建主目录结构
echo "Creating project structure..."
mkdir src lib tests results

# 创建源代码文件
touch src/dft_calculation.py
touch src/band_structure.py
touch src/density_of_states.py
touch src/visualization.py

# 创建库文件
touch lib/quantum_espresso.py
touch lib/utils.py

# 创建测试文件
touch tests/test_dft.py
touch tests/test_band_structure.py
touch tests/test_dos.py

# 创建结果目录
mkdir results/mos2
mkdir results/nbse2
mkdir results/si
mkdir results/ge

# 创建环境安装脚本
cat << EOF > install_environment.sh
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
EOF

chmod +x install_environment.sh

# 创建 README.md
cat << EOF > README.md
# 2D Material DFT

This project performs DFT calculations on 2D materials using Quantum ESPRESSO.

## Setup

1. Run the environment setup script:
   \`\`\`
   ./install_environment.sh
   \`\`\`

2. Activate the Python virtual environment:
   \`\`\`
   source qe_env/bin/activate
   \`\`\`

## Usage

(Add usage instructions here)

## License

(Add license information here)
EOF

echo "Project structure created successfully!"
echo "GitHub repository initialized and project structure created."
echo "To set up the environment, run: ./install_environment.sh"

# 初始化 git 仓库并提交
git add .
git commit -m "Initial commit: Project structure and setup scripts"
git push -u origin main
