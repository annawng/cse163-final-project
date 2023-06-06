"""
Joey Kang, Eric Kim, and Anna Wang
CSE 163
Given the time and location a crime is committed, predicts the type of offense
it is (assault, larceny, fraud, etc.).
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def predict_offense_type(data: pd.DataFrame) -> None:
    """
    Trains and assesses a model for predicting the type of offense based on
    time (hour of the day) and location (MCPP/neighborhood) using `data`, the
    SPD crime dataset.
    """
    # Process data
    data = data[['Offense Start DateTime', 'Offense Parent Group',
                'MCPP']].dropna()
    data['DateTime'] = pd.to_datetime(
        data['Offense Start DateTime'])
    data['Hour'] = data['DateTime'].dt.hour
    data['Year'] = data['DateTime'].dt.year.astype(int)
    data = data[data['Year'] >= 2020]

    data = data[['Hour', 'Offense Parent Group',
                'MCPP']]
    features = data[['Hour', 'MCPP']]
    features = pd.get_dummies(features)
    labels = data['Offense Parent Group']
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.3, random_state=0)

    # Train the model
    knn = KNeighborsClassifier(n_neighbors=7).fit(features_train, labels_train)

    # Assess the model
    accuracy = knn.score(features_test, labels_test)
    print(f'Accuracy: {accuracy}')
