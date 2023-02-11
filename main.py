import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import List
from dataclasses import dataclass


# tweets = list(df_tweets.iloc[:, 1])  # fetch the tweets in a list form from the "TWEETS" feature of df_tweets 

@dataclass
class DegreeOfProfanity:
    """This class shall be used for the computation of `Degree of Profanity` for each tweet in the given
    list of tweets ~ "tweets".

    Args:
        tweets (List): List whose each element represents a tweet made by a certain user in the `str` format.
        racial_slurs (List): A custom list in which each element is a racial slur/profane word based on which 
        the degree of profanity has to be computed for each tweet.
    """
    tweets: List
    racial_slurs: List

    def _get_degree_of_profanity(self, tweet: List) -> float:
        """Computes and returns the `Degree of Profanity` for the given tweet.
        Formula for computing `Degree of Profanity`:
            Degree of Profanity = (Number of Profane Words in the tweet)/(total number of words in the tweet)

        Args:
            tweet (List): Tweet in word tokenized form for which the degree of profanity has to be computed.

        Raises:
            e: Raises an exception shoud any pops up while execution of this method.

        Returns:
            float: Output value of Degree of Profanity for the given tweet.
        """
        try:
            degree_of_profanity = len([word for word in tweet if word in self.racial_slurs])/len(tweet)
            return degree_of_profanity
            ...
        except Exception as e:
            raise e

    def compute(self) -> List:
        """Parses each tweet in the given list of tweets, tokenizes them accompanied by their cleaning --
         removal of stop words and lemmatization --, followed by calculation of degree of profanity for each 
         tweet and finally returns a list containing degree of profanity for each tweet.

        Raises:
            e: Raises an exception shoud any pops up while execution of this method.

        Returns:
            List: List whose each element represents the degree of profanity for each tweet. 
        """
        try:
            lemma = WordNetLemmatizer()  # Lemmatizer object
            degree_of_profanities = []  # List that will contain `Degree of Profanity` for each tweet
            
            for tweet in self.tweets:  # Parsing a tweet at a time
                sentences = nltk.sent_tokenize(tweet)  # Sentence Tokenization
                for sentence in sentences:
                    words = nltk.words_tokenize(sentence)  # Word Tokenization
                    words = words.lower()  # Lowering the words to obliterate the case sensitivity
                    cleaned_tweet = [lemma.lemmatize(word) for word in words if word not in stopwords.words('english')]
                    degree_of_profanities.append(self._get_degree_of_profanity(tweet=cleaned_tweet))
            
            return degree_of_profanities
            ...
        except Exception as e:
            raise e


# Now, the degree of profanities can be assigned to the df_tweets accordingly.
# degree_of_profanity = DegreeOfProfanity(tweets=tweets, racial_slurs=racial_slurs)
# tweets_dop = degree_of_profanity.compute()
# df_tweets["Degree of Profanity"] = tweets_dop