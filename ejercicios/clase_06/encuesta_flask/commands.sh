# Create environment
conda create --name encuestas_flask
source activate encuestas_flask
conda install -c conda-forge flask-sqlalchemy flask-wtf
conda env export > environment.yml

# Create folder structure
mkdir encuesta_flask
# But first initialize a git repository
git init
cd encuesta_flask/
touch README.md
# Create the main module
mkdir encuesta_proyecto
cd encuesta_proyecto/
# Create main module configuration files
touch __init__.py app.py config.py database.py
# Create all the folders
mkdir applications static templates
# Now create the application folders to host the blueprints
cd applications/
touch __init__.py
# And create the blueprint
mkdir encuesta_app
cd encuesta_app/
# With all the required files and folders
touch __init__.py conf.py models.py urls.py
mkdir static templates views
touch views/__init__.py
