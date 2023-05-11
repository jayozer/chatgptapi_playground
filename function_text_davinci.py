# Old way of writing the function. 

# Define a function to convert the SQL dialect using the OpenAI ChatGPT API:
def convert_sql(sql, from_sql, to_sql):
    prompt = f"SQL Dialect Conversion:\n\nFrom SQL: {from_sql}\nTo SQL: {to_sql}\n\nInput SQL:\n{sql}\n\nOutput SQL:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"]
    )
    return response.choices[0].text

def convert_sql(sql, from_sql, to_sql):
    # Generate the prompt using the user inputs
    prompt = f"Convert the following {from_sql} SQL code to {to_sql}:\n\n{sql}"
    # Generate the completion using the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Extract the converted SQL code from the API response
    converted_sql = response.choices[0].text.strip()
    
    # Return the converted SQL code
    return converted_sql