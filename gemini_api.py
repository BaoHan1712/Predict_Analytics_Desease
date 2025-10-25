import os
import json
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from rule_prompt import BASE_RULES  # 🔥 import quy tắc nền

# --- Cấu hình API ---
os.environ["GOOGLE_API_KEY"] = "AIzaSyC2yA-VkIroULlcEkcb3yAIH7haoqLo91w"

# --- Khởi tạo model Gemini ---
chat = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# --- Hàm phân tích bằng Gemini ---
def analyze_with_gemini(user_data: dict, result: dict) -> str:
    # Tạo prompt tự nhiên, thân thiện và hướng dẫn rõ ràng
    prompt = f"""
{BASE_RULES}

📋 **DỮ LIỆU BỆNH NHÂN:**
{json.dumps(user_data, ensure_ascii=False, indent=2)}

💡 **KẾT QUẢ DỰ ĐOÁN MÔ HÌNH:**
{result['message']}  
🔢 Xác suất nguy cơ: {result['probability']}%

🩺 Hãy đóng vai một bác sĩ tim mạch tận tâm, nói chuyện tự nhiên và dễ hiểu.
Phân tích ý nghĩa từng chỉ số nếu cần, sau đó đánh giá tình trạng tim mạch tổng thể.
Dựa vào kết quả dự đoán và thông số, hãy:
1️⃣ Nêu tình trạng sức khỏe tổng quan của bệnh nhân  
2️⃣ Phân tích nguyên nhân hoặc yếu tố rủi ro chính  
3️⃣ Đưa ra lời khuyên về chế độ ăn uống phù hợp 🍎  
4️⃣ Gợi ý về vận động, thể dục 💪  
5️⃣ Hướng dẫn theo dõi và tái khám định kỳ 🏥  

⚠️ Viết ngắn gọn, súc tích, thân thiện — giống như bạn đang tư vấn cho bệnh nhân thật.  
Trả về **văn bản thuần túy**, không định dạng JSON, không thêm tiêu đề kỹ thuật.
"""

    try:
        # --- Gọi Gemini ---
        response = chat.invoke([HumanMessage(content=prompt)])
        text_output = response.content.strip()

        # Làm sạch kết quả để UI hiển thị đẹp hơn
        text_output = text_output.replace("**", "").replace("##", "").strip()

        return text_output

    except Exception as e:
        print("⚠️ Lỗi gọi Gemini:", e)
        return (
            "⚠️ Lỗi khi phân tích dữ liệu. "
            "Vui lòng kiểm tra lại kết nối API hoặc định dạng dữ liệu đầu vào."
        )


# --- Test nhanh ---
if __name__ == "__main__":
    sample_user = {
        "age": 23.0, "sex": 1.0, "cp": 1.0, "trestbps": 123.0,
        "chol": 123.0, "fbs": 1.0, "restecg": 1.0, "thalach": 123.0,
        "exang": 1.0, "oldpeak": 1.0, "slope": 0.0, "ca": 1.0, "thal": 2.0
    }
    result = {"message": "🧠 Nguy cơ bệnh tim nhẹ", "probability": 42.7}
    text = analyze_with_gemini(sample_user, result)
    print("\n🎯 PHÂN TÍCH TỪ GEMINI:\n", text)
