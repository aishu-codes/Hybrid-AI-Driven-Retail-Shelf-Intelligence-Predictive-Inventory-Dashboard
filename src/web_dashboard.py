import streamlit as st
import pandas as pd

# Sample data for expected and detected quantities
expected_data = {'Item': ['Item A', 'Item B', 'Item C', 'Item D'],
                 'Expected Quantity': [100, 150, 200, 250]}

detected_data = {'Item': ['Item A', 'Item B', 'Item C', 'Item D'],
                  'Detected Quantity': [90, 160, 180, 240]}

expected_df = pd.DataFrame(expected_data)
detected_df = pd.DataFrame(detected_data)

# Merge the two dataframes on 'Item'
comparison_df = pd.merge(expected_df, detected_df, on='Item')

# Streamlit dashboard setup
st.title('Inventory Visualization Dashboard')
st.write('### Expected vs Detected Quantities')

# Display the comparison table
st.write(comparison_df)

# Create a bar chart for visualization
st.bar_chart(comparison_df.set_index('Item'))

# Optionally, highlight items with differences
st.write('### Items with Differences')
differences = comparison_df[comparison_df['Expected Quantity'] != comparison_df['Detected Quantity']]
if not differences.empty:
    st.write(differences)
else:
    st.write('All quantities match!')