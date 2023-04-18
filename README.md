# **BreastCancerDiagnosticTool_G1**
The repository contains code implementation of a Breast Cancer Diagnostic Tool that determines whether a given Patient's Mammogram Image is Benign or Malignant. VGG16 model, which is 16 layers deep was used.


# **Hosting on streamlit Community Cloud**
1.Clone the stream App codes on the repository onto your device. You can use Visual Studio Code or any ide of your choice that supports python language.
2.Push the stream App codes to a github repository; in our case - [repository](https://github.com/johnthuo1/breast-cancer-tool).
3. Set up an account on streamlit Community Cloud
4. Connected the github public repository to streamlit cloud
5. Deployed the app.

  **Live Project : [breast-cancer-tool.com](https://johnthuo1-breast-cancer-tool-streamapp-647vh4.streamlit.app/)**
  
  # **Limitations of the Project:**
1. The model was trained using more Benign cases than malignant. Hence on rare occasions, its predictions may be skewed towards benign. The reason why it is not 100% accurate.
2. The data was small. The more the data used, the more efficient the model will be in predicting accurately. Hence our small train data also affected the accuracy of our model.
  
  # **Next Steps (Points of Improvement):**
1.More data, will be needed to improve the model's performance.
2.Training the data with equal number of benign and malignant images will reduce bias.
3. A new model that caters for images unrelated to cancer will be needed to test the model's efficiency in identifying cancer-related images.
4. We can also employ multi-class classification instead of binary to cater for a broader scope. 
 
