# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Explanation
  Having little to no background knowledge in computer science, I wanted to push my boundaries and learn more about coding, and computer science in general, from this challenge. Due to my lack of knowledge in the field, I decided to research sentiment analysis more in-depth and what it did, learning that the language identifies subjective information with natural language processing and text analytics. Due to the prompt's suggestion on python, I decided to look more into that programming language because of its easy-to-implement nature. From there, I found that it was useful to know that sentiment analysis used natural language processing tools to identify "emotions" in text (allowing the computer to understand the human language) because I decided to adopt and understand python NLTK code with the help of 2 different beginner-friendly sources online. According to the Datacamp source, there are 2 ways to perform sentiment analysis: a machine learning-based approach or a lexicon-based approach. Reading these definitions, I was able to recognize that for this challenge the lexicon-based approach was easier and useful to figure out the score of the text file. In addition, I took the source's example of sentence tokenization and applied it to the text file, effectively breaking down the file into sentences. Then, with the Medium source’s help, I was able to take code and understand that the values of the positive, negative, and overall score need to be set to 0 so that it's easier to read and so there's no value bias. Thus, when the sums of the scores are printed, I can see the individual scores add up and decipher the negative and positive tone of the text.

Sources Used:
- https://medium.com/@sharonwoo/sentiment-analysis-with-nltk-422e0f794b8
- https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk

Scores:
- Overall Score: 0.17
- Positive Score: 0.14
- Negative Score: -0.11

  As you can see from the overall score, it is a little bit more positive. This score indicates that the body of text has a slightly more positive tone (due to the range of positive words compared to the negative words detected by the code). 
  
