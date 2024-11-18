# **NORM 🍍🍕🍰**  
**Fruits and Vegetable Classification with Calorie Tracking**

This is a fruit and vegetable detection model that uses a real-time camera to effectively calculate calories based on the user's health. It helps users keep track of their food intake and provides a daily calorie chart with tips for improvement.  

---

## **Features**  
- **Real-time Food Detection**: Identify fruits and vegetables using a trained classification model.  
- **Calorie Calculation**: Estimate calories based on detected food items.  
- **Daily Summary**: Track calorie consumption and provide visual charts for the day.  
- **Health Tips**: Receive tips to improve your dietary habits.  

---

## **Main File**  
- **`Fruits_Vegetable_Classification.py`**:  
  The core file that implements the food detection and calorie tracking logic.

---

## **Other Files**  
- **`App.py`**: Runs the main application interface.  
- **`FV.h5`**: Pretrained model file for fruits and vegetable classification.  
- **`ec2_api.py`**: API integration script for deployment on AWS EC2.  
- **`requirements.txt`**: Lists all dependencies needed to run the project.  

---

## **Technologies Used**  
- **Python**: Core programming language.  
- **TensorFlow/Keras**: For training and running the classification model.  
- **Streamlit**: For the user interface (if applicable).  
- **Matplotlib**: For generating calorie charts.  

---

## **Setup Instructions**  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/your-username/norm-fruit-detection.git
   cd norm-fruit-detection
   ```

2. **Install Dependencies**:  
   Ensure Python is installed and then run:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:  
   Start the main application:  
   ```bash
   python Fruits_Vegetable_Classification.py
   ```

4. **Optional**: To deploy using AWS EC2, configure and run `ec2_api.py`.  

---

## **How It Works**  
1. The application captures real-time images using the camera.  
2. Identifies the fruits or vegetables present using the trained model (`FV.h5`).  
3. Estimates the calorie count for the identified food items.  
4. Generates a daily calorie chart with insights and health tips.  

---

## **Future Enhancements**  
- Add support for more food categories.  
- Improve calorie estimation accuracy with additional data.  
- Integrate mobile application support.  

---

## **License**  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**
This project is based on the work of "https://github.com/Spidy20/Fruit_Vegetable_Recognition"
We have cloned and modified it to include additional features and improvements specific to our use case.

--- 

## **Contributing**  
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

--- 
