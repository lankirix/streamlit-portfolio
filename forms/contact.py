import re
import streamlit as st
import requests  # pip install requests

# Retrieve the webhook URL from Streamlit secrets
WEBHOOK_URL = st.secrets["WEBHOOK_URL"]


def is_valid_email(email):
    """Validate email using regex."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def is_valid_nigerian_phone(phone):
    """
    Validate Nigerian phone numbers.
    Accepts formats like:
    - 08012345678
    - +234 801 234 5678
    - 0817 123 4567
    - (234) 803 456 7890
    - 0706-123-4567
    """
    # Remove common separators
    cleaned = re.sub(r"[\s\-\(\)\+]", "", phone)

    # Should be 11 digits starting with 0 (local) or 13 digits starting with 234 (international)
    if re.fullmatch(r"0[789]\d{9}", cleaned):  # e.g. 08012345678
        return True
    if re.fullmatch(r"234[789]\d{9}", cleaned):  # e.g. 2348012345678
        return True

    return False


def contact_form():
    st.markdown("### 📬 Send Me a Message")
    st.write("Please fill out the form below to get in touch.")

    with st.form("contact_form"):
        name = st.text_input(
            "Your Full Name*", placeholder="Enter your full name"
        )
        email = st.text_input(
            "Email Address*", placeholder="you@example.com"
        )
        phone = st.text_input(
            "Phone Number*",
            placeholder="e.g., 0801 234 5678 or +234 812 345 6789"  # Nigerian format
        )
        message = st.text_area(
            "Your Message*", placeholder="Type your message here..."
        )
        submit_button = st.form_submit_button("📤 Send Message")

    if submit_button:
        # Validate all fields
        if not WEBHOOK_URL:
            st.error("📧 The contact form is not configured. Please try later.", icon="⚠️")
            st.stop()

        if not name.strip():
            st.error("🧑 Please enter your full name.", icon="❗")
            st.stop()

        if not email:
            st.error("📨 Please enter your email address.", icon="❗")
            st.stop()

        if not is_valid_email(email):
            st.error("📧 Please enter a valid email address.", icon="❗")
            st.stop()

        if not phone:
            st.error("📱 Please enter your phone number.", icon="❗")
            st.stop()

        if not is_valid_nigerian_phone(phone):
            st.error(
                "📞 Invalid Nigerian phone number. "
                "Use format: 0801 234 5678 or +234 812 345 6789", 
                icon="❗"
            )
            st.stop()

        if not message.strip():
            st.error("💬 Please write a message.", icon="❗")
            st.stop()

        # Prepare payload
        data = {
            "name": name.strip(),
            "email": email.lower().strip(),
            "phone": re.sub(r"[^\d+]", "", phone).replace("234", "0", 1) if phone.startswith("234") else phone,
            "message": message.strip(),
        }

        # Send to webhook
        try:
            response = requests.post(WEBHOOK_URL, json=data, timeout=10)
            if response.status_code == 200:
                st.success("✅ Your message has been sent successfully! I'll get back to you soon. 🎉", icon="🚀")
            else:
                st.error("❌ Something went wrong. Please try again later.", icon="😨")
        except Exception as e:
            st.error(f"⚠️ Network error: {e}. Could not send your message.", icon="🔌")
            st.stop()