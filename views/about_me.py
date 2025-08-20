import streamlit as st
import os
from PIL import Image

# --- Resolve paths correctly ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # go up from /views
logo_path = os.path.join(BASE_DIR, "public", "lankirix_logo.jpeg")
profile_path = os.path.join(BASE_DIR, "public", "lancaster_picture.jpeg")

# --- MUST BE AT THE TOP ---
st.set_page_config(
    page_title="Lankirix | DevOps & MLOps Expert",
    page_icon="🛠️",  # use emoji instead of jpeg favicon
    layout="wide",
)

# --- LOGO ---
st.logo(Image.open(logo_path))

# --- CONTACT FORM DIALOG ---
@st.dialog("Contact Me")
def show_contact_form():
    from forms.contact import contact_form
    contact_form()

# --- HERO SECTION ---
st.markdown("<h1 style='margin-bottom: 0;'>About Me</h1>", unsafe_allow_html=True)
st.write("DevOps, AWS, MLOps & Solutions Engineering")

col1, col2 = st.columns([1, 2], gap="large", vertical_alignment="center")
with col1:
    st.image(profile_path, width=230)

with col2:
    st.write(
        """
        ### Lancaster Chris
        **DevOps, AWS, MLOps, and Solutions Engineering Expert**

        Helping enterprises build scalable, automated, and data-driven infrastructure solutions.
        """
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.markdown("### Experience & Qualifications")
st.write(
    """
    - **10+ Years** experience in DevOps, cloud infrastructure, and automation
    - Strong expertise in **AWS** (EC2, S3, Lambda, ECS, CloudFormation, IAM, VPC)
    - Proven track record in **MLOps** pipeline development and model deployment
    - **Solutions Engineering** expert with enterprise architecture experience
    - Excellent problem-solving skills and leadership in complex technical projects
    """
)

# --- SKILLS ---
st.markdown("### Hard Skills")
st.write(
    """
    - **Cloud & DevOps**: AWS, Docker, Kubernetes, Terraform, CI/CD (GitHub Actions, Jenkins)
    - **Programming**: Python, Bash, YAML/JSON, SQL, Infrastructure as Code
    - **MLOps**: Model deployment, monitoring, MLflow, Kubeflow, automated ML pipelines
    - **Infrastructure**: IaC, observability (CloudWatch, Prometheus, Grafana), logging
    """
)
