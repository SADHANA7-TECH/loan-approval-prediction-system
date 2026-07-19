import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="Bank Financial Health Dashboard",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Financial Health Dashboard")
st.write("### AI Powered Loan Approval Prediction")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Customer Details")

    dependents = st.number_input("Number of Dependents", 0, 10, 1)

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    income = st.number_input(
        "Annual Income",
        min_value=0,
        value=9000000
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=2000000
    )

    loan_term = st.number_input(
        "Loan Term",
        min_value=1,
        value=12
    )

    cibil = st.slider(
        "CIBIL Score",
        300,
        900,
        750
    )

    residential = st.number_input(
        "Residential Asset Value",
        value=6000000
    )

    commercial = st.number_input(
        "Commercial Asset Value",
        value=3000000
    )

    luxury = st.number_input(
        "Luxury Asset Value",
        value=2000000
    )

    bank = st.number_input(
        "Bank Asset Value",
        value=5000000
    )

with col2:

    st.subheader("📊 Prediction")

    if st.button("🔍 Analyze"):

        education_value = 0 if education == "Graduate" else 1
        self_value = 0 if self_employed == "No" else 1

        input_data = pd.DataFrame([[
            dependents,
            education_value,
            self_value,
            income,
            loan_amount,
            loan_term,
            cibil,
            residential,
            commercial,
            luxury,
            bank
        ]], columns=[
            "no_of_dependents",
            "education",
            "self_employed",
            "income_annum",
            "loan_amount",
            "loan_term",
            "cibil_score",
            "residential_assets_value",
            "commercial_assets_value",
            "luxury_assets_value",
            "bank_asset_value"
        ])

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0]

        approval = probability[0] * 100

        st.metric("Financial Health Score", f"{approval:.1f}/100")
        st.metric("Approval Probability", f"{approval:.2f}%")

        if prediction[0] == 0:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")