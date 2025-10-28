import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Load the pipeline (pipeline_v2.bin is in the base image at /code)
with open('pipeline_v2.bin', 'rb') as f:
    pipeline = pickle.load(f)

# Create FastAPI app
app = FastAPI()

# Define the request model
class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# Define the prediction endpoint
@app.post("/predict")
async def predict(lead: Lead):
    # Convert the lead to a dictionary
    lead_dict = lead.model_dump()
    
    # Make prediction
    probability = pipeline.predict_proba([lead_dict])[0, 1]
    
    # Return the result
    return {
        "conversion_probability": float(probability),
    }

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "ML Model API is running"}
