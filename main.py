from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    Function to extract the reviews from json file  
    Args : filepath
    Return: the list of sentiments you've generated from your OpenAI API.
    """
    
    with open (filepath) as j:
        data = json.load(j)
        
    data['results']

    # get a list of sentiments for each line using get_sentiment
    final_result = get_sentiment(data['results'])

    # plot a visualization expressing sentiment ratio
    make_plot(final_result)


    return(final_result)


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
