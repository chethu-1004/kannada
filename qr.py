import streamlit as st
from urllib.parse import urlencode

# ==========================================
# CONFIGURATION
# ==========================================

UPI_ID = "chethann2005@axl"
PAYEE_NAME = "CHETHAN N"

FEES = {
    "Men": 1000,
    "Women": 500,
    "2nd year, 3rd year Juniors": 500,
}

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Kannada Rajyotsava Payment",
    page_icon="💛❤️",
    layout="centered",
)

# ==========================================
# KARNATAKA FLAG THEME
# ==========================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            135deg,
            #fff4b8 0%,
            #fffafa 45%,
            #ffe0e0 100%
        );
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        color: #b30000 !important;
        font-weight: 800 !important;
    }

    .karnataka-banner {
        background: linear-gradient(
            to bottom,
            #ffcc00 0%,
            #ffcc00 50%,
            #d71920 50%,
            #d71920 100%
        );
        padding: 8px;
        border-radius: 12px;
        margin-bottom: 20px;
    }

    .stTextInput input {
        border: 2px solid #d71920;
        border-radius: 8px;
    }

    .stSelectbox div[data-baseweb="select"] {
        border-radius: 8px;
    }

    .stButton button,
    .stDownloadButton button,
    .stLinkButton a {
        background: linear-gradient(90deg, #d71920, #a50000) !important;
        color: white !important;
        border: 2px solid #ffcc00 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        padding: 12px !important;
    }

    div[data-testid="stMarkdownContainer"] div[style*="background-color:#e8f5e9"] {
        background: linear-gradient(135deg, #fff0a6, #ffe0e0) !important;
        border: 2px solid #d71920;
        border-radius: 15px;
    }

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    hr {
        border-color: #d71920 !important;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# MAIN APPLICATION
# ==========================================

st.title("💛❤️ Kannada Rajyotsava Payment Portal")

st.write(
    "Welcome! Enter your details, select your category "
    "and complete your payment."
)

st.divider()

# ==========================================
# STUDENT DETAILS
# ==========================================

st.subheader("👤 Student Details")

name = st.text_input(
    "Enter Your Full Name",
    key="student_name",
)

department = st.selectbox(
    "Select Department",
    [
        "Select Department",
        "AIML",
        "ISE",
        "CSE",
        "ECE",
        "EEE",
        "ME",
        "CIVIL",
        "Other",
    ],
)

category = st.selectbox(
    "Select Your Category",
    [
        "Select Category",
        "Men",
        "Women",
        "2nd year, 3rd year Juniors",
    ],
)

# ==========================================
# PAYMENT DETAILS
# ==========================================

if category != "Select Category":
    amount = FEES[category]

    st.divider()
    st.subheader("💰 Payment Summary")

    st.write(f"**Name:** {name if name else 'Not entered'}")
    st.write(f"**Department:** {department}")
    st.write(f"**Category:** {category}")

    st.markdown(
        f"""
        <div style="
            background-color:#e8f5e9;
            padding:25px;
            border-radius:12px;
            text-align:center;
        ">
            <h3 style="color:#166534;">Total Amount</h3>
            <h1 style="color:#15803d;">₹{amount:,}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # ======================================
    # DIRECT UPI PAYMENT
    # ======================================

    st.subheader("📲 Make Payment")

    payment_data = {
        "pa": UPI_ID,
        "pn": PAYEE_NAME,
        "am": str(amount),
        "cu": "INR",
        "tn": f"Kannada Rajyotsava - {name}",
    }

    upi_link = "upi://pay?" + urlencode(payment_data)

    if name.strip() and department != "Select Department":
        st.link_button(
            f"💳 PAY NOW - ₹{amount:,}",
            upi_link,
            type="primary",
            use_container_width=True,
        )

        st.info(
            "Click PAY NOW to open a compatible UPI application. "
            "Verify the recipient and amount before confirming payment."
        )
    else:
        st.warning("Please enter your name and select your department.")

# ==========================================
# FOOTER
# ==========================================

st.divider()
st.caption("💛❤️ Kannada Rajyotsava Management | Payment Portal")
