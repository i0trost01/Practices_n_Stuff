import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import VarianceThreshold
import statsmodels.formula.api as sm
import plotly as py
import plotly.graph_objs as go

df = pd.read_csv("Countries.csv")
X = df.iloc[:, 2:-1].values
y = df.iloc[:, -1:].values


def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x


SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4]]

X_Modeled = backwardElimination(X_opt, SL)

X_train, X_test, y_train, y_test = train_test_split(X_Modeled, y, test_size=0.25, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred2 = model.predict(X_train)

print(model.score(X_test, y_test))

x_scat = X_train[:, 0]
y_scat = X_train[:, 1]
z_scat = y_train[:, 0]

trace1 = go.Scatter3d(
    x=x_scat,
    y=y_scat,
    z=z_scat,
    mode='markers',
    name='Country Data',
    marker=dict(
        size=10,
        line=dict(
            color='black',
            width=0.5
        ),
        opacity=0.8
    )

)


x_line = X_train[:, 0]
y_line = X_train[:, 1]
z_line = y_pred2[:, 0]

trace2 = go.Scatter3d(
    x=x_line,
    y=y_line,
    z=z_line,
    mode='lines',
    name='Model',
    marker=dict(
        size=20,
        line=dict(
            color='black',
            width=1
        ),
        opacity=0.8
    )

)

layout = go.Layout(
    title='Infant Mortality Model',
    scene=dict(
    xaxis=dict(
        title='Literacy'
    ),
    yaxis=dict(
        title='Agriculture'
    ),
    zaxis=dict(
        title='Mortality'
    )
    ),
    margin=dict(
        l=100,
        r=50,
        b=50,
        t=100
    )

)
data = [trace1,trace2]
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='file.html')
