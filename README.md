# 🎓 SnapClass AI – Face and Voice Recognition Attendance System

## 📌 About the Project

SnapClass AI is an AI-powered attendance management system that uses **Face Recognition and Voice Recognition** to make attendance tracking smarter and more efficient.

The application provides separate interfaces for teachers and students, allowing users to manage attendance, subjects, schedules, and student information through an interactive dashboard.

## ✨ Key Features

- **Face Recognition:** Identifies users using facial recognition technology.
- **Voice Recognition:** Provides voice-based recognition functionality.
- **Student Dashboard:** Allows students to access their academic and attendance information.
- **Teacher Dashboard:** Helps teachers manage students, subjects, and attendance.
- **Subject Management:** Supports subject creation, enrollment, and sharing.
- **Database Integration:** Stores application data using Supabase.
- **Secure Authentication:** Uses bcrypt for password hashing.
- **Interactive Interface:** Built using Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | User interface and dashboard |
| Scikit-learn | Machine learning functionality |
| dlib | Facial recognition support |
| Librosa | Audio processing |
| Supabase | Database and backend services |
| bcrypt | Password hashing |
| Pandas & NumPy | Data handling |
| Pillow | Image processing |
| Segno | QR code generation |
| Altair | Data visualization |

## 📂 Project Structure

```text
SnapClass-AI/
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/moditarushi/SnapClass-AI.git
cd SnapClass-AI
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

For macOS/Linux:

```bash
source venv/bin/activate
```

**4. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**5. Configure Supabase**

Add your Supabase URL and API key to your local Streamlit secrets configuration. Never upload secret credentials to GitHub.

**6. Run the application**

```bash
streamlit run app.py
```

## 🎯 Project Objective

The objective of SnapClass AI is to simplify attendance management by exploring AI-based face and voice recognition technologies. It aims to reduce manual work, improve convenience, and provide an organized platform for teachers and students.

## 👩‍💻 Author

**Tarushi Modi**

GitHub: [@moditarushi](https://github.com/moditarushi)

---

⭐ If you find this project interesting, feel free to explore the repository!

**SnapClass AI – Making Attendance Smarter with AI.**
