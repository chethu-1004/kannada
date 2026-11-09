import streamlit as st
from urllib.parse import urlencode
from datetime import datetime
from io import BytesIO
import uuid

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# ==========================================
# CONFIGURATION
# ==========================================

UPI_ID = "chethann2005@axl"
PAYEE_NAME = "CHETHAN N"

FEES = {
    "Men": 1000,
    "Women": 500,
    "2nd year, 3rd year Juniors": 500
}


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    
    page_title="Kannada Rajyotsava Payment",
    page_icon="💛❤️",
    layout="centered"
)
# ==========================================
# KARNATAKA FLAG THEME
# ==========================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(
        135deg,
        #fff4b8 0%,
        #fffafa 45%,
        #ffe0e0 100%
    );
}

/* Main content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main headings */
h1, h2, h3 {
    color: #b30000 !important;
    font-weight: 800 !important;
}

/* Karnataka flag banner */
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

/* Input fields */
.stTextInput input {
    border: 2px solid #d71920;
    border-radius: 8px;
}

/* Select boxes */
.stSelectbox div[data-baseweb="select"] {
    border-radius: 8px;
}

/* Buttons */
.stButton button,
.stDownloadButton button,
.stLinkButton a {
    background: linear-gradient(
        90deg,
        #d71920,
        #a50000
    ) !important;
    color: white !important;
    border: 2px solid #ffcc00 !important;
    border-radius: 10px !important;
    font-weight: bold !important;
    padding: 12px !important;
}

/* Payment amount card */
div[data-testid="stMarkdownContainer"] div[style*="background-color:#e8f5e9"] {
    background: linear-gradient(
        135deg,
        #fff0a6,
        #ffe0e0
    ) !important;
    border: 2px solid #d71920;
    border-radius: 15px;
}

/* Success messages */
div[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Dividers */
hr {
    border-color: #d71920 !important;
}

/* Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PDF RECEIPT GENERATOR
# ==========================================

def generate_receipt(
    receipt_no,
    name,
    department,
    category,
    amount,
    transaction_id,
    payment_date
):

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4

    # Heading
    pdf.setFont("Helvetica-Bold", 19)

    pdf.drawCentredString(
        width / 2,
        height - 70,
        "💛❤️KANNADA RAJYOTSAVA"
    )

    pdf.setFont("Helvetica-Bold", 16)

    pdf.drawCentredString(
        width / 2,
        height - 100,
        "PAYMENT RECEIPT"
    )

    pdf.line(
        50, height - 125,
        width - 50, height - 125
    )

    # Receipt number
    pdf.setFont("Helvetica-Bold", 12)

    pdf.drawString(
        60,
        height - 165,
        f"Receipt No: {receipt_no}"
    )

    # Student details
    details = [
        ("Student Name", name),
        ("Department", department),
        ("Category", category),
        ("Amount Paid", f"Rs. {amount}"),
        ("UPI Transaction ID", transaction_id),
        ("Payment Date", payment_date),
        ("Payment Status", "SELF-REPORTED - NOT VERIFIED")
    ]

    y = height - 215

    for label, value in details:

        pdf.setFont("Helvetica-Bold", 11)

        pdf.drawString(
            70,
            y,
            label
        )

        pdf.setFont("Helvetica", 11)

        pdf.drawString(
            240,
            y,
            str(value)[:65]
        )

        y -= 38

    pdf.line(
        50, y,
        width - 50, y
    )

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawCentredString(
        width / 2,
        y - 45,
        "Thank you for participating!"
    )

    pdf.setFont("Helvetica", 9)

    pdf.drawCentredString(
        width / 2,
        y - 70,
        "Kannada Rajyotsava Management"
    )

    pdf.save()

    buffer.seek(0)

    return buffer.getvalue()


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
    key="student_name"
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
        "Other"
    ]
)

category = st.selectbox(
    "Select Your Category",
    [
        "Select Category",
        "Men",
        "Women",
        "2nd year, 3rd year Juniors"
    ]
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
        unsafe_allow_html=True
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
        "tn": f"Kannada Rajyotsava - {name}"
    }

    upi_link = "upi://pay?" + urlencode(payment_data)

    if name.strip() and department != "Select Department":

        st.link_button(
            f"💳 PAY NOW - ₹{amount:,}",
            upi_link,
            type="primary",
            use_container_width=True
        )

        st.info(
            "Click PAY NOW to open a compatible UPI application. "
            "Verify the recipient and amount before confirming payment."
        )

    else:

        st.warning(
            "Please enter your name and select your department."
        )


    # ======================================
    # PAYMENT CONFIRMATION DETAILS
    # ======================================

    st.divider()

    st.subheader("🧾 Payment Confirmation & Receipt")

    st.write(
        "After completing your UPI payment, enter your "
        "transaction reference number to generate your receipt."
    )

    transaction_id = st.text_input(
        "Enter UPI Transaction ID / UTR Number",
        placeholder="Enter your 12-digit UPI reference number"
    )

    payment_completed = st.checkbox(
        "I confirm that I have completed the UPI payment."
    )


    # ======================================
    # GENERATE RECEIPT
    # ======================================

    if st.button(
        "Generate Payment Receipt",
        type="primary",
        use_container_width=True
    ):

        if not name.strip():

            st.error("Please enter your name.")

        elif department == "Select Department":

            st.error("Please select your department.")

        elif not transaction_id.strip():

            st.error("Please enter your UPI transaction ID.")

        elif not payment_completed:

            st.error("Please confirm that you have completed payment.")

        else:

            receipt_no = (
                "KRS-"
                + datetime.now().strftime("%Y%m%d")
                + "-"
                + uuid.uuid4().hex[:6].upper()
            )

            payment_date = datetime.now().strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )

            receipt_pdf = generate_receipt(
                receipt_no,
                name,
                department,
                category,
                amount,
                transaction_id,
                payment_date
            )

            # Store receipt details
            st.session_state["receipt_pdf"] = receipt_pdf

            st.session_state["receipt_details"] = {
                "receipt_no": receipt_no,
                "name": name,
                "department": department,
                "category": category,
                "amount": amount,
                "transaction_id": transaction_id,
                "payment_date": payment_date
            }


    # ======================================
    # DISPLAY PAYMENT DETAILS
    # ======================================

    if "receipt_details" in st.session_state:

        details = st.session_state["receipt_details"]

        st.divider()

        st.success("Payment acknowledgement generated!")

        st.subheader("✅ Payment Details")

        st.write(f"**Receipt Number:** {details['receipt_no']}")

        st.write(f"**Student Name:** {details['name']}")

        st.write(f"**Department:** {details['department']}")

        st.write(f"**Category:** {details['category']}")

        st.write(f"**Amount:** ₹{details['amount']:,}")

        st.write(f"**Transaction ID:** {details['transaction_id']}")

        st.write(f"**Payment Date:** {details['payment_date']}")

        st.warning(
            "This receipt records student-submitted payment details. "
            "UPI payment success has not been independently verified."
        )

        st.divider()

        st.subheader("🖨️ Download / Print Receipt")

        st.download_button(
            label="📄 Download PDF Receipt",
            data=st.session_state["receipt_pdf"],
            file_name=f"{details['receipt_no']}.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        st.caption(
            "Open the downloaded PDF and press Ctrl + P to print your receipt."
        )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "💛❤️ Kannada Rajyotsava Management | Payment Portal"
)
