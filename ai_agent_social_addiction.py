# -----------------------------------------
# 📦 Libraries
# -----------------------------------------
import pandas as pd

# -----------------------------------------
# 🔁 Input Functions
# -----------------------------------------

def get_valid_float(prompt, min_val=0, max_val=12):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"⛔ Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("⛔ Invalid input. Only numbers are allowed.")

def get_valid_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "no"]:
            return 1 if answer == "yes" else 0
        else:
            print("⛔ Please answer with 'yes' or 'no'.")

def get_user_input():
    print("💬 Please answer the following questions honestly:")
    print("👉 Note: Use numbers between 0 and 12 (e.g., 2.5, 7.0).")

    usage = get_valid_float("1️⃣ How many hours do you use social media daily? (0–12): ")
    sleep = get_valid_float("2️⃣ How many hours do you sleep every night? (0–12): ")
    academic = get_valid_yes_no("3️⃣ Does social media affect your academic performance? (yes/no): ")
    conflicts = get_valid_yes_no("4️⃣ Do you have conflicts with others because of social media? (yes/no): ")

    return {
        "Avg_Daily_Usage_Hours": usage,
        "Sleep_Hours_Per_Night": sleep,
        "Affects_Academic_Performance": academic,
        "Conflicts_Over_Social_Media": conflicts
    }

# -----------------------------------------
# 🤖 Agent Logic
# -----------------------------------------

def predict_addiction_level(model, input_data: dict):
    label_map = {0: "Low", 1: "Medium", 2: "High"}
    input_df = pd.DataFrame([input_data])

    prediction_encoded = model.predict(input_df)[0]
    prediction = label_map.get(prediction_encoded, "Unknown")

    # 📍 Explanation
    explanation = []
    if input_data["Avg_Daily_Usage_Hours"] > 4:
        explanation.append("Your daily social media usage is high.")
    if input_data["Sleep_Hours_Per_Night"] < 6:
        explanation.append("Your sleep duration is lower than the recommended amount.")
    if input_data["Affects_Academic_Performance"] == 1:
        explanation.append("Your academic performance is affected by social media.")
    if input_data["Conflicts_Over_Social_Media"] == 1:
        explanation.append("You experience conflicts due to social media use.")

    if not explanation:
        explanation.append("No significant risk factors were detected.")

    # 💡 Advice
    advice = []
    if input_data["Avg_Daily_Usage_Hours"] > 4:
        advice.append("Try to reduce your daily social media usage.")
    if input_data["Sleep_Hours_Per_Night"] < 6:
        advice.append("Prioritize sleep — aim for at least 7–8 hours.")
    if input_data["Affects_Academic_Performance"] == 1:
        advice.append("Manage your time better to maintain academic performance.")
    if input_data["Conflicts_Over_Social_Media"] == 1:
        advice.append("Talk to friends or family about setting healthy boundaries.")

    if not advice:
        advice.append("Your social media usage appears balanced. Keep it up!")

    # 🔄 What-if: simulate better sleep
    what_if_data = input_data.copy()
    what_if_data["Sleep_Hours_Per_Night"] = 8
    what_if_pred = model.predict(pd.DataFrame([what_if_data]))[0]
    what_if_label = label_map[what_if_pred]

    if what_if_label != prediction:
        what_if_message = f"❓ If you slept 8 hours, the prediction would change to: **{what_if_label}**"
    else:
        what_if_message = "❓ Even with 8 hours of sleep, the prediction would remain the same."

    # 📝 Report
    report = f"""
📌 **User Report**
Predicted Addiction Level: **{prediction}**

📍 Explanation:
- {'; '.join(explanation)}

💡 Suggestions:
- {'; '.join(advice)}

🔄 What-if Analysis:
- {what_if_message}
"""
    return report.strip()

# -----------------------------------------
# ▶️ Run Agent (Assuming model already trained)
# -----------------------------------------

user_data = get_user_input()
result = predict_addiction_level(model, user_data)

print("\n===========================")
print("📄 Final Report:")
print("===========================\n")
print(result)
