# TA Exercise: Visualizing the Iris Dataset

In this exercise, you will analyze and visualize the **Iris dataset**. Each task is designed to build your skills in real-world data visualization. Work on each task independently, but feel free to ask your TA for guidance if needed.

---

## Objectives

1. Understand the structure of the Iris dataset.
2. Use visualizations to explore patterns and relationships.
3. Draw insights from data visualizations.

---

## Prerequisites

Ensure the following:
1. Python is installed with `pandas`, `matplotlib`, and `seaborn`.
2. You have the `iris.csv` file provided by your TA.

---

## Exercise 1: Load and Inspect the Data

### **Task 1.1: Load the Dataset**
- Load the Iris dataset using `pandas`.
- Display the first 5 rows of the dataset.

**Hints:**
- Use `pd.read_csv()` to load the file.
- Use `.head()` to display the rows.

---

### **Task 1.2: Check the Dataset**
1. How many rows and columns does the dataset have?
2. Are there any missing values?

**Code Block (Start with this):**
```python
# Load the dataset
import pandas as pd
iris = pd.read_csv("iris.csv")

# Your solution here
```

---

## Exercise 2: Basic Visualizations

### **Task 2.1: Histograms**
- Create histograms for each numerical feature.
- Use 20 bins for better granularity.

**Questions:**
- Which feature has the most variability?

**Challenge:** Customize the colors of the histograms using Matplotlib.

---

### **Task 2.2: Boxplots**
- Create a boxplot for each numerical feature.

**Questions:**
1. Identify features with outliers.
2. Are there significant differences in the range of values for features?

**Code Block (Start with this):**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Your solution here
```

---

## Exercise 3: Relationships Between Features

### **Task 3.1: Pairwise Scatterplots**
- Use Seaborn's `pairplot()` to create scatterplots of all features.
- Add a color hue to differentiate species.

**Questions:**
1. Are there any pairs of features that clearly separate the species?
2. Which features seem most correlated?

**Challenge:** Use `diag_kind='kde'` to add kernel density estimates for diagonal plots.

---

### **Task 3.2: Correlation Heatmap**
- Compute the correlation matrix and visualize it as a heatmap.
- Annotate the heatmap with correlation values.

**Questions:**
- Which pair of features is most strongly correlated?
- Does this correlation make sense based on the scatterplots?

**Hint:** Use `sns.heatmap()` for the visualization.

---

## Exercise 4: Advanced Visualizations

### **Task 4.1: Violin Plots**
- Create a violin plot for `sepal_length` grouped by species.

**Questions:**
- Which species has the widest spread for `sepal_length`?
- How does the median `sepal_length` vary across species?

**Challenge:** Add split violins (`split=True`) to compare distributions more clearly.

---

### **Task 4.2: 3D Scatter Plot**
- Create a 3D scatter plot for `sepal_length`, `sepal_width`, and `petal_length`.

**Questions:**
1. Are there distinct clusters in 3D space for the species?
2. How do these clusters compare to the pairwise scatterplots?

**Hint:** Use `Axes3D` from `mpl_toolkits.mplot3d`.

---

## Exercise 5: Draw Insights

### **Task 5.1: Create a Dashboard of Insights**
- Summarize your findings in a dashboard format using:
  - A heatmap for correlations.
  - A scatterplot for the two most correlated features.
  - A violin plot for `petal_length` grouped by species.

**Questions:**
1. Which features are most useful for distinguishing species?
2. Are there any unexpected patterns?

---

## Bonus Challenge

### **Task 6.1: Interactive Visualizations**
- Use `plotly` or `bokeh` to create interactive versions of the scatterplots and histograms.

**Challenge Question:**
- How does interactivity help in exploring the dataset?

---

## Submission Instructions

1. Save your final work in a Jupyter Notebook or `.py` file.
2. Include brief answers to the questions posed in each task.
3. Submit your work to the TA for review.
