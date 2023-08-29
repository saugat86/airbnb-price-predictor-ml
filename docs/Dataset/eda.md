 <h1><strong> EDA </strong></h1>

The dataset contains 67 columns and 9582 rows and was last scraped 2021-10-26 from the [Inside Airbnb](http://insideairbnb.com/get-the-data/). The dataset contains many features for which you can find more information [here](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit#gid=1322284596). Two features were added. The distance of a listing from Acropolis
and Syntagma, two famous sightseeings in Athens.

<br>

### Explore the data

#### Price

The target variable price is skewed right and thus we perfrom a log transformation for a better understanding.

|                            Price                             |                          Log Price                          |
| :----------------------------------------------------------: | :---------------------------------------------------------: |
| <img src="../img/price_before_log.png" width=500 height=500> | <img src="../img/price_after_log.png" width=500 height=500> |

#### Missing values

|      Missing values       |
| :-----------------------: |
| ![](../img/na_values.png) |

#### Spatial Features

|                Distance from Acropolis vs Price                |                Distance from Syntagma vs Price                |
| :------------------------------------------------------------: | :-----------------------------------------------------------: |
| <img src="../img/Acropolis_vs_price.png" width=500 height=500> | <img src="../img/Syntagma_vs_price.png" width=500 height=500> |

#### Other features

Distributions of some important features of the dataset

|    Distributions     |
| :------------------: |
| ![](../img/attr.png) |

#### Features Correlation

|        Correlation        |
| :-----------------------: |
| ![](../img/feat_corr.png) |
