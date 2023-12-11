import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor

print()

df = pd.read_csv(os.getcwd() + '/data_set/credit_score_ds.csv')

df[['month', 'age', 'occupation', 'annual_income', 'monthly_inhand_salary', 'num_bank_accounts', 'num_credit_card', 'num_of_loan', 'num_credit_inquiries', 'credit_history_age', 'amount_invested_monthly', 'payment_behaviour', 'monthly_balance', 'credit_score']] = df['month|age|occupation|annual_income|monthly_inhand_salary|num_bank_accounts|num_credit_card|num_of_loan|num_credit_inquiries|credit_history_age|amount_invested_monthly|payment_behaviour|monthly_balance|credit_score'].str.split('|', expand=True)

# Замена исходного столбца

df = df.drop('month|age|occupation|annual_income|monthly_inhand_salary|num_bank_accounts|num_credit_card|num_of_loan|num_credit_inquiries|credit_history_age|amount_invested_monthly|payment_behaviour|monthly_balance|credit_score', axis=1)

# print(df.columns)
train_columns = ['age', 'annual_income', 'monthly_inhand_salary',
       'num_bank_accounts', 'num_credit_card', 'num_of_loan',
       'num_credit_inquiries', 'credit_history_age', 'amount_invested_monthly',
       'monthly_balance',]


# Колонка ответом, который должна дать нейросеть
y = df['credit_score']

# Колонки, на которых нейросеть будет опиратьсяЮ какой дать ответ.
X = df[train_columns]

credit_model = DecisionTreeRegressor()

credit_model.fit(X, y)
predictions = credit_model.predict(X)
print(predictions)


# check_data_set = {

#     'age' : False,
#     'annual_income' : False,
#     'monthly_inhand_salary' : False ,
#     'num_bank_accounts' : False,
#     'num_credit_card' : False,
#     'num_of_loan' : False,
#     'num_credit_inquiries' : False,
#     'credit_history_age' : False,
#     'amount_invested_monthly' : False,
#     'monthly_balance' : False

# }