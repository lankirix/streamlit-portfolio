import streamlit as st
import requests

def contact_form():
    st.header("📬 Get in Touch")

    # Tabs for Contact vs Work With Me
    tab1, tab2 = st.tabs(["✉️ Contact Me", "🤝 Work With Me"])

    # --- Contact Form ---
    with tab1:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            phone = st.text_input("Your Phone Number")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send")

        if submitted:
            send_to_webhook("contact", name, email, phone, {"message": message})

    # --- Work With Me Form ---
    with tab2:
        with st.form("work_form"):
            name = st.text_input("Your Name", key="work_name")
            email = st.text_input("Your Email", key="work_email")
            phone = st.text_input("Your Phone Number", key="work_phone")
            company = st.text_input("Company / Organization", key="work_company")
            problem = st.text_area("Describe your business problem", key="work_problem")
            goal = st.text_area("What outcome do you want to achieve?", key="work_goal")
            submitted = st.form_submit_button("Submit Proposal")

        if submitted:
            send_to_webhook(
                "work_with_me",
                name,
                email,
                phone,
                {
                    "company": company,
                    "problem": problem,
                    "goal": goal,
                },
            )

def send_to_webhook(form_type, name, email, phone, extra_fields):
    try:
        webhook_url = st.secrets["WEBHOOK_URL"]

        payload = {
            "form_type": form_type,
            "name": name,
            "email": email,
            "phone": phone,
            **extra_fields,
        }

        response = requests.post(webhook_url, json=payload)

        if response.status_code == 200:
            st.success("✅ Your submission has been sent successfully!")
        else:
            st.error(f"❌ Failed to send. Server responded with {response.status_code}")
            st.write(response.text)

    except KeyError:
        st.error("❌ Missing `WEBHOOK_URL` in Streamlit `secrets.toml`.")
    except Exception as e:
        st.error("⚠️ An unexpected error occurred.")
        st.write(e)
