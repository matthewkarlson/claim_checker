from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from prompts import system_prompt

# Define Claim models
class Claim(BaseModel):
    description: str
    verifiable: bool
    opinion: bool

class Claims(BaseModel):
    claims: list[Claim]

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

def extract_claims(file_path: str, model_name: str = "gpt-4o") -> Claims:
    """
    Reads a transcript file and extracts claims using OpenAI's API.
    
    Args:
        file_path (str): The path to the transcript file.
        model_name (str, optional): The OpenAI model to use. Defaults to "gpt-4o".
    
    Returns:
        Claims: A Pydantic object containing a list of claims.
    """
    # Read the contents of the transcript file
    with open(file_path, 'r', encoding='utf-8') as file:
        transcript = file.read()

    # API call to OpenAI
    completion = client.beta.chat.completions.parse(
        model=model_name,
        messages=[
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": transcript}
        ],
        response_format=Claims
    )
    
    # Return the parsed claims object
    return completion.choices[0].message.parsed

# Example usage:
# claims_data = extract_claims("transcript.txt")
# print(claims_data)
