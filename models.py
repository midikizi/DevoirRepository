from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Models
class Vehicle(BaseModel):
    registration: str
    owner: str
    category: str
    insurance_quotation: float
    surcharge: float

class Bill(BaseModel):
    registration: str
    owner: str
    total_amount: float

# Data
vehicles = [
    Vehicle(registration="ABC123", owner="Congregation", category="Car", insurance_quotation=1000.0, surcharge=200.0),
    Vehicle(registration="DEF456", owner="Community1", category="Motorcycle", insurance_quotation=500.0, surcharge=100.0),
    Vehicle(registration="GHI789", owner="Sister1", category="Car", insurance_quotation=800.0, surcharge=160.0),
    Vehicle(registration="JKL012", owner="Sister2", category="Motorcycle", insurance_quotation=400.0, surcharge=80.0),
]

# Endpoints
@app.get("/category/{category}")
async def get_vehicles_by_category(category: str) -> List[Vehicle]:
    return [vehicle for vehicle in vehicles if vehicle.category == category]

@app.get("/owner/{owner}")
async def get_vehicles_by_owner(owner: str) -> List[Vehicle]:
    return [vehicle for vehicle in vehicles if vehicle.owner == owner]

@app.get("/bills/{owner}")
async def get_bills_for_owner(owner: str) -> List[Bill]:
    bills = []
    owner_vehicles = [vehicle for vehicle in vehicles if vehicle.owner == owner]
    for vehicle in owner_vehicles:
        total_amount = vehicle.insurance_quotation + vehicle.surcharge
        bills.append(Bill(registration=vehicle.registration, owner=owner, total_amount=total_amount))
    return bills
