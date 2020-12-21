# Install Python 3.7
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7

# Make and Activate 3.7 venv
sudo apt-get install python3.7-dev python3.7-venv
cd ~/kaggle_riiid
python3.7 -m venv ./venv
source ./venv/bin/activate

# Make 3.7 Kernel
python3.7 -m pip install ipykernel
python3.7 -m ipykernel install --user --name riiid

# Install libraries
pip install boto3
pip install pandas
pip install scikit-learn
pip install scipy
pip install wheel

# Install LightGBM
cd ~
sudo apt-get install cmake
git clone --recursive https://github.com/microsoft/LightGBM
cd LightGBM
mkdir build
cd build
cmake ..
make -j4
cd ../python-package
sudo /home/ubuntu/kaggle_riiid/venv/bin/python setup.py install



