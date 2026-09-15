import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Food Recipe AI",
    page_icon="🍳"
)

st.title("🍳 Food Recipe AI")
st.subheader("ระบบแนะนำเมนูอาหารและสูตรอาหารด้วย AI")

st.write("อัปโหลดรูปอาหารเพื่อดูข้อมูลเมนูและสูตรอาหาร")

uploaded_file = st.file_uploader(
    "📷 เลือกรูปอาหาร",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="รูปอาหารที่เลือก",
        use_container_width=True
    )

    st.success("✅ อัปโหลดรูปอาหารสำเร็จ")

    st.subheader("🍽️ เมนูอาหาร")
    st.write("กะเพราหมูสับ")

    st.subheader("🥬 วัตถุดิบ")
    st.write("""
    - หมูสับ
    - ใบกะเพรา
    - กระเทียม
    - พริก
    - น้ำปลา
    - ซอสปรุงรส
    """)

    st.subheader("👨‍🍳 วิธีทำ")
    st.write("""
    1. โขลกกระเทียมและพริก
    2. ผัดกระเทียมและพริกให้หอม
    3. ใส่หมูสับและผัดให้สุก
    4. ใส่ใบกะเพราและปรุงรส
    5. ผัดให้เข้ากัน พร้อมรับประทาน
    """)

    st.subheader("💡 ข้อมูลโภชนาการโดยประมาณ")
    st.write("พลังงานประมาณ 450 kcal ต่อ 1 จาน")