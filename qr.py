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
# KARNATAKA FLAG THEME + READABLE TEXT
# ==========================================

st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background: linear-gradient(
            135deg,
            #fff4b8 0%,
            #fffafa 45%,
            #ffe0e0 100%
        );
        color: #000000 !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Keep only the main page title red */
    h1 {
        color: #b30000 !important;
        font-weight: 800 !important;
    }

    /* All other headings and normal text black */
    h2, h3, h4, h5, h6,
    p, label, li, span, small,
    [data-testid="stMarkdownContainer"],
    [data-testid="stCaptionContainer"],
    [data-testid="stWidgetLabel"] {
        color: #000000 !important;
    }

    h2, h3, h4, h5, h6 {
        font-weight: 800 !important;
    }

    /* Text input: white field with black entered text */
    .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 2px solid #b30000 !important;
        border-radius: 8px !important;
    }

    .stTextInput input::placeholder {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    opacity: 1 !important;
    }

    /* Select box: white background and black selected value */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 1px solid #b30000 !important;
        border-radius: 8px !important;
    }

    .stSelectbox div[data-baseweb="select"] *,
    [data-baseweb="popover"] *,
    [role="listbox"] *,
    [role="option"] {
        color: #000000 !important;
    }

    [data-baseweb="popover"],
    [role="listbox"],
    [role="option"] {
        background-color: #ffffff !important;
    }

    /* High-contrast buttons: yellow background and black text */
    .stButton button,
    .stDownloadButton button,
    .stLinkButton a {
        background: #ffcc00 !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 2px solid #b30000 !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        padding: 12px !important;
    }

    .stButton button *,
    .stDownloadButton button *,
    .stLinkButton a * {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Payment amount card: black text for readability */
    div[data-testid="stMarkdownContainer"] div[style*="background-color:#e8f5e9"] {
        background: linear-gradient(135deg, #fff0a6, #ffe0e0) !important;
        border: 2px solid #b30000 !important;
        border-radius: 15px !important;
    }

    div[data-testid="stMarkdownContainer"] div[style*="background-color:#e8f5e9"] h1,
    div[data-testid="stMarkdownContainer"] div[style*="background-color:#e8f5e9"] h3 {
        color: #000000 !important;
    }

    /* Alert boxes */
    div[data-testid="stAlert"] {
        border-radius: 10px !important;
    }

    div[data-testid="stAlert"] *,
    [data-testid="stNotification"] * {
        color: #000000 !important;
    }

    /* Dividers and footer */
    hr {
        border-color: #b30000 !important;
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
            background: linear-gradient(135deg, #fff0a6, #ffe0e0);
            padding: 25px;
            border: 2px solid #b30000;
            border-radius: 12px;
            text-align: center;
        ">
            <h3 style="color:#000000;">Total Amount</h3>
            <h1 style="color:#000000;">₹{amount:,}</h1>
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
