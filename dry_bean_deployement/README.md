<div style="text-align: center;">
  <h2>
    <span style="color: #8B5A2B; font-weight: bold; text-decoration: underline;">
      Dry Bean Capstone Project
    </span>
  </h2>
</div>

## Data Fields
The dataset consists of features describing the shape of the bean and you're required to predict it's type.
- ID - an ID for this instance
- Area - (A), The area of a bean zone and the number of pixels within its boundaries.
- Perimeter - (P), Bean circumference is defined as the length of its border.
- MajorAxisLength - (L), The distance between the ends of the longest line that can be drawn from a bean.
- MinorAxisLength - (l), The longest line that can be drawn from the bean while standing perpendicular to the main axis.
- AspectRatio - (K), Defines the relationship between L and l.
- Eccentricity - (Ec), Eccentricity of the ellipse having the same moments as the region.
- ConvexArea - (C), Number of pixels in the smallest convex polygon that can contain the area of a bean seed.
- EquivDiameter - (Ed), The diameter of a circle having the same area as a bean seed area.
- Extent - (Ex), The ratio of the pixels in the bounding box to the bean area.
- Solidity - (S), Also known as convexity. The ratio of the pixels in the convex shell to those found in beans.
- Roundness - (R), Calculated with the following formula: (4piA)/(P^2)
- Compactness - (CO), Measures the roundness of an object: Ed/L
- ShapeFactor1 - (SF1)
- ShapeFactor2 - (SF2)
- ShapeFactor3 - (SF3)
- ShapeFactor4 - (SF4)
- y - the class of the bean. It can be any of BARBUNYA, SIRA, HOROZ, DERMASON, CALI, BOMBAY, and SEKER.

**Data Types of Attribues and Non-Null values Count**
<br>
All attributes are continuous type except the class attribute which contains Bean Type.
*   There are no missing values in the dataset

* The dataset has an unequal distribution of datapoints in various classes.
* This is an imbalanced dataset.
* DERMASON is the most dominant class.
* BOMBAY is the most rare class.

*   The distribution of BOMBAY class in many attribtes like *Area*, *MinorAxisLength*, *Convex Area*, *Minor Axis Length*, *ShapeFactor1* is well separated from other classes.
*   *Area* & Convex Area have very similar distribution across all classes indicating very high correlation.
* Distribution of *DERMASON* is very similar *SEKER* in many attributes for e.g. roundness, solidity, ShapeFactor2
* For the **extent** attribute the range of values is similar for all the bean classes which indicates that the bounding box to the bean area(measured  by extent attribute)  represented for all classes is equally good.

* Box plot analysis show there are lot of outliers in some attributes like **solidity**, **roundness** , **ShapeFactor4**
* There are verly less oultiers for the attribute **extent**
* It can be seen that Bombay and Horoz class are distinct from other classes for many attributes

* For various attributes Bombay class clearly differs from other classes as observed in the  violin plot

* Many of the attributes are highly correlated as observed from the correlation matrix below, thus PCA would be an apt choice to reduce the dimensionality and produce uncorrelated features.
* There a lot of highly correlated attributes in the above correlation matrix, for eg: </br>

    *   **Area & Convex Area**:1
    *   **Shaped Factor3 & Comapctness**:1
    *   **Aspect ration & compactness**: -0.99
    *   **Area & Perimeter**: 0.97
    *   **Perimeter & ShapeFactor1**: -0.87
    *   **Aspect ration & Eccentricity**: 0.92 </br>
* Some attributes with low level of correlation among them:
    *   **Extent & EquivDiameter**: 0.029
    *   **Solidity & Eccentricity**: -0.3
    *   **Compactnes & Area**: -0.27

    ### **Overall Summary of insights from the EDA**

*   The distribution of BOMBAY class in many attributes like *Area*, *MinorAxisLength*, *Convex Area*, *Minor Axis Length*, *ShapeFactor1* is well separated from other classes.
*   *Area* & Convex Area have very similar distribution across all classes indicating very high correlation.
* For the **extent** attribute the range of values is similar for all the bean classes which indicates that the bounding box to the bean area(measured  by extent attribute)  represented for all classes is equally good.
* Some attributes like **Shape Factor2, Solidity** exhibit highly skewed distribiution with long tails.
*   Box plot analysis show there are lot of outliers in some attributes like **solidity**, **roundness**, **ShapeFactor4**.
* For various attributes Bombay class clearly differs from other classes as observed from the violin plot and box plot.
* Many of the attributes are highly correlated as observed from the correlation matrix above, thus PCA would be an apt choice to reduce the dimensionality and produce uncorrelated features.

*   Contrary to the usual expectations, Multinomial Naive bayes is performing better than Gaussian Naive bayes on this dataset.
*   The input attributes of this dataset are contninous real values and Multinomial NB works best when input attributes are categorical in nature.
* However the results indicate better metrics for Multinomial NB.
* A possible reason of this discrepancy could be that the continous feature values are repeated for many datapoints which gives them a categorical nature, thus making the Multinomial NB probability estimates better than the Gaussian one.

## **Multinomial Logsitic Regression on the dataset and comparison with Gaussian Naive Bayes**


*   Performed below is Multinomial Logsitic Regression on this dataset.
*   There are various hyperparameters available for Logistic Regression such as:</br>
max_iter, multi_class, penalty, solver,
* We  are tuning two hyperparameters values i.e. max_iter and verbose and keeping all others set to their default values.
* max_iter: MAximum no of iterations taken by the Logistic Regression algorithm
* verbose: Produces the logging output
* The best performance is coming  when **max_iter** is set to 150 and **verbose** is set to 1.

Logsitic Regression is performing better than Gaussian Naive Bayes for all the three choices of hyperparameters , the best is in the case when max_iter is set to 150

