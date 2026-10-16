import streamlit as st
import time

st.set_page_config(page_title="تطبيق الفيديو", page_icon="🎬")

st.title("مرحباً بك في تطبيق الفيديو")
st.write("هنا يمكنك استعراض وتشغيل الفيديوهات بسهولة.")

# الشريط الجانبي
st.sidebar.title("إعدادات التطبيق")
st.sidebar.info("اختر نوع الفيديو والجودة المناسبة.")

# خيارات القائمة الجانبية
user_prompt = st.sidebar.text_area("أدخل فكرة الفيديو أو النص:")
col1, col2 = st.sidebar.columns(2)
with col1:
    category = st.selectbox("التصنيف", ["عام", "تعليمي", "ترفيهي"])
with col2:
    quality = st.selectbox("الجودة", ["عالية", "متوسطة"])

if st.sidebar.button("بدء إنشاء الفيديو"):
    if user_prompt:
        with st.spinner("جاري تنفيذ الطلب البرمجي..."):
            time.sleep(3)
        st.success("تم إنشاء الفيديو بنجاح!")
        # مثال لعرض فيديو افتراضي
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    else:
        st.sidebar.warning("الرجاء إدخال فكرة أو نص أولاً!")
