import pickle
import pandas as pd

# Load the saved model AND the saved columns
with open('rent_predictor.pkl', 'rb') as file:
    model = pickle.load(file)
with open('model_columns.pkl', 'rb') as file:
    model_columns = pickle.load(file)

print("Model and columns loaded successfully!")

# --- Create a Sample Data Point to Test ---
test_data = {
    'BHK': [2],
    'Size': [1000],
    'Floor': [1],
    'Bathroom': [2],
    'City_Mumbai': [1],
    'Furnishing Status_Semi-Furnished': [1],
    'Area Type_Super Area': [1],
    'Tenant Preferred_Family': [1],
    'Point of Contact_Contact Owner': [1]
}

# Convert the dictionary into a small DataFrame
input_df = pd.DataFrame(test_data)

# Re-order and add missing columns using the loaded list
# This guarantees the names AND order are exactly correct
final_input = input_df.reindex(columns=model_columns, fill_value=0)

# Make a prediction
predicted_rent = model.predict(final_input)

# Print the result
print(f"\nPredicted Rent: ₹{predicted_rent[0]:,.2f}")