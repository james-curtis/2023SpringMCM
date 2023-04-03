from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.ensemble import *
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.svm import *
from sklearn.neighbors import *
from sklearn.neural_network import *
from sklearn.metrics import *
import matplotlib.pyplot as plt
import pickle

X, Y = getxy()

feature_names = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)  # , random_state=42

alpha_ = 12.8
models = [
    LinearRegression(),
    Ridge(alpha=alpha_),
    Lasso(),
    ElasticNet(),
    DecisionTreeRegressor(),
    RandomForestRegressor(),
    AdaBoostRegressor(),
    GradientBoostingRegressor(),
    XGBRegressor(),
    LGBMRegressor(),
    CatBoostRegressor(),
    SVR(),
    KNeighborsRegressor(),
    MLPRegressor()
]

# Train and test each model and output R-squared values
for model in models:
    modelName = type(model).__name__
    title = f'[{modelName}]{modelName}'
    print(f'-----------{title}-----------')
    # if type(models).__name__ == 'LGBMRegressor':
    #     model.fit(X_train, y_train, feature_name=feature_names)
    # else:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    # r2 = r2_score(y_test, y_pred)

    # Predict and visualize results
    plt.scatter(y_test, y_pred)
    plt.title(type(model).__name__)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.axis('equal')
    plt.axis('square')
    # plt.xlim([9e4, 1e5])
    # plt.ylim([9e4, 1e5])
    _ = plt.plot([-1e10, 1e10], [-1e10, 1e10])
    plt.tight_layout()
    plt.savefig(f'{modelName}.svg')
    plt.show()

    # Calculate mean square error
    print(title, f'r2_score: {r2_score(y_test, y_pred)}')
    print(title, f'mse: {mean_squared_error(y_test, y_pred)}')
    print(title, f'mae: {mean_absolute_error(y_test, y_pred)}')
    print(title, f'mape: {mean_absolute_percentage_error(y_test, y_pred)}')

    # Save Model
    with open(f'{modelName}.pkl', 'wb') as f:
        pickle.dump(model, f)

    if type(model).__name__ == 'CatBoostRegressor':
        print('Hyperparameter', model.get_all_params())

    if type(model).__name__ == 'Ridge':
        for feature, coef in zip(feature_names, model.coef_):
            print(f"{feature}: {coef:.5f}")
        print('coefficient', model.coef_ / alpha_)
