import tensorflow as tf
import streamlit as st
import numpy as np
import cv2

@st.cache_data
def load_model():
    try:
        with tf.device('/cpu:0'): 
            model = tf.keras.models.load_model("C:/Users/Hp/Desktop/BreastCancerDiagnosisStreamlit/model/vgg16mammaryglandsClassifier.h5", compile=False)
            return model 
    except FileNotFoundError:
        st.error("Model File not found")
        return None
    
    except RuntimeError:
        st.error("tensorflow not found in your device")
        
        
        return None
    
def model_pred(img):
    try:
        # Image preprocessing
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (224,224))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        with tf.device('/cpu:0'):
            pred = model.predict(img)
        
        return pred[0][0]
        
    except cv2.error:
        st.error("Invalid Image File")
        return None
    
    except RuntimeError:
        st.error("tensorflow not found in your device and cv2 ")
        return None
    

def main():
    st.title("Breast Cancer Diagnostic Tool(Benign / Malignant)")
    result = ""
    img_file = st.file_uploader("Please Upload your Mammogram Image", type=["png"])
    if img_file is not None:
        img = cv2.imdecode(np.fromstring(img_file.read(), np.uint8), 1)
        st.image(img, caption="Uploaded image", use_column_width=True)
        
        # Press this button to see results
        if st.button("See Results"):
            pred = model_pred(img)
            if pred is not None:
                if pred > 0.5 :
                    result = "Malignant!Consult your Oncologist for more Details."
                else:
                    result = "Benign! Consult your Oncologist for more Details."
                
    st.success(result)
    
if __name__ == '__main__':
    model = load_model()
    if model is not None:
        main()
        
                    
                
    
    
            
    