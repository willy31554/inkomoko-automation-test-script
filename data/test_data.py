# Test data
valid_transaction_data = [
    {"amount": 100},
    {"amount": 500},
    {"amount": 1000}
]

invalid_transaction_data = [
    {"amount": -100},  # Negative amount
    {"amount": "abc"},  # Non-numeric amount
    {"amount": 10000}  # High amount exceeding available balance
]
