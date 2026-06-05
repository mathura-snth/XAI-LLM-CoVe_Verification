from openai import OpenAI
import os
from dotenv import load_dotenv
import anthropic
import uuid
import google.generativeai as genai
from google.api_core import exceptions

load_dotenv('.env')
openai_api_key = os.getenv("OPENAI_API_KEY")
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
claud_api_key = os.getenv("CLAUD_API_KEY")
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
grok_api_key = os.getenv("GROK_API_KEY")

class LlmCalling:
    def __init__(self):
        pass

    def OpenAI_llm(self, prompt):
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content.strip()
    
    def llama_llm(self, prompt):
        client = OpenAI(
            base_url="https://router.huggingface.co/novita/v3/openai",
            api_key=huggingface_api_key,
        )

        completion = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        return completion.choices[0].message.content
    
    def claud_llm(self, prompt):
        client = anthropic.Anthropic(
        api_key=claud_api_key,
        )
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ],
            metadata={"user_id": str(uuid.uuid4())}
        )
        return message.content[0].text
    
    def deepseek_llm(self, prompt):
        client = OpenAI(api_key=deepseek_api_key, 
                        base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=False
        )

        return response.choices[0].message.content.strip()
    
    def grok_llm(self, prompt):
        client = OpenAI(
            api_key=grok_api_key,
            base_url="https://api.x.ai/v1",
        )
        # Send a basic reasoning query
        response = client.chat.completions.create(
            model="grok-3",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.2,  # lower temperature for more deterministic answers
        )
        return response.choices[0].message.content.strip()
    
    def gemini_llm(self,prompt):
        """
        Cette fonction envoie un prompt à l'API Gemini et retourne la réponse.
        """
        try:
            # Configurez la clé API pour la bibliothèque
            genai.configure(api_key=gemini_api_key)

            # Créez le modèle
            # Vous pouvez choisir d'autres modèles comme 'gemini-1.5-flash'
            model = genai.GenerativeModel('gemini-1.5-flash-latest')

            # Générez le contenu à partir du prompt
            response = model.generate_content(prompt)

            # Retournez le texte de la réponse en supprimant les espaces superflus
            return response.text.strip()
        except exceptions.PermissionDenied as e:
            return f"Erreur d'authentification: {e}"
        except exceptions.ResourceExhausted as e:
            return f"Quota dépassé: {e}"
        except exceptions.GoogleAPIError as e:
            return f"Erreur API Google: {e}"
        except Exception as e:
            return f"Erreur inattendue: {e}"


if __name__ == "__main__":
    llm =LlmCalling()
    print(llm.gemini_llm("qu'est-ce que l'xai"))