from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
from gemini_api import analyze_with_gemini  # import hàm AI Gemini

app = Flask(__name__)

# --- Load mô hình ---
with open("xgb_heart_model.pkl", "rb") as f:
    model = pickle.load(f)
print("✅ Model đã load thành công!")

# --- Các cột đặc trưng ---
COLUMNS = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # 🧩 Lấy dữ liệu từ form
        user_input = {col: float(request.form[col]) for col in COLUMNS}
        df_input = pd.DataFrame([user_input])

        # 🔍 Dự đoán bằng mô hình ML
        prediction = model.predict(df_input)[0]
        prob = model.predict_proba(df_input)[0][1]

        result = {
            "prediction": int(prediction),
            "probability": round(prob * 100, 2),
            "message": "🧠 Có nguy cơ mắc bệnh tim"
            if prediction == 1
            else "💖 Không có nguy cơ mắc bệnh tim"
        }

        print("\n📥 User input:", user_input)
        print("📊 Model Output:", result)

        # 🤖 Gọi AI Gemini để phân tích text
        gemini_text = analyze_with_gemini(user_input, result)
        print("\n🎯 PHÂN TÍCH TỪ GEMINI:\n", gemini_text)

        # 🧱 Gửi trả về UI JSON text
        response_data = {"analysis_text": gemini_text}
        return jsonify(response_data)

    except Exception as e:
        print("❌ Lỗi:", e)
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
