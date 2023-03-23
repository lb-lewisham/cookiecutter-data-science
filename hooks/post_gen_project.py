import os
import shutil

source_dir = os.getcwd()
target_dir = "{{ cookiecutter.final_destination }}"

shutil.move(source_dir, target_dir)