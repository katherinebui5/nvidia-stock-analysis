git clone https://github.com/katherinebui5/nvidia-stock-analysis.git
cd nvidia-stock-analysis

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

pandas
numpy
matplotlib
seaborn
yfinance
scipy
