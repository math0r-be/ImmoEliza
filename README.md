# ImmoEliza - Real Estate Price Prediction Platform 🏠💻

A complete solution for real estate price estimation combining machine learning with modern web technologies.

## ✨ Key Features
- 🚀 FastAPI backend for robust predictions
- 📊 Streamlit-powered interactive frontend
- 🛠️ Machine learning integration
- 🌍 Render.com cloud deployment
- 🔄 CORS-enabled secure communication

<<<<<<< HEAD
---

## 🚀 Live Demo

👉 https://immo-streamlit.onrender.com/

---

## 💡 What this app does

- Takes user input through a simple web interface (Streamlit)
- Predicts the property price using random forest regression model
- Displays the predicted price

---


=======
## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/matho/ImmoEliza.git
cd ImmoEliza

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

## 🖥️ Usage

```bash
# Start backend API
uvicorn src.api.routes:app --reload

# Launch frontend (in separate terminal)
streamlit run frontend/streamlit_app.py
```

## ☁️ Deployment
1. **Backend API** (FastAPI):
   - Create new Web Service on Render
   - Set environment: `Python 3.9+`
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn src.api.routes:app --host 0.0.0.0 --port $PORT`

2. **Frontend** (Streamlit):
   - Create new Web Service on Render
   - Select "Streamlit" environment
   - Point to `frontend/streamlit_app.py`

## 📂 Project Structure
```
ImmoEliza/
├── data/               # Training datasets
├── frontend/           # Streamlit interface
│   └── streamlit_app.py
├── src/
│   ├── api/            # FastAPI components
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── model.py
│   └── ml/             # Machine learning models
│       ├── train.py
│       └── model.pkl
├── requirements.txt
└── README.md
```

## 🤝 Contribution
```bash
1. Fork the repository
2. Create feature branch (git checkout -b feature/amazing-feature)
3. Commit changes (git commit -m 'Add amazing feature')
4. Push to branch (git push origin feature/amazing-feature)
5. Open Pull Request
```

## 📄 License
MIT License - See [LICENSE](LICENSE) for details

---

🔗 **Live Demo**: [Streamlit App](https://immoeliza.onrender.com) | [API Documentation](https://immo-api.onrender.com/docs)
>>>>>>> 329849c (debug prediction error after deployement)
