from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

def train_models(df, target):
    # Only use rolling features
    features = [col for col in df.columns if "_rolling" in col]

    X = df[features]
    y = (df[target] > df[target].median()).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    log_model = LogisticRegression(max_iter=1000)
    log_model.fit(X_train, y_train)

    xgb_model = XGBClassifier(
        n_estimators=200,
        max_depth=4,
        learning_rate=0.05
    )
    xgb_model.fit(X_train, y_train)

    return log_model, xgb_model