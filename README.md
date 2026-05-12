<div align="center">

# 📸 SnapClass

### AI-Powered Attendance Management System

*Take attendance in seconds — no roll calls, no paperwork, just faces.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## 🎯 What is SnapClass?

SnapClass is a smart classroom attendance system that uses **facial recognition** and **voice verification** to mark students present — automatically. No more calling names, no more forged signatures. Teachers snap a photo, AI does the rest.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **Face Recognition Login** | Students log in and get marked present via webcam — no passwords needed |
| 🎙️ **Voice Enrollment** | Optional voice biometric for added verification |
| 👨‍🏫 **Teacher Dashboard** | Take attendance, manage subjects, and view full session history |
| 🎓 **Student Dashboard** | See enrolled subjects, attendance stats, and personal records |
| 📊 **Attendance Records** | Per-session logs with timestamps, subject info, and present/absent status |
| 🔐 **Secure Storage** | Passwords hashed with bcrypt; embeddings stored in Supabase |
| 📱 **QR Code Support** | QR-based subject enrollment for students |

---

## 🛠️ Tech Stack

- **Frontend / UI** — [Streamlit](https://streamlit.io)
- **Face Recognition** — `face_recognition`, `dlib`, `scikit-learn`
- **Voice Verification** — `resemblyzer`, `librosa`
- **Database** — [Supabase](https://supabase.com) (PostgreSQL)
- **Image Processing** — `Pillow`, `NumPy`
- **Data Handling** — `pandas`
- **Auth Security** — `bcrypt`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [Supabase](https://supabase.com) project (free tier works)
- Webcam (for face recognition)

### Installation

# 1. Clone the repository
git clone https://github.com/Rohanthanvi/snapclass-rohan-main.git
cd snapclass-rohan-main

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your Supabase credentials
# Create a .streamlit/secrets.toml file and add:
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_anon_key"

# 4. Run the app
streamlit run app.py

---

## 📁 Project Structure

snapclass-rohan-main/
├── app.py                    # Entry point
├── requirements.txt
├── .streamlit/
│   └── config.toml           # Streamlit theme config
└── src/
    ├── components/           # UI components (header, footer, cards, dialogs)
    ├── database/
    │   └── db.py             # All Supabase queries
    ├── pipelines/
    │   ├── face_pipeline.py  # Face embedding, training, prediction
    │   └── voice_pipeline.py # Voice embedding
    ├── screens/              # Teacher & Student dashboard screens
    └── ui/
        └── base_layout.py    # Layout and background utilities

---

## 🖥️ How It Works

Student opens app
      ↓
Webcam captures face
      ↓
Face embedding extracted → compared against stored embeddings
      ↓
Match found → Student logged in + marked present
      ↓
Attendance record saved to Supabase with timestamp & subject

For new students, the app prompts registration — capturing their face (and optionally voice) to build their profile on the spot.

---

## 🔒 Security Notes

- Facial embeddings are stored as float vectors, not raw images
- All passwords are hashed using `bcrypt` before storage
- Supabase Row Level Security (RLS) is recommended for production use

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author

**Rohan Thanvi**
- GitHub: [@Rohanthanvi](https://github.com/Rohanthanvi)

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
  <sub>Built with ❤️ using Streamlit, face_recognition, and Supabase</sub>
</div>
