# Text classification project walkthrough

On this walkthrough I go through all necessary steps to create your own [text classification](https://monkeylearn.com/text-classification/) project. I choose twitter as the data source, as its relatively easy to mine data from it.

Lets begin with data extraction

## Data extraction

I created two scripts to extract data from Twitter. First however you have to obtain your API key by following [this tutorial](https://www.smartaddons.com/documentation/key/). The scripts are on this repo.

### Twitter listener

Use it to extract data from Twitter in real time. In the variable "listening" write whatever keywork you want to filter tweets. The filtered tweets will be inserted in a new sqlite database that will be created in the same directory you execute the script.

### Twitter search

Search in Twitter for a particular query. This will only return tweets made at the moment of execution or in the past, with a limit of 7 days in the past. Also creates a sqlite database.

## Cleaning data, from sql database to csv

We need to convert the previous sqlite file to a csv, so we can use some anotation tool for labeling. We cant train our own model or test the accuracy of a model without labeled data. [This notebook](https://github.com/Jvmd95/NLP-project-guide/blob/master/Cleaning%20data%20to%20excel.ipynb) explains the necessary steps. The output is a csv file that you can input on the data labeling tool of your choice.

## Labeling the data

Labeling the data extracted from Twitter would take a significant amount of time, so I wont do it here. However, I recommend Label Studio to perform the labeling: is straight foward to use and has many useful features. You can find a quick start tutorial [here](https://labelstud.io/guide/#Quickstart). Labeling the data is not a complicated process, but is very time consuming.

## Modeling

Once you have your data labeled you can follow [this personal notebook](https://github.com/Jvmd95/NLP-classification-with-disaster-Tweets/blob/master/NLP%20classification%20disaster%20Tweets.ipynb) I made for a Kaggle competition to perform modeling. In that notebook I use google BERT, a neural network-based technique for natural language processing that can achieve state of the art accuracy. The task is a similar classification task, and you can just swap the data from the notebook for the data extracted from Twitter.

### Some comments:

Needless to say this is a simple sketch of a text classification project, chances are that depending on your project you will need to clean the data in a different way or extract different features from the data, however I hope it helps on getting started.
