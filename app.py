import pandas as pd
import plotly.express as px
import streamlit as st
df_vehicles = pd.read_csv('vehicles_us.csv')
def extract_manufacturer(model_name):
    # Splitting by space and assuming the first word is the manufacturer
    return model_name.split()[0].lower()  # Assuming all manufacturer names are lowercase

# Apply the function to create the 'manufacturer' column
df_vehicles['manufacturer'] = df_vehicles['model'].apply(extract_manufacturer)
manu_adv = df_vehicles.groupby('manufacturer')['date_posted'].count().reset_index() 
manu_years_df = df_vehicles.groupby('manufacturer')['model_year'].mean().reset_index()
manu_price_df = df_vehicles.groupby('manufacturer')['price'].mean().reset_index() 
st.header("Car Advertising at a glance", divider="red")
st.header("Car price per Manufcturer", divider="red")
fig = px.histogram(manu_price_df,x='price',color='manufacturer',title='Average price by Manufacturer')
st.plotly_chart(fig)
st.header("Model Year per manufacturer", divider="red")
fig = px.scatter(manu_years_df,x='manufacturer',color='model_year',title='Average Model Year by manufacturer')
st.plotly_chart(fig)
st.header("Advertisements created per manufacturer", divider="red")
fig = px.histogram(manu_adv,x='date_posted',color='manufacturer',title='Ads posted by manufacturer')
st.plotly_chart(fig)
manu_model = df_vehicles.groupby(['manufacturer','model'])['date_posted'].count().reset_index()
st.header("Advertisements per manufacturer and model",divider="red")
option= st.selectbox("Choose a manufacturer",("acura","bmw",
"buick","cadillac","chevrolet","chrysler","dodge","ford","gmc","honda","hyundai","jeep","kia","nissan","ram","subaru","toyota")
)
st.write(option)
st.bar_chart(manu_model[manu_model['manufacturer']== option] ,x="model",y="date_posted")