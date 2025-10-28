import pickle

# Load the pipeline
with open('/workspaces/machine_learning_data_talks_club_homework/05-deployment/pipeline_v1.bin', 'rb') as f:
    pipeline = pickle.load(f)

# The record to score
lead = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Make prediction
probability = pipeline.predict_proba([lead])[0, 1]

print(f"Probability of conversion: {probability:.3f}")
