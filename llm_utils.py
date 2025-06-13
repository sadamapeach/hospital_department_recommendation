import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# PENGECEKAN MODEL GEMINI
# models = genai.list_models()
# for m in models:
#     print(m.name, "→", m.supported_generation_methods)

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def get_recommended_department(gender: str, age: int, symptoms: list[str]) -> str:
    prompt = f"""
    Berdasarkan informasi pasien berikut:
    - Jenis Kelamin: {gender}
    - Umur: {age}
    - Gejala: {', '.join(symptoms)}

    Departemen rumah sakit mana yang paling sesuai untuk pasien ini?
    Jawab dengan nama departemen saja, misal: Neurology.
    """
    try:
        response = model.generate_content(prompt)
        department = response.text.strip()
        return department
    except Exception as e:
        raise Exception(f"Gagal mendapatkan rekomendasi: {e}")