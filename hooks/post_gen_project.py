import os
import shutil

source_dir = os.getcwd()
target_dir = "{{ cookiecutter.final_destination }}"

if len(target_dir) > 3:
    shutil.move(source_dir, target_dir)