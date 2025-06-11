from google import genai
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ["GEMINI_KEY_API"]

def get_car_ai_bio(model, brand, year):
    client = genai.Client(api_key=api_key)

    
    my_prompt = f"""Me mostre uma descrição de venda para o carro {model} {brand} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo de carro."""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents= my_prompt
)
    return response.text
