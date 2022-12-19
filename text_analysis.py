from transformers import pipeline
import pandas as pd

def txt_sentiment(text:str)->list:

    sentiment_pipeline = pipeline("sentiment-analysis")
    data = text.split('.')
    return sentiment_pipeline(data)

def df_sentiment(df):
    sentiment_pipeline = pipeline("sentiment-analysis")
    df['label']=''
    df['score']=''
    df['sentiment']=''
    text = list(df['text'])
    sentiment = sentiment_pipeline(text)
    df['sentiment']=sentiment
    label = []
    score = []
    for s in sentiment:
        label.append(s['label'])
        score.append(s['score'])
    df['label'] = label
    df['score'] = score

    return df

def txt_overall_sentiment(text:str)->list:
    sentiment_pipeline = pipeline("sentiment-analysis")

    return sentiment_pipeline(text)


def sentiment_analysis(sentiments:list)->None:
    #Take the sentiment array in input and give the number of positive, negative, len, overall

    posive = 0
    negative = 0
    overall = 0
    overall_tracker = [0]
    len_sentiments = len(sentiments)
    for sentiment in sentiments:
        if sentiment['label']=='POSITIVE':
            posive +=1
            overall +=sentiment['score']
            overall_tracker.append(overall)
        else:
            negative +=1
            overall -=sentiment['score']
            overall_tracker.append(overall)

    overall = (overall+len_sentiments)/(2*len_sentiments)*100 #score between 0 and 100%
    posive_pct = posive/len_sentiments*100
    negative_pct = negative/len_sentiments*100

    print(f'We have {posive_pct:0.2f}% of positive sentences (or {posive} out of {len_sentiments}) and {negative_pct:0.2f}% of negative sentences (or {negative} out of {len_sentiments}).')
    print(f'The overall sentiment score is {overall:0.2f}% (where 0% is totally negative and 100% is totally positive.)')
    if overall>=50:
        print('The overall outlook is positive!')
    else:
        print('The overall outlook is negative!')


    import matplotlib.pyplot as plt
    import numpy as np

    overall_tracker = np.array(overall_tracker)
    overall_tracker = (overall_tracker+len_sentiments)/(2*len_sentiments)*100

    plt.plot(overall_tracker)
    plt.title('Sentiment across the speech')
    plt.ylabel('Sentiment (%)')
    plt.xlabel('Sentences')
