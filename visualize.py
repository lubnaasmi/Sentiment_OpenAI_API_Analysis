import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Function to plot how frequent different sentiment occurs.

    Args : list of sentiments. eg, ['positive','negative','neutral']

    Return : list of each sentiment occured. eg,[30,9,0]

    """
    
    pos = 0
    neg = 0
    neu = 0
    irr = 0

    for items in sentiments:
        if items == "positive":
            pos += 1
        elif items == 'negative':
            neg += 1
        elif items == 'neutral':
            neu += 1
        else:
            irr += 1
    
    fig,ax = plt.subplots()
    ax.set_title("Sentiment_Analysis")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("count")
    ax.bar(["Positive","Negative","Neutral","Irrelevant"],[pos, neg, neu, irr])
    fig.savefig("/Users/lubna/Documents/TKH_Labs/review-process/images/sentiment_analysis.png")


    return [pos, neg, neu, irr]







