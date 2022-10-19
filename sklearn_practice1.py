from sklearn import datasets
from IPython.display import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


iris = datasets.load_iris()
iris

# iris 샘플 출력 (feature data)
for i in range(0, len(iris.data)):
    print(i + 1, iris.data[i], iris.target[1])  # target : label

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df

df['target'] = iris.target
df

# 표준화
X = df.iloc[:, 0]
X

# 표준화
X_ = (X - X.mean()) / X.std()
X_

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.distplot(X, bins=10, color='b')
plt.title('Original', fontsize=12)
plt.subplot(1, 2, 2)
sns.distplot(X_, bins=10, color='r')
plt.title('Standardization', fontsize=12)
plt.show()

# StandardScaler 활용
x_scaled = StandardScaler().fit_transform(df.iloc[:, :4])
x_scaled

# 표준화확인
round(x_scaled.mean(), 2), x_scaled.std()


# 시각화
# 꽃받침Sepal 길이/넓이에 따른 꽃 종류 (target)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(x=df['sepal length (cm)'], y=df.iloc[:, 1],
                hue=df.target, palette='muted')
plt.title('Sepal (Original)', fontsize=12)
plt.subplot(1, 2, 2)
sns.scatterplot(x=x_scaled[:, 0], y=x_scaled[:, 1],
                hue=df.target, palette='muted')
plt.title('Sepal (Scaled)', fontsize=12)
plt.show()

# 꽃잎Petal에 따른 꽃 종류
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(x=df.iloc[:, 2], y=df.iloc[:, 3],
                hue=df.target, palette='muted')
plt.title('Petal (Original)', fontsize=12)
plt.subplot(1, 2, 2)
sns.scatterplot(x=x_scaled[:, 2], y=x_scaled[:, 3],
                hue=df.target, palette='muted')
plt.title('Petal', fontsize=12)
plt.show()

# 정규화 - MinMaxScaler 활용
x_scaler = MinMaxScaler().fit_transform(df.iloc[:, :4])
x_scaler

x_scaler.min(), x_scaler.max()

# 시각화
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
sns.scatterplot(x=df['sepal length (cm)'], y=df.iloc[:, 1],
                hue=df.target, palette='muted')
plt.title('Sepal (Original)', fontsize=12)
plt.subplot(2, 2, 2)
sns.scatterplot(x=x_scaler[:, 0], y=x_scaler[:, 1],
                hue=df.target, palette='muted')
plt.title('Sepal (Scaled)', fontsize=12)
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 3)
sns.scatterplot(x=df.iloc[:, 2], y=df.iloc[:, 3],
                hue=df.target, palette='muted')
plt.title('Petal (Original)', fontsize=12)
plt.subplot(2, 2, 4)
sns.scatterplot(x=x_scaler[:, 2], y=x_scaler[:, 3],
                hue=df.target, palette='muted')
plt.title('Petal', fontsize=12)
plt.show()


# 데이터 분할 train_test_split
df.shape
# sample data
x = df.iloc[:, :4]
y = df.iloc[:, 4]
x.head(3)
y.head(3)

# 주요 hyperparameter
# test_size: validation set에 할당할 비율 (20% -> 0.2), 기본값 0.25
# stratify: 분할된 샘플의 class 갯수가 동일한 비율로 유지
# random_state: 랜덤 시드값
# shuffle: 셔플 옵션, 기본값 True

x_train, x_test, y_train, y_test = train_test_split(
    x, y, stratify=y, test_size=0.2, random_state=30)

x.shape
x_train.shape
x_test.shape
y.shape
y_train.shape
y_test.shape


# KNN
knn = KNeighborsClassifier()
# 학습
knn.fit(x_train, y_train)
# 검증
prediction = knn.predict(x_test)
(prediction == y_test).mean()
knn.score(x_test, y_test)
# 최적값k
for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
    knn.fit(x_train, y_train)
    score = knn.score(x_test, y_test)
    print('k: %d, accuracy: %.2f' % (k, score * 100))
