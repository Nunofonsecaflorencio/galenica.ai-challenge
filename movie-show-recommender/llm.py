from openai import OpenAI
import json
import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get("GALENICA_OPEN_AI_KEY")

class Recommender:
    def __init__(self):
        self.client = OpenAI(api_key=SECRET_KEY)
    
    def _prompt(self, prompt):
        self.completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are a helpful assistant that specializes in providing movie and TV show recommendations. Always respond in valid JSON format."},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return self.completion.choices[0].message.content
    
    def recommend(self, user_input):
        prompt = (
                f"Based on the following input: '{user_input}', recommend ONLY 2 highly rated movies and TV shows. "
                "Provide two separate lists: one for movies and one for TV shows. "
                "For each item, include the title and a brief, engaging description. "
                "Ensure the response is in this exact JSON format (Nothing more than JSON):\n\n"
                "{\n"
                "  \"movies\": [\n"
                "    {\"title\": \"Movie Title 1\", \"description\": \"Short description of Movie 1.\"},\n"
                "    {\"title\": \"Movie Title 2\", \"description\": \"Short description of Movie 2.\"}\n"
                "  ],\n"
                "  \"tv_shows\": [\n"
                "    {\"title\": \"TV Show Title 1\", \"description\": \"Short description of TV Show 1.\"},\n"
                "    {\"title\": \"TV Show Title 2\", \"description\": \"Short description of TV Show 2.\"}\n"
                "  ]\n"
                "}\n\n"
                "Replace placeholders with actual recommendations based on the user's input."
            )
        
        response = self._prompt(prompt)
        print("\nRESPONSE: ", response, "\n")
        as_json = json.loads(response)
        
        return (
            self.make_dataframe(as_json["movies"]),
            self.make_dataframe(as_json["tv_shows"])
        )
    
    def make_dataframe(self, data_object): # Chat GPT
        # Create DataFrame from the data object
        df = pd.DataFrame(data_object)
        
        # Add Rank column
        df["Rank"] = [f"#{i+1}" for i in range(len(df))]
        
        # Reorder columns to place Rank first
        df = df[["Rank"] + list(df.columns[:-1])]  # Exclude the original 'Rank' column added at the end
        
        
        # Capitalize headers
        return df.rename(columns=str.capitalize)
        
    