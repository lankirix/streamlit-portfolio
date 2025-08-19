import streamlit as st

from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/lancaster picture.jpeg", width=230)

with col2:
    st.title("Lancaster Chris", anchor=False)
    st.write(
        "DevOps, AWS, MLOps, and Solutions Engineering expert, "
        "helping enterprises build scalable, automated, and "
        "data-driven infrastructure solutions."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 7+ Years experience in DevOps, cloud infrastructure, and automation
    - Strong expertise in AWS services (EC2, S3, Lambda, ECS, 
      CloudFormation)
    - Proven track record in MLOps pipeline development and 
      model deployment
    - Solutions Engineering expert with experience in enterprise 
      architecture
    - Excellent problem-solving skills and strong initiative in complex technical projects
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Cloud & DevOps: AWS (EC2, S3, Lambda, ECS, 
      CloudFormation), Docker, Kubernetes, CI/CD pipelines
    - Programming: Python, Bash, Terraform, YAML/JSON, SQL
    - MLOps: Model deployment, monitoring, MLflow, Kubeflow, 
      automated ML pipelines
    - Infrastructure: Infrastructure as Code, monitoring (CloudWatch, 
      Prometheus), logging
    """
)
