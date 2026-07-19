def calculate_health_score(probability):
    return int(probability)


def risk_level(score):
    if score >= 80:
        return "🟢 Low Risk"

    elif score >= 60:
        return "🟡 Medium Risk"

    else:
        return "🔴 High Risk"


def recommendations(cibil, income, loan_amount, assets):

    advice = []

    if cibil >= 750:
        advice.append("✅ Excellent CIBIL Score")

    elif cibil >= 650:
        advice.append("⚠ Average CIBIL Score")

    else:
        advice.append("❌ Improve your CIBIL Score")

    if income > loan_amount * 2:
        advice.append("✅ Income comfortably supports the requested loan.")

    else:
        advice.append("⚠ Loan amount is high compared with annual income.")

    if assets > loan_amount:
        advice.append("✅ Strong asset portfolio.")

    else:
        advice.append("⚠ Increase asset backing if possible.")

    return advice