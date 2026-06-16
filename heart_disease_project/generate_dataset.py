import numpy as np
import pandas as pd

rng = np.random.RandomState(42)
n = 303

age      = rng.normal(54.4, 9.0, n).clip(29, 77).astype(int)
sex      = rng.binomial(1, 0.68, n)
cp       = rng.choice([1,2,3,4], n, p=[0.08,0.17,0.28,0.47])
trestbps = rng.normal(131.7, 17.6, n).clip(94, 200).astype(int)
chol     = rng.normal(246.7, 51.8, n).clip(126, 564).astype(int)
fbs      = rng.binomial(1, 0.15, n)
restecg  = rng.choice([0,1,2], n, p=[0.48,0.02,0.50])
thalach  = rng.normal(149.6, 22.9, n).clip(71, 202).astype(int)
exang    = rng.binomial(1, 0.33, n)
oldpeak  = (rng.exponential(1.0, n) * rng.choice([0,1], n, p=[0.32,0.68])).round(1).clip(0, 6.2)
slope    = rng.choice([1,2,3], n, p=[0.21,0.68,0.11])
ca       = rng.choice([0,1,2,3], n, p=[0.58,0.22,0.13,0.07])
thal     = rng.choice([3,6,7], n, p=[0.55,0.06,0.39])

log_odds = (
    -3.5
    + 0.04 * (age - 54)
    + 0.5  * sex
    + 0.8  * (cp == 4).astype(int)
    - 0.03 * (thalach - 149)
    + 0.6  * exang
    + 0.5  * oldpeak
    + 0.4  * (thal == 7).astype(int)
    + 0.4  * ca
)
prob   = 1 / (1 + np.exp(-log_odds))
target = (rng.uniform(0, 1, n) < prob).astype(int)

df = pd.DataFrame({
    'age': age, 'sex': sex, 'chest_pain_type': cp,
    'resting_bp': trestbps, 'cholesterol': chol,
    'fasting_blood_sugar': fbs, 'rest_ecg': restecg,
    'max_heart_rate': thalach, 'exercise_angina': exang,
    'st_depression': oldpeak, 'st_slope': slope,
    'num_vessels': ca, 'thalassemia': thal, 'target': target
})

out = '/sessions/amazing-festive-volta/mnt/capstone/heart_disease_project/heart_disease.csv'
df.to_csv(out, index=False)
print(f"Saved {len(df)} rows")
print(f"Heart disease: {df['target'].sum()} cases ({df['target'].mean()*100:.1f}%)")
