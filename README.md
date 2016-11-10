# AutoTextCat

## Automated categorisation of 'User Intent' survey on gov.uk

This repository is hosted on github.gds here: <https://github.gds/DataScience/intents_survey>

## Requirements

Nominally this application requires the following:

* Python >= 3.5.2  
* [classify](https://github.com/ivyleavedtoadflax/classify.git) >= 0.4.0  

See [requirements.txt](requirements.txt)

## Outline

One in 50 users of gov.uk are requested to fill in a survey on their intents.
This survey contains a number of categorical fields with classes such as 'Satisfied' and 'Unsatisfied'.
Users are also asked to fill in a number of free text boxes.
At present a subset of these reponses are categorised by hand.

A corpus of pre-classified documents exists.
This app uses a pre-trained model that was applied to the pre-classified corpus to identify new cases that can be classes as 'ok' and therefore excluded from the manual classification process.

## What is here

This repo is a heroku app which allows survey monkey files to be uploaded, a machine learning algorithm to be applied, and an automatically classified file to be downloaded.

