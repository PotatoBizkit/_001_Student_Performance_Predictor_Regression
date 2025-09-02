# Student Performance Prediction API

This project uses a Linear Regression model to predict student exam scores.

## Files
- `_001_Student_Performance_Simple_Linear_Regression_Flask.py` → Flask API
- `_001_Student_Performance_Simple_Linear_Regression.pkl` → Trained model
- `_001_Student_Performance_Simple_Linear_Regression.ipynb` → Training notebook
- `requirements.txt` → Dependencies

## How to Run
1. Clone this repo
2. Create a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Start the server:
   ```bash
   python _001_Student_Performance_Simple_Linear_Regression_Flask.py
5. Test with curl / Postman:
   ```bash
   curl.exe -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"features\": [values_here]}"
