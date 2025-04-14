import streamlit as st

def predict_next_value(prices):
    if len(prices) < 2:
        return None
    diffs = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    recent_diffs = diffs[-5:]
    directions = ['up' if d > 0 else 'down' for d in recent_diffs]
    last_dir = directions[-1]
    next_dir = 'up' if last_dir == 'down' else 'down'
    recent_magnitudes = [abs(d) for d in recent_diffs]
    avg_magnitude = sum(recent_magnitudes[-3:]) / len(recent_magnitudes[-3:])
    predicted_change = int(avg_magnitude * 0.8)
    last_value = prices[-1]
    if next_dir == 'up':
        next_value = last_value + predicted_change
    else:
        next_value = max(0, last_value - predicted_change)
    return next_value

st.title("R6 Market Snipe Predictor")

user_input = st.text_input("Enter price history (comma-separated):", "35,66,12,166,10,120,16,98,66,33")
if user_input:
    try:
        price_list = [int(x.strip()) for x in user_input.split(',')]
        prediction = predict_next_value(price_list)
        st.success(f"Predicted next value: {prediction}")
    except:
        st.error("Make sure to enter only numbers separated by commas.")
