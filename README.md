# Data extraction scripts

Collection of personal tools and scripts to extract data from different sources

## Twitter listener

Use it to extract data from Twitter in real time. In the variable "listening" write whatever keywork you want to filter tweets. The filtered tweets will be inserted in a new sqlite database that will be created in the same working directory you execute the script.

## Twitter search

Search in Twitter for a particular query. This will only return tweets made at the moment of execution or in the past, with a limit of 7 days in the past. Also creates a sqlite database in the cwd.
