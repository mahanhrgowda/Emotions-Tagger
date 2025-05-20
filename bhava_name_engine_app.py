import streamlit as st
import pandas as pd
from bhava_guesser import guess_bhava_tags
from bhava_card_export import get_card_png_bytes
from bhava_csv_batch_processor import process_csv
import tempfile

st.set_page_config(page_title="Bhāva Name Engine", page_icon="🕉", layout="centered")
st.title("🌸 Bhāva Name Engine by Mahān !!!")
st.markdown("Map your name to its **emotive essence**, **chakra flow**, and **Rasa** — inspired by Sanskrit phonetics and classical dramaturgy.")

st.header("🔤 Single Name Bhāva Tagger")
name_input = st.text_input("Enter a name:")
if name_input:
    tags = guess_bhava_tags(name_input)
    if tags:
        st.success("✨ Bhāva Tags:")
        for bhava, chakra, rasa, color in tags:
            st.markdown(f"<div style='padding:10px;margin:5px;border-radius:10px;background:{color};color:white'><b>{chakra}</b> • {bhava} • <i>{rasa}</i></div>", unsafe_allow_html=True)
        png_data = get_card_png_bytes(name_input, tags)
        st.download_button("📥 Download Bhāva Card (PNG)", data=png_data, file_name=f"{name_input}_bhava_card.png", mime="image/png")
    else:
        st.warning("No Bhāva tags could be confidently inferred.")

st.divider()
st.header("📁 Batch Bhāva Tagging (CSV Upload)")
uploaded_file = st.file_uploader("Upload CSV with a 'Name' column", type=['csv'])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file.flush()
        df_out = process_csv(temp_file.name)
    st.success("✅ Processed Bhāva Tags:")
    st.dataframe(df_out)
    csv = df_out.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Tagged CSV", data=csv, file_name="Bhava_Tagged_Names.csv", mime='text/csv')
st.markdown("---")
st.markdown("🧬 Powered by Maheshwara Sūtras • Rasa Theory • Sanskrit Sound Science")
