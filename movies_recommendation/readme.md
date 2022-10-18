Here I create a few recommendations systems for movies using data with users ratings.

# setting up environment
git clone https://github.com/bulka4/movies_recommendation.git
cd movies_recommendation
# create virtual environment
python -m venv venv
# activating venv for Windows:
venv\Scripts\activate
# activating venv for Mac:
source venv/bin/activate
# update pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt
# you can check this code using JupyterLab, in order to run it just write this command with activated venv:
jupyter-lab