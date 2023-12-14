import streamlit as st
import base64
def embed_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        data = f.read()
    base64_pdf = base64.b64encode(data).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf">'
    styled_container = f"""
    <div style="
        background-color: #f4f4f4;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
    ">
        <h2 style="color: #3498db; text-align: center;">PDF Viewer</h2>
        <div style="margin-top: 20px;">{pdf_display}</div>
    </div>
    """
    
    st.markdown(styled_container, unsafe_allow_html=True)

# Example usage
pdf_path = "assets/whitepaper.pdf"
st.set_page_config(page_title="White Paper", page_icon="📚")
st.title("White Paper")
embed_pdf(pdf_path)
