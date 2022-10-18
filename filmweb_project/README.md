This respiratory contains a code where I create a data set about movies from base at filmweb.pl, built some models trying to predict a rating of a movies and built a recommendation system.

# setting up environment
git clone https://github.com/bulka4/filmweb_project.git
cd filmweb_project
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