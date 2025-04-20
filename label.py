from openai import OpenAI

client = OpenAI()


def get_sentiment(text: list) -> list:
    
    """
    This function will interface with the gpt-4o-mini language model.

    Args : list of string reviews, text
        
    Returns : list of sentiments
    
    """

    if not text:
        return "Wrong input. text must be an array of strings."
    
    for items in text:
        if str(items).isdigit():
            return "Wrong input. text must be an array of strings."
    
    
    system_prompt = """
    You are an expert in interpreting human sentiments across cultures.
    """

    prompt = f"""
    please categorize the review as either positive, neutral, negative, or irrelevant.

    Use only a one-word response for each line. Do not include any numbers.
    Return exactly {len(text)} labels, one per review.
    Do NOT split reviews into multiple items, even if they contain multiple opinions.
    Only return one sentiment per line. No numbers. No extra text.
    Some reviews may contain HTML tags like <br> or <br /> — treat these as part of a single review.
    Return exactly one sentiment label per review line, even if the review contains multiple sentences or HTML tags.{text}
    """
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
	    { "role": "developer",  "content": system_prompt },
        { "role": "user",  "content": prompt }
    ]
    )
    return (completion.choices[0].message.content).split()
    

    
