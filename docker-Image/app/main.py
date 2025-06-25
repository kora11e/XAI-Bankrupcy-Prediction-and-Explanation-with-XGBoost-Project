from fastapi import FastAPI
from pydantic import BaseModel
import pickle, os, xgboost

#the model can be used as an endpoint via post method
#in order to utilize it, run curl method from file curl_command and change the values of parameters for own need
class InputData(BaseModel):
    Operating_Profit_Rate: float
    Operating_Expense_Rate: float
    Interest_bearing_debt_interest_rate: float
    Revenue_Per_Share: float
    Realized_Sales_Gross_Profit_Growth_Rate: float
    Operating_Profit_Growth_Rate: float
    Continuous_Net_Profit_Growth_Rate: float
    Current_Ratio: float
    Interest_Expense_Ratio: float
    Total_debt_Total_net_worth: float
    Long_term_fund_suitability_ratio: float
    Accounts_Receivable_Turnover: float
    Average_Collection_Days: float
    Inventory_Turnover_Rate: float
    Net_Worth_Turnover_Rate: float
    Quick_Assets_Current_Liability: float
    Inventory_Working_Capital: float
    Inventory_Current_Liability: float
    Current_Liabilities_Liability: float
    Long_term_Liability_to_Current_Assets: float
    Current_Asset_Turnover_Rate: float
    Cash_Turnover_Rate: float
    No_credit_Interval: float
    Degree_of_Financial_Leverage: float
    Interest_Coverage_Ratio: float
    Net_Income_Flag: float

app = FastAPI(title='Bankruptcy Prediction')

with open('pickle_bankruptcy_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

@app.post('/predict_bankruptcy')
async def predict(data: InputData):
    input_features = [[data.Operating_Profit_Rate, 
                       data.Operating_Expense_Rate,
                       data.Interest_bearing_debt_interest_rate,
                       data.Revenue_Per_Share,
                       data.Realized_Sales_Gross_Profit_Growth_Rate,
                       data.Operating_Profit_Growth_Rate,
                       data.Continuous_Net_Profit_Growth_Rate,
                       data.Current_Ratio,
                       data.Interest_Expense_Ratio,
                       data.Total_debt_Total_net_worth,
                       data.Long_term_fund_suitability_ratio,
                       data.Accounts_Receivable_Turnover,
                       data.Average_Collection_Days,
                       data.Inventory_Turnover_Rate,
                       data.Net_Worth_Turnover_Rate,
                       data.Quick_Assets_Current_Liability,
                       data.Inventory_Working_Capital,
                       data.Inventory_Current_Liability,
                       data.Current_Liabilities_Liability,
                       data.Long_term_Liability_to_Current_Assets,
                       data.Current_Asset_Turnover_Rate,
                       data.Cash_Turnover_Rate,
                       data.No_credit_Interval,
                       data.Degree_of_Financial_Leverage,
                       data.Interest_Coverage_Ratio,
                       data.Net_Income_Flag]]

    prediction = model.predict(input_features)
    return {'predicted outcome': prediction[0]}

