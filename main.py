from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    INSERT DOCSTRING HERE
    """
    # open the json object
    with open (filepath) as j:
        data = json.load(j)
        
    # extract the reviews from the json file
    data['results']


    # get a list of sentiments for each line using get_sentiment
    final_result = get_sentiment(data['results'])

    # plot a visualization expressing sentiment ratio
    make_plot(final_result)

    # return sentiments
    return(final_result)


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
