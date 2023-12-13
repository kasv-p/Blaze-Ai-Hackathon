
import streamlit as st

# Sample data
mkr_data = {
    "Overview": {
        "Position and Functionality": "Maker (MKR) is a cryptocurrency and a governance token associated with the MakerDAO platform, which operates on the Ethereum blockchain. MakerDAO is a decentralized autonomous organization (DAO) that enables the creation of a stablecoin called DAI.",
        "Popularity": "As of today, Maker holds the position of #57 in the Coinbase ranking."
    },
    "Key Metrics": {
        "Market Cap": "₹103.4B",
        "Trading Volume": "₹6.97B",
        "Price": "₹112,874.91"
    },
    "Tokenomics": {
        "Token Supply": "Circulating supply: 918,769 coins, Maximum supply: 1,005,577 coins",
        "Distribution": "Founders and projects: 69.50%, Team: 15.0%, Seed Round 1: 4.0%, Seed Round 2: 6.0%, Seed Round 3: 5.5%",
        "Image":"assets/1.png"
    }
}

st.set_page_config(page_title="Maker (MKR) Cryptocurrency Information", page_icon="📈")
st.title("Maker (MKR) Cryptocurrency Information")

st.sidebar.title("Navigation")
section_option = st.sidebar.selectbox("Go to", list(mkr_data.keys()))

for section, content in mkr_data.items():
    if section == section_option:
        st.header(section)
        for key, value in content.items():
            
            if key=="Image":
                st.image(value)
            else:
                st.subheader(key)
                st.write(value)
