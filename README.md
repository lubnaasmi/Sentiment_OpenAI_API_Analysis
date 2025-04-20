# Sentiment Analysis TLAB — Zico Reviews


Welcome to my TLAB submission for sentiment analysis using the OpenAI API! This project walks through extracting product reviews, analyzing sentiment, and visualizing the results, all built as part of our TLAB assignment.

### Datasets
Company has provided you with a sample of real-world reviews that they've received from customers from 1999-2012 on coconut water. These reviews are listed in the JSON file labeled `reviews.json`.
Company has also provided you an API key to interface with this API. 

### Objective

The goal of this project was to:

Load a set of product reviews from a JSON file.

Use the OpenAI GPT-4o API to classify each review's sentiment.

Plot the distribution of sentiments (positive, negative, neutral, irrelevant).

Practice modular function design and AI prompt engineering.



### How to Run


1) Activate your conda environment via the following terminal command:
```bash
conda activate ds
```

2) Confirm that you see the `(ds)` prompt at the beginning of your environment.

3) Once you've confirmed that you are in your environment, set your given API key to a conda environment variable using the terminal command below:

```bash
conda env config vars set OPENAI_API_KEY="your_api_key"
```

4) Deactivate and reactive your environment by running the following commands in your terminal
```bash
conda deactivate ds
conda activate ds
```

5) Next, install the `openai` package by running the following pip command:
```bash
pip install openai
```


These instructions have been based off of documentation from the [OpenAI API](https://platform.openai.com/docs/libraries?desktop-os=windows&language=python). 


label.py module contains a function that you will implement to interface with the `gpt-4o-mini` language model. It will take in a list of string reviews, and pass this list to the open ai API via the `chat.completions.create()` method.


## Challenges Faced

My bar charts seemed to show more than 50 sentiments even though the input only contained 50 reviews. This was due to the model sometimes returning more than one label per review or appending extra lines. Even after refining the prompt in multiple ways, the output count varied (e.g., 52, 54, or 60 labels), which required additional cleanup and stricter output formatting to correct.

## Next Steps

Explore line by line sentiment classification by sending each review individually to the API to ensure one response per input.

Add a validation step that compares the number of outputs with the number of inputs and flags inconsistencies.

Pre-clean reviews to strip any HTML tags or formatting that may confuse the model.

Improve prompt engineering further to reinforce structure and response limits.


## Conclusion


Based on sentiment analysis of 50 customer reviews using the OpenAI GPT-4o model, the majority of feedback was negative, with approximately 35 out of 50 reviews falling into this category. The most common criticism focused on the product's taste, which many customers described as unpleasant or inferior compared to other brands.

Although the model provided generally accurate classifications, there were some mislabelings, indicating that automated sentiment analysis can benefit from manual review or prompt refinement to improve reliability.

Overall, the insights from this analysis suggest a clear opportunity for product improvement. Reformulating the drink to enhance flavor or offering new flavored variants could significantly increase customer satisfaction and loyalty. Addressing these concerns could also help the company better compete in a crowded market and avoid further reputational damage from recurring negative feedback.




