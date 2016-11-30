[![GitHub tag](https://img.shields.io/github/tag/ivyleavedtoadflax/AutoTextCat.svg)]()

# Automated categorisation of 'User Intent' survey

## Requirements

Nominally this application requires the following:

* Python >= 3.5.2  
* [classify](https://github.com/ivyleavedtoadflax/classify.git) >= 0.4.0  

See [requirements.txt](requirements.txt)

## What is it?

This repo is a heroku app which allows survey monkey files to be uploaded, a machine learning algorithm to be applied, and an automatically classified file to be downloaded.

The heavy lifting is done by the [classify](git@github.com:ivyleavedtoadflax/classify.git) class, with a machine learning model packaged as a pickle object applied in the app.

Currently only the transformation of the data, not the machine learning is implemented.

