# Pfizer-dsmasterclass-2022-team1

# Airbnb Price Prediction Project

[![Version](https://img.shields.io/badge/version-0.7.0-blue.svg)](https://bitbucket.org/lbesson/ansi-colors)


## Table of contents

- [Introduction](#introduction)

- [Background](#back)

- [Objectives](#obj)

- [Data](#data)

- [Methodology](#methodology)

- [Conclusion](#conclusion)

- [Authors](#authors)

<a name="introduction"></a>

## Documentation

You can check the documentaion of the app [here](https://imanousar.github.io/airbnb-price-predictor/) and the deployed app [here](https://airbnb-price-prediction-project.netlify.app/).

## Introduction

This is a group project implemented as part of the Pfizer X Code Hub Data Masterclass Bootcamp

<p align="center">
  <img src ="docs/img/Data-Science-Masterclass-1.png" width = "500"   height="600" title="photo">  
</p>

<a name="back"></a>

## Background

Airbnb is a home-sharing platform that allows home-owners and renters (‘hosts’) to put their properties (‘listings’) online, so that guests can pay to stay in them. Hosts are expected to set their own prices for their listings. Although Airbnb and other sites provide some general guidance, there are currently no free and accurate services which help hosts price their properties using a wide range of data points.

<a name="obj"></a>

## Objectives

The main idea of this project is to select and handle approprately the given data in order to predict as accurately as possible the price of an airbnb listing in Athens.

- Identify which features affect the pricing of a listing
- Train ML models to obtain the most accurate predictive results

<a name="data"></a>

## Data

The actual data used for this project was provided to us by the Academy of Code Hub. It consists of 67 columns and 9582 rows each representing a unique listing in Athens.

<a name="methodology"></a>

## Methodology

To find the best model in order to predict the price of a listing, a selection of Machine Learning and Neural Network methods were used. We used a Linear Regression as the baseline model. For a more thorough experiment and analysis we applied machine learning classical models, which we tuned, specifically we implemented a Linear Regression model,a Random Forest model, a Lasso model, an Extra Trees Regressor, a LightGbm and an XGBoost model.Going a step further various neural network models were trained, which unfortunately did not seem to capture the relationship between the target variable price and the explanatory features that well.
Furthermore, in this particular project, trying to increase efficiency, we used Grid Search and cross validation to improve performance . Later a comparative analysis of these regression models was implemented. All the models were trained on the training data and evaluated using the test dataset. The XGBoost one, was the one with the lowest mean squared error and highest accuracy scores. The evaluation results are comprised of R-squared, mean absolute error, mean absolute percentage error and mean squared error.

<a name="conclusion"></a>

## Conclusion

In conclusion, this project provides a solution for predicting the price of an airbnb listing, utilizing real world data from airbnb with machine learning algorithms that we applied. Beginning with the data preprocessing, we examined our data carefully with various visualizations and other tasks. We handled categorical data accordingly by creating dummies, converted true/false values to binary (0/1), removed unecessary features and even created our own features with the help of existing ones. In advance, we proceeded on transforming the target variable from simple to log (y) in order to resemble the normal distribution and capture the essence of all price ranges. Then, we segregated the data for training and testing and implemented a series of Machine Learning algorithms to obtain the best accuracy results. From this project, we resulted on the XGboost model, as the one which minimized the mean absolute error in comparison to the rest, for predicting the price of an airbnb listing.

## Authors

- [Giannis Manousaridis](https://github.com/imanousar)

- [Tzeni Tsobanaj](https://github.com/jenny-cobanaj)
