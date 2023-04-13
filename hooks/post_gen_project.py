import os
import shutil

source_dir = os.getcwd()
target_dir = "{{ cookiecutter.final_destination }}"

models_dir = os.path.join(source_dir, 'models')
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if len(target_dir) > 3:
    shutil.move(source_dir, target_dir)

boilerplate = "{{cookiecutter.add_boilerplate}}"
if boilerplate == "Yes":
    boilerplate_text = 'from pathlib import Path\nraw = Path("data/raw")\nprocessed = Path("data/processed")\ninterim = Path("data/interim")\ndownloaded = Path("data/downloaded")\nmodels = Path("models")'
    with open(os.path.join(source_dir, 'clean_dataset.py'), 'w+') as f:
        f.write(boilerplate_text)
    