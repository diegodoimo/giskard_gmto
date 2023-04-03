# What are the odds to reach Endor?

A simple web application to compute the probability that the Millennium Falcon reaches Endor before the Death Star.

Platforms:

- Ubuntu 22.04

## Create the environment

You can get miniconda from https://docs.conda.io/en/latest/miniconda.html, or install the dependencies shown below manually.

```
conda create -n gmto_env python                                
conda activate gmto_env
python3 -m pip install --upgrade build
pip install flask flask_wtf
```

## Install the package
```
python3 -m build
pip install .
```

## Compute the probability (as percentage) to arrive at the destination planet from command line using the tests/examples/example2 setup: 
```
give-me-the-odds tests/examples/example2/millennium-falcon.json tests/examples/example2/empire.json
``` 
The expected answer is 81.0.

## Run the web appliction with:
```
python run_webpage.py
```
Examples of empire data (in a '.json' file format) that can be uploaded on the web interface can be found in one of the directories saved in tests/examples.

