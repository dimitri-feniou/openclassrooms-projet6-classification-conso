# Script for API 
import requests
import requests
import pandas as pd

# API key
app_id = '1a481052'
app_key = '6eb699942174846cc368ffde3035275e'

# Term to search
query = 'champagne'

# URL of API
url = 'https://api.edamam.com/api/food-database/v2/parser'

# parameter query 
params = {
    'app_id': app_id,
    'app_key': app_key,
    'ingr': query,

}

# Send request GET
response = requests.get(url, params=params)

# Verify statut of response
if response.status_code == 200:
    data = response.json()
    # Extract first 10 products
    hints = data.get('hints', [])[:10]
    # Prepare data 
    products = []
    for hint in hints:
        food = hint.get('food', {})
        products.append({
            'foodId': food.get('foodId', ''),
            'label': food.get('label', ''),
            'category': food.get('category', ''),
            'foodContentsLabel': food.get('foodContentsLabel', ''),
            'image': food.get('image', '')
        })
    # Create dataframe
    df = pd.DataFrame(products)
    # Save dataframe into csv file 
    df.to_csv('edamam_products.csv', index=False)
    print('Les données ont été enregistrées dans edamam_products.csv')
else:
    print(f'Erreur {response.status_code} : {response.text}')
