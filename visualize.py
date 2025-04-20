import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Function to plot how frequent different sentiment occurs.

    Args : list of sentiments.

    Return : list of each sentiment occured.

    """
    
    sentiment_counts = [0,0,0,0]

    for items in sentiments:
        if items == "positive":
            sentiment_counts[0] += 1
        elif items == 'negative':
            sentiment_counts[1] += 1
        elif items == 'neutral':
            sentiment_counts[2] += 1
        else:
            sentiment_counts[3] += 1
    
    fig,ax = plt.subplots()
    ax.set_title("Sentiment_Analysis")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    ax.bar(["Positive","Negative","Neutral","Irrelevant"],sentiment_counts)

    plt.tight_layout()
    fig.savefig("images/sentiment_analysis.png")


    return sentiment_counts


