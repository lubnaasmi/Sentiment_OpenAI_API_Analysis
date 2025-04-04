from openai import OpenAI

client = OpenAI()
new_list = []

def get_sentiment(text: list) -> list:
    
    
    """
    
    """

    if not text:
        return "Wrong input. text must be an array of strings."
    
    for items in text:
        if str(items).isdigit():
            return "Wrong input. text must be an array of strings."
    
    
    system_prompt = """
    You are an expert in interpreting human sentiment across cultures.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
	    { "role": "developer",  "content": system_prompt },
        { "role": "user",  "content": prompt }
    ]
    )
    return (completion.choices[0].message.content).split()
    

    
