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

5. Activate environment

```python
activate <your-name>
```

6. Run following command to isntall packages from requirements.txt

```python
conda install --file requirements.txt
```

7. Run individual Jupyter Notebook blocks to display the code results.
  
<h2>Project Explanation</h2>

<h3>Features:</h3>

Data processing:

The project loads a big dataset that is later processed into the more appropriate set of features.

It uses a machine learning model to classify the set of values for bankruptcy.

Data Modeling:

Columnar data is parsed into ensemble model and then optimized using Bayesian Search Space to determine the best features.

Data Explanation:

Data is explained using multiple etchniques to better understand how it changes over time, instance and with/without inclusion of one feature.

Model Training:

A XGBoost Regression is trained on the scaled data coming from bankruptcy dataset.

The model learns to predict the probability of comany going bankrupt.

<h2>Explainability with LIME and GIME:</h2>

<h3>LIME (Local Interpretable Model-agnostic Explanations) is used to explain individual predictions. </h3>

Explains why a particular text was classified in a certain way by highlighting key words.

<h3>SHAP (Shapley Additive Explanations) is used to explain impact of data on particular instance.</h3>

It calculates how the prediction would change if a specific feature were included or excluded, across all possible combinations of features.

Each feature gets a SHAP value:

Positive SHAP value → pushes the prediction higher.

Negative SHAP value → pushes the prediction lower.


<h2>Docker Container Access </h2>
If you have Docker, you can access the model via fast api with post method.

'''python
docker pull <your_username>/bankruptcy-prediction-api:v1
'''

'''python
docker run -d -p 80:80 <your_username>/bankruptcy-prediction-api:v1
'''

<h2>Dhango Frontend user access</h2>
