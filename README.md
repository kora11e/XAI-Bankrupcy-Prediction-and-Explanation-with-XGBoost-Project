<h1>Bankruptcy Prediction Project for Explainable AI Classes</h1>

<h2>The project incorporates techniques of Explainable AI such as Shapley Additive Explanations, Local Interpretable Model-Agnostic Explanations and Partial Dependency Plots.</h2>

<h2>Instructions to run the code with Conda Environment</h2>
1. Download the project as zip in upper right corner of clone the project on your machine.
2. Open the project in your desired code editor. 
3. In the console move to folder
4. In Conda console create the environment with command:

```python
conda create --name <your-name>
```

5. Run following command to isntall packages from requirements.txt
6. 
```python
conda install --file requirements.txt
```

6. Run individual Jupyter Notebook blocks to display the code results.
  
<h2>Project Explanation</h2>

<h3>Features:</h3>

Text Classification:

The project loads a dataset of text reviews (presumably for sentiment analysis).

Uses a machine learning model to classify texts.

TF-IDF Vectorization:

Text data is vectorized using TfidfVectorizer, converting raw text into numerical features.

Model Training:

A Logistic Regression classifier is trained on the vectorized data.

The model learns to predict the sentiment of text inputs.

Explainability with LIME:

LIME (Local Interpretable Model-agnostic Explanations) is used to explain individual predictions.

Explains why a particular text was classified in a certain way by highlighting key words.
