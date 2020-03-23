
# Computational Neuroscience Project Skeleton

This repository is a skeleton Python package that students in PSYC 5270 can use to get started on their data exploration assignments.

## Getting started

Start by cloning the repository: `git clone https://github.com/melizalab/comp-neurosci-skeleton.git`

This will create a new directory, `comp-neurosci-skeleton`, containing the following items:

- `README.md`: this file
- `setup.py`:  package description file. You will need to edit this.
- `requirements.txt`: a list of packages your code depends on
- `.gitignore`: a list of files git will ignore when telling you what's changed
- `src`:       a directory where you will put your python code
- `test`:      a directory where you will put test code
- `data`:      a directory where your data will live
- `build`:     a directory where processed output from your analysis will live

Choose a new name for your package. For the PSYC 5270 assignment, use something like `crcns-datasetid-computingid`. Rename the top-level directory (`comp-neurosci-skeleton`) and edit `setup.py` to set the new name and other identifying information.

Now you need to create a github repository of your own. Go to [https://github.com/new](https://github.com/new). Give the repository your chosen name and a description, then click Create Repository. **DO NOT** check the box to initialize the repository with a readme. Ignore the instructions on how to set up your repository, but make a note of the address. It will look something like `https://github.com/dmeliza/dummy.git`

Finally, set your local directory to track the github repository by running the following commands in your working directory. Replace the repository address in the code below with the one for your project.

``` shell
git remote rm origin
git remote add origin https://github.com/dmeliza/dummy.git
git push -u origin master
```

If you get an error on the last command, it's probably because you let github initialize your repository. You'll have to delete and re-create the repository on github and then run the last command again.

## Next steps

Edit `data/README.md` to describe how to retrieve data. Better yet, write a script.

Edit `requirements.txt` to add any needed dependencies, then create a virtual environment and install the dependencies as follows:

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Alternatively, if you're using anaconda, create a new environment and run the following to install dependencies:

``` shell
conda install git numpy scipy pandas matplotlib notebook
```

Install the project in development mode by running `python setup.py develop`. If you use notebooks, this will ensure that you can access your modules.

Edit this file to describe your actual project.
