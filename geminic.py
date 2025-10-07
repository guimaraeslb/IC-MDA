from google import genai
import dotenv
import os

dotenv.load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_video_content_description(videoTitle):
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents= "Explique, em APENAS um parágrafo, os principais argumentos mencionados no vídeo do YouTube com titulo " +videoTitle
    )
    print("Resumo retornado com sucesso! ✅")
    return response.text