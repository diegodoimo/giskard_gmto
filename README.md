# What are the odds to reach Endor?

A simple web application to compute the probability that the Millennium Falcon reaches Endor before the Death Star.

Platforms:

- Ubuntu 22.04

## Create the environment

You can get miniconda from https://docs.conda.io/en/latest/miniconda.html, or install the dependencies shown below manually.

```
conda create -n gmto_env                                
conda activate gmto_env
python3 -m pip install --upgrade build
pip install flask, flask_wtf
```

## Install the package
```
python3 -m build
pip install .
```

## Compute the probability to arrive at the destination planet from command line: 
```
give-me-the-odds tests/examples/example1/millennium-falcon.json tests/examples/example1/empire.json
``` 

## Run the web appliction with:
```
python run_webpage.py
```
