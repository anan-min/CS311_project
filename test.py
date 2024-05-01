from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df.head(5)

enc = LabelEncoder()


gender = enc.fit_transform(df['gender'])
smoking_status = enc.fit_transform(df['smoking_status'])
work_type = enc.fit_transform(df['work_type'])
Residence_type = enc.fit_transform(df['Residence_type'])
ever_married = enc.fit_transform(df['ever_married'])


df['work_type'] = work_type
df['ever_married'] = ever_married
df['Residence_type'] = Residence_type
df['smoking_status'] = smoking_status
df['gender'] = gender
df.drop('id', axis=1, inplace=True)
# drop the Attrition_Flag Column
X = df.drop(['stroke'], axis=1)
X.head()

Y = df['stroke']


# split data to train data and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=10)


# Import ML Libraries

classifiers = [[CatBoostClassifier(verbose=0), 'CatBoost Classifier'], [XGBClassifier(), 'XGB Classifier'], [RandomForestClassifier(), 'Random Forest Classifier'],
               [KNeighborsClassifier(), 'K-Nearest Neighbours'], [SGDClassifier(), 'SGD Classifier'], [
    SVC(), 'SVC'], [LGBMClassifier(), 'LGBM'], [GaussianNB(), "GaussianNB"],
    [DecisionTreeClassifier(), 'Decision Tree Classifier'], [LogisticRegression(), 'LogisticRegression']]


for cls in classifiers:
    model = cls[0]
    model.fit(X_train_std, y_train)

    y_pred = model.predict(X_test_std)
    accuracy = accuracy_score(y_test, y_pred) * 100
    print(cls[1])
    print('Confusion Matrix: ')
    print(confusion_matrix(y_test, y_pred))
    print("Accuracy : ", accuracy)
    print("Recall : ", recall_score(y_test, y_pred) * 100)
    print("Precision : ", precision_score(y_test, y_pred) * 100)
