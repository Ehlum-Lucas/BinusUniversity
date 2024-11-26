
**Enhanced Hands-On Activity Instructions:**

### 1. Choose Your Data and Plot Type:

- **Line Plot:**
  - **Data:**
    ```python
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    ```
  - **Instructions:** Plot this data using `plt.plot()`.

- **Scatter Plot:**
  - **Data:**
    ```python
    x = [10, 20, 30, 40, 50]
    y = [15, 25, 35, 45, 55]
    ```
  - **Instructions:** Plot this data using `plt.scatter()`.

- **Bar Chart:**
  - **Data:**
    ```python
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [5, 10, 15, 20, 25]
    ```
  - **Instructions:** Plot this data using `plt.bar()`.

### 2. Customize Your Plot:

- **Line Plot Customization:**
  - **Color:** `#ff6347` (Tomato)
  - **Line Style:** `--` (dashed)
  - **Line Width:** 2
  - **Marker:** `o` (circle)

- **Scatter Plot Customization:**
  - **Color:** `#1e90ff` (Dodger Blue)
  - **Marker Size:** 50
  - **Marker Style:** `^` (triangle up)

- **Bar Chart Customization:**
  - **Color:** `#32cd32` (Lime Green)
  - **Bar Width:** 0.5
  - **Add Horizontal Grid Lines:** `plt.grid(True, axis='x')`

### 3. Add Labels, Title, and Annotations:

- **Line Plot:**
  - **X-axis Label:** 'X-axis'
  - **Y-axis Label:** 'Y-axis'
  - **Title:** 'Line Plot of Prime Numbers'
  - **Annotation:** Add an annotation for the maximum y-value with `plt.annotate()`.

- **Scatter Plot:**
  - **X-axis Label:** 'X Values'
  - **Y-axis Label:** 'Y Values'
  - **Title:** 'Scatter Plot with Triangle Markers'
  - **Annotation:** Add an annotation for the point `(40, 45)` using `plt.annotate()`.

- **Bar Chart:**
  - **X-axis Label:** 'Categories'
  - **Y-axis Label:** 'Values'
  - **Title:** 'Bar Chart with Custom Width'
  - **Annotation:** Label each bar with its corresponding value using `plt.text()`.

### 4. Additional Customizations:

- **Grid Lines:** Add grid lines to all plots.
- **Legend:** Include a legend for each plot type.
- **Save the Plot:** Save the generated plot as a PNG file using `plt.savefig('plot.png')`.

### 5. Submission Instructions:

1. **Complete Your Plot:** Implement the instructions to create and customize your plot.
2. **Push to GitHub:** Upload your code and plot images to your GitHub repository.
3. **Pull Request:** Create a pull request with a description of your customizations.
4. **Approval:** Your pull request will be reviewed. If accepted, it means your plot meets the requirements.

