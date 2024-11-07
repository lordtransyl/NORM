import streamlit as st
from PIL import Image
import numpy as np
from datetime import datetime
from keras.preprocessing.image import img_to_array
from keras.models import load_model

model = load_model('FV.h5')

labels = {
    0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot',
    7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger',
    14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
    19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple',
    26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn',
    32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'
}

fruits = ['Apple', 'Banana', 'Bell Pepper', 'Chilli Pepper', 'Grapes', 'Jalepeno', 'Kiwi', 'Lemon', 'Mango', 'Orange',
          'Paprika', 'Pear', 'Pineapple', 'Pomegranate', 'Watermelon']
vegetables = ['Beetroot', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Corn', 'Cucumber', 'Eggplant', 'Ginger',
              'Lettuce', 'Onion', 'Peas', 'Potato', 'Raddish', 'Soy Beans', 'Spinach', 'Sweetcorn', 'Sweetpotato',
              'Tomato', 'Turnip']

calories_dict = {
    "apple": 52, "banana": 89, "beetroot": 43, "bell pepper": 20, "cabbage": 25, "capsicum": 20, "carrot": 41,
    "cauliflower": 25, "chilli pepper": 40, "corn": 96, "cucumber": 16, "eggplant": 25, "garlic": 149, "ginger": 80,
    "grapes": 69, "jalepeno": 40, "kiwi": 61, "lemon": 29, "lettuce": 15, "mango": 60, "onion": 40, "orange": 47,
    "paprika": 80, "pear": 57, "peas": 81, "pineapple": 50, "pomegranate": 83, "potato": 77, "raddish": 16,
    "soy beans": 446, "spinach": 23, "sweetcorn": 96, "sweetpotato": 86, "tomato": 18, "turnip": 28, "watermelon": 30
}
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_bmi(weight, height):
    height_m = height / 100  
    return weight / (height_m ** 2)


def has_high_sugar(food):
    high_sugar_foods = ['banana', 'grapes', 'mango', 'pineapple', 'watermelon']
    return food.lower() in high_sugar_foods

def categorize_food(predicted_food):
    if predicted_food.lower() in [food.lower() for food in fruits]:
        return "Fruit"
    elif predicted_food.lower() in [veg.lower() for veg in vegetables]:
        return "Vegetable"
    else:
        return "Unknown"


def suggest_food_based_on_time(bmr):
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        suggestion = "It’s morning! A high-protein food like eggs or beans will be ideal."
    elif 12 <= current_hour < 18:
        suggestion = "It’s afternoon! A balanced meal like rice and vegetables would be great."
    else:
        suggestion = "It’s evening! Try a lighter meal like salad or soup."
    return suggestion

def fetch_calories(predicted_food):
    """Fetch calories for the predicted food"""
    try:
        calories = calories_dict.get(predicted_food.lower(), "Unknown")
        return calories
    except Exception as e:
        st.error("Error in fetching the calories")
        print(e)
        return None

def predict_food(img):
    """Process the image and predict the food class"""
    img = Image.open(img)  

    
    img = img.resize((224, 224))  
    img = img_to_array(img)  
    img = img / 255.0  

    img = np.expand_dims(img, axis=0)


    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=-1)[0]  
    predicted_food = labels[predicted_class]  
    return predicted_food

def get_food_dimensions(img):
    """Calculate food dimensions (width, height, area) from the image"""
    img = Image.open(img)
    width, height = img.size 
    area = width * height  
    return width, height, area

st.markdown("""
    <style>
        /* Title Customization */
        .title {
            font-size: 50px;
            font-weight: normal;
            text-align: center;
            color: white;
            background: linear-gradient(135deg, #FF4E50, #F9D423); /* Creative Gradient */
            -webkit-background-clip: text;
            color: transparent;
            font-family: 'Verdana', sans-serif;
        }
        .highlight {
            font-size: 70px;
            font-weight: bold;
            background: linear-gradient(135deg, #FF4E50, #F9D423);
            -webkit-background-clip: text;
            color: transparent;
        }
        /* Background and page design */
        body {
            background-color: #f4f4f9;
            background-image: url('https://www.w3schools.com/w3images/nature.jpg'); /* Background image */
            background-size: cover;
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 12px 24px;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stTextInput input {
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
    </style>
    """, unsafe_allow_html=True)


def run():

    st.markdown('<div class="title"><span class="highlight">N</span>utritional <span class="highlight">O</span>ptimization and <span class="highlight">R</span>ecommendation <span class="highlight">M</span>odel</div>', unsafe_allow_html=True)

    age = st.number_input("Enter your age:", min_value=1, max_value=150)
    height = st.number_input("Enter your height in cm:", min_value=30, max_value=300)
    weight = st.number_input("Enter your weight in kg:", min_value=10, max_value=500)
    gender = st.selectbox("Select your gender:", ("Male", "Female"))

    bmr = calculate_bmr(weight, height, age, gender)
    bmi = calculate_bmi(weight, height)

    st.write(f"Your BMR (Basal Metabolic Rate) is: {bmr} kcal/day")
    st.write(f"Your BMI (Body Mass Index) is: {bmi}")

    img = st.camera_input("Take a picture of your food")

    if img is not None:
        st.image(img, caption="Captured Food", use_column_width=True)
        predicted_food = predict_food(img)
        st.write(f"Predicted Food: {predicted_food.capitalize()}")
        food_calories = fetch_calories(predicted_food)
        if food_calories != "Unknown":
            st.write(f"Estimated Calories: {food_calories} kcal per 100g of {predicted_food.capitalize()}")
        food_category = categorize_food(predicted_food)
        st.write(f"Food Category: {food_category}")

        food_suggestion = suggest_food_based_on_time(bmr)
        st.write(food_suggestion)

        if has_high_sugar(predicted_food) and age > 60:
            st.warning(f"Warning: The food {predicted_food.capitalize()} is high in sugar! Be cautious if you're elderly.")

        width, height, area = get_food_dimensions(img)
        st.write(f"Food Dimensions: Width = {width}, Height = {height}, Area = {area} pixels")

if __name__ == "__main__":
    run()
