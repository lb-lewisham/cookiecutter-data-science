# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### Starting a new project:
------------
To start a new project, `cd` into a directory where you want the new project and run

    cookiecutter https://github.com/lb-lewisham/cookiecutter-data-science.git

This version of the `cookiecutter` data science template provides a few modifications to the original one. For one, the directory structure is simplified. Second, this template provides an option to choose from various different projects types (e.g. mapping, torch_ml, tensorflow_ml, general, and minimal), which will add packages to the `requirements.txt` file accordingly. This template also adds the option of including boilerplate code in the `clean_dataset.py` file in the form of paths to the different `data` and `models` folders. Finally, as Windows Command Prompt cannot handle UNC paths (although PowerShell can), the `final_destination` option allows the user to define a final path for the project manually. This requires a full path to be provided, after which the `post_gen_project.py` hook will run to move the project folder to the specified location. Leave the `final_destination` option empty if you do not wish to move the project. 

The below video is not an accurate representation of the options shown when using this fork.
[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)

### New version of Cookiecutter Data Science
------------
Cookiecutter data science is moving to v2 soon, which will entail using
the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
will continue to work, and this version of the template will still be available.
To use the legacy template, you will need to explicitly use `-c v1` to select it.
Please update any scripts/automation you have to append the `-c v1` option (as above),
which is available now.


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```

├── README.md          <- The top-level README for developers using this project.
├── .gitignore         <- NEVER DELETE THIS FILE.
├── data
│   ├── downloaded     <- Data from downloads.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt
├── .env               <- Environment variables                          
│
├── clean_dataset.py   <- Compilation and reformatting of data to create data files in /data/processed/
│                          
└── analysis.py        <- Analyse data and create final data product based on files in /data/processed/
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt


