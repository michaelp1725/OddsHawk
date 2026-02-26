def backtest(df, model):
    features = [col for col in df.columns if "rolling" in col]
    probs = model.predict_proba(df[features])[:, 1]
    df["model_prob"] = probs
    return df