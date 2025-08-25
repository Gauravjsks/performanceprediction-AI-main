import os
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template

# --- App Setup ---
app = Flask(__name__)

# --- Load the Pre-trained Model ---
# This code now assumes the gwp.pkl file has been created by the notebook
try:
    model_path = os.path.join(os.path.dirname(__file__), 'gwp.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully.")
except FileNotFoundError:
    print("FATAL: Model file 'gwp.pkl' not found.")
    print("Please run the 'Employee_Prediction.ipynb' notebook first to train and save the model.")
    model = None

# This is the definitive list of features the model expects.
model_features = [
    'team', 'targeted_productivity', 'smv', 'wip', 'over_time', 'incentive',
    'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers',
    'quarter_Quarter2', 'quarter_Quarter3', 'quarter_Quarter4', 'quarter_Quarter5',
    'department_sweing', 'day_Saturday', 'day_Sunday', 'day_Thursday',
    'day_Tuesday', 'day_Wednesday'
]

# --- Flask Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model is not loaded. Please run the training notebook and restart the server.'}), 500

    try:
        form_data = request.form.to_dict()
        
        # Validation for negative values
        non_negative_fields = ['wip', 'over_time', 'incentive', 'idle_time', 'idle_men', 'no_of_style_change', 'no_of_workers']
        for field in non_negative_fields:
            if float(form_data.get(field, 0)) < 0:
                return jsonify({'error': f'Invalid input: "{field}" cannot be negative.'}), 400

        # Create DataFrame and make prediction
        input_df = pd.DataFrame(columns=model_features)
        input_df.loc[0] = 0

        for key, value in form_data.items():
            if key in input_df.columns:
                input_df.at[0, key] = float(value)

        for key in ['quarter', 'department', 'day']:
            value = form_data.get(key)
            if value and f"{key}_{value}" in input_df.columns:
                input_df.at[0, f"{key}_{value}"] = 1
        
        prediction = model.predict(input_df[model_features])
        score = round(prediction[0], 2)

        # Generate data-driven recommendations
        recommendations = []
        if score > 0.80:
            category = "High Potential"
            color = "blue"
            recommendations.append("This score indicates a top performer for this task configuration.")
            if float(form_data.get('smv', 0)) > 20:
                recommendations.append("Excelling at a high-complexity task (SMV > 20) is a great sign. Consider this employee for more challenging assignments.")
            recommendations.append("ACTION: Discuss career growth and consider for mentorship roles to aid retention.")
        elif score >= 0.60:
            category = "Good"
            color = "green"
            recommendations.append("This employee is predicted to be a consistent and reliable performer.")
            if float(form_data.get('no_of_style_change', 0)) > 0:
                recommendations.append("Maintaining solid productivity despite style changes shows adaptability.")
            recommendations.append("ACTION: Reinforce positive work habits and provide standard professional development opportunities.")
        else:
            category = "Needs Support"
            color = "orange"
            recommendations.append("This employee may benefit from additional guidance for this task.")
            if float(form_data.get('smv', 0)) > 25:
                recommendations.append("The high SMV suggests this is a complex task; ensure the employee has received adequate training.")
            if float(form_data.get('wip', 0)) > 1000:
                recommendations.append("A high Work-in-Progress (WIP) level might be creating pressure or bottlenecks.")
            recommendations.append("ACTION: Consider a coaching session to identify potential blockers and offer support.")

        result = {'score': f"{score:.2f}", 'category': category, 'color': color, 'recommendation': "\n".join(f"• {r}" for r in recommendations)}
        return jsonify(result)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'Failed to process the request. Check input values.'}), 500

# --- This block starts the server ---
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)