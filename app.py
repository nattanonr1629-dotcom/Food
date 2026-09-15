import streamlit as st
from PIL import Image
from openai import OpenAI
import base64

# =========================
# ตั้งค่าหน้าแอป
# =========================
st.set_page_config(
    page_title="Food Recipe AI",
    page_icon="🍳",
    layout="wide"
)

# =========================
# CSS ตกแต่ง
# =========================
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.box {
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #dddddd;
    margin-bottom: 15px;
}

.small-title {
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# หัวข้อ
# =========================
st.markdown(
    '<div class="main-title">🍳 Food Recipe AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">🤖 ระบบวิเคราะห์อาหารและแนะนำสูตรอาหารด้วย AI</div>',
    unsafe_allow_html=True
)

st.info(
    "📷 อัปโหลดรูปอาหาร แล้วให้ AI วิเคราะห์ชื่อเมนู "
    "วัตถุดิบ วิธีทำ โภชนาการ และเมนูใกล้เคียง"
)

# =========================
# อ่าน API Key
# =========================
try:
    with open("key.txt", "r", encoding="utf-8") as f:
        api_key = f.read().strip()

    if not api_key:
        st.error("❌ ไม่พบ API Key ในไฟล์ key.txt")
        st.stop()

    client = OpenAI(api_key=api_key)

except Exception:
    st.error("❌ ไม่สามารถโหลด API Key ได้ กรุณาตรวจสอบไฟล์ key.txt")
    st.stop()

# =========================
# อัปโหลดรูป
# =========================
uploaded_file = st.file_uploader(
    "📷 เลือกรูปอาหาร",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    # =========================
    # รูปอาหาร
    # =========================
    with col1:
        st.markdown("### 📸 รูปอาหาร")
        st.image(
            image,
            caption="รูปอาหารที่อัปโหลด",
            width="stretch"
        )

    # =========================
    # วิเคราะห์ AI
    # =========================
    with col2:
        st.markdown("### 🤖 Food Recipe AI")

        image_bytes = uploaded_file.getvalue()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        file_type = uploaded_file.type
        prompt = """
วิเคราะห์รูปอาหารนี้และตอบเป็นภาษาไทย โดยให้ข้อมูลดังนี้:

1. 🍽️ ชื่อเมนูอาหาร
2. 🥬 วัตถุดิบที่คาดว่าใช้
3. 👨‍🍳 วิธีทำโดยสรุป
4. 🥗 ข้อมูลโภชนาการโดยประมาณ
5. 💡 เมนูอาหารที่ใกล้เคียง

หากไม่แน่ใจ ให้ระบุว่าไม่สามารถยืนยันได้
และอย่าสร้างข้อมูลที่ไม่สามารถประเมินจากภาพได้
"""

        with st.spinner("🤖 AI กำลังวิเคราะห์รูปอาหาร..."):
            try:
                response = client.responses.create(
                    model="gpt-5.6-luna",
                    input=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "input_text",
                                    "text": prompt
                                },
                                {
                                    "type": "input_image",
                                    "image_url": f"data:{file_type};base64,{image_base64}"
                                }
                            ]
                        }
                    ]
                )

                result = response.output_text

                st.success("✅ วิเคราะห์อาหารสำเร็จ")
                st.markdown("### 🍽️ ผลการวิเคราะห์")
                st.write(result)

            except Exception as e:
                st.error("❌ เกิดข้อผิดพลาดในการวิเคราะห์")
                st.write(str(e))

       