# Mini Project - FastAPI Recommendation System

## Description
Proyek ini adalah aplikasi FastAPI sederhana untuk memberikan rekomendasi berdasarkan input user, menggunakan layanan API dari Google Gemini.

Adapun input user merupakan data pasien yang mencakup:  
    - Gender  
    - Age  
    - Symptoms

Dari data pasien ini akan muncul departemen rumah sakit yang sesuai.

## Fitur
- Endpoint rekomendasi ('/recommend')
- Swagger UI tersedia di '/docs'
- Konfigurasi API key melalui file '.env'

---

## Instalasi
1. **Clone repositori**  
    '''bash  
    git clone https://github.com/username/name-repo.git  
    cd nama-repo
2. **Buat dan aktifkan virtual environment**  
    python -m venv venv  
    '''bash
    source venv/Scripts/activate
3. **Install dependencies**  
    pip install -r requirements.txt

## Konfigurasi Environment
1. **Salin file .env.example ke .env**  
    '''bash  
    cp .env.example .env
2. **Masukkan api key anda**  
    GOOGLE_API_KEY=your_google_api_key_here

## Menjalankan Aplikasi
'''bash  
uvicorn main:app --reload

Buka di browser:
- API root: http://127.0.0.1:8000  
- Swagger Docs: http://127.0.0.1:8000/docs
