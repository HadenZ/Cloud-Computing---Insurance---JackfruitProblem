from datetime import date
from app.schemas import QuoteCreate

def calculate_premium(quote: QuoteCreate) -> float:
    base_premium = 100.0

    # Add-ons for travel insurance
    if quote.insurance_type == "travel":
        duration = 0
        if quote.start_date and quote.end_date:
            duration = (quote.end_date - quote.start_date).days
        base_premium += duration * 5  # ₹5 per day
        if quote.destination and quote.destination.lower() in ["usa", "uk", "australia"]:
            base_premium += 50  # higher risk countries
        if quote.coverage_amount:
            base_premium += quote.coverage_amount * 0.001  # 0.1% of coverage

    # Add-ons for health insurance
    elif quote.insurance_type == "health":
        if quote.age:
            if quote.age < 30:
                base_premium += 50
            elif quote.age < 50:
                base_premium += 100
            else:
                base_premium += 200
        if quote.pre_existing_conditions:
            base_premium += 150
        if quote.coverage_amount:
            base_premium += quote.coverage_amount * 0.002  # 0.2%

    return round(base_premium, 2)
