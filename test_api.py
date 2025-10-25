# gemini_simple.py
import os
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


# --- Cấu hình API key ---
os.environ["GOOGLE_API_KEY"] = "AIzaSyC2yA-VkIroULlcEkcb3yAIH7haoqLo91w"

# --- Khởi tạo model Gemini ---
chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def simple_gemini_answer(prompt: str):
    """
    Gửi prompt tới Gemini và trả về phản hồi dạng văn bản.
    """
    try:
        response = chat.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"Lỗi khi gọi Gemini API: {e}"

# --- Test nhanh ---
if __name__ == "__main__":
    prompt = "Bạn là chuyên gia tim mạch. Giải thích ngắn gọn nguy cơ bệnh tim cho người 45 tuổi, nam giới."
    answer = simple_gemini_answer(prompt)
    print("🎯 Gemini trả lời:")
    print(answer)
