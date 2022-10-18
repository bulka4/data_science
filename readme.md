## Setting up virtual environment and requirements 

python3.7 -m venv venv  
source venv/bin/activate  
  
python3.7 -m pip install --upgrade pip  
pip3 install -r requirements.txt  

## installing jupyter-lab:
pip install jupyterlab  
pip install ipykernel  
python -m ipykernel install --user --name=venv  