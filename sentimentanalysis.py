import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

# Read input.txt
readfile = open("input.txt","r")
text = readfile.read()

# Tokenize text
sentences = tokenize.sent_tokenize(text)

# Instantiate SIA and Scores
SIA = SentimentIntensityAnalyzer()
overallScore = 0
positiveScore = 0
negativeScore = 0

# Sum scores
for sentence in text:
    overallScore += SIA.polarity_scores(sentence)['compound']
    positiveScore += SIA.polarity_scores(sentence)['positive']
    negativeScore -= SIA.polarity_scores(sentence)['negative']
    
# Print scores
print("Overall Score", overallScore/len(text))
print("Positive Score", positiveScore/len(text))
print("Negative Score", negativeScore/len(text))
