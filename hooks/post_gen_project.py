import os
import shutil

source_dir = os.getcwd()
target_dir = "{{ cookiecutter.final_destination }}"

models_dir = os.path.join(source_dir, 'models')
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if len(target_dir) > 3:
    shutil.move(source_dir, target_dir)