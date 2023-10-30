import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo"

class GptObject:
    def query_to_response(self, input_prompt):

        response = openai.ChatCompletion.create(
          model=MODEL,
          messages=input_prompt['messages'],
          temperature=0,
          max_tokens=1024
        )

        return response

    def get_sql_query(self, gpt_response):
            return gpt_response['choices'][0]['message']['content']