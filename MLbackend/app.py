# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import model  # This assumes model.py is in the same directory

app = FastAPI()

class BudgetRequest(BaseModel):
    income: float

class BudgetResponse(BaseModel):
    primary: float
    secondary: float
    tertiary: float

@app.post("/predict/", response_model=BudgetResponse)
async def predict_budget(request: BudgetRequest):
    try:
        # Predict budget based on income
        categories = ["food", "transportation", "subscription"]  # Replace with actual categories
        prediction = model.predict_budget(categories, request.income)
        
        # Calculate budget allocation based on prediction
        total = request.income
        primary_budget = total * (0.5 if 'Primary' in prediction else 0)
        secondary_budget = total * (0.3 if 'Secondary' in prediction else 0)
        tertiary_budget = total * (0.2 if 'Tertiary' in prediction else 0)

        # Calculate spending percentages
        total_spending = primary_budget + secondary_budget + tertiary_budget
        #primary_percentage = primary_budget
        #secondary_percentage = secondary_budget
        #tertiary_percentage = tertiary_budget
        primary_percentage = (primary_budget / total_spending) * 100 if total_spending > 0 else 0
        secondary_percentage = (secondary_budget / total_spending) * 100 if total_spending > 0 else 0
        tertiary_percentage = (tertiary_budget / total_spending) * 100 if total_spending > 0 else 0

        return BudgetResponse(
            primary=primary_percentage,
            secondary=secondary_percentage,
            tertiary=tertiary_percentage
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
