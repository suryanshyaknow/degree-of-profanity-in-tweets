# Degree Of Profanity Computation For Twitter Tweets

## Problem Statement

Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file. Write in any programming language (preferably in Python) - make any assumptions, but remember to state them.

## Assumptions Made

**i.** Imagining that a dataframe `df_tweets` has been prepared out of the said twitter's tweets file in which there are two columns -- `USERS` containing user names and `TWEETS` containing the repective tweets. And the objective is to compute the `degree of profanity` for each tweet made by a certain user.

**ii.** `racial_slurs` is a list where each element represents a profane word in its base (lemmatized) form.

**iii.** Additionaly, I'm presuming that before `degree of profanity` is to be computed for a tweet, the tweet has to be cleaned -- removal of stop words accompanied by the lemmatization of the word tokens, for the least part.