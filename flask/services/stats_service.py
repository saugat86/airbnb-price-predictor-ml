import csv
import logging
import os
import string
from typing import List
import pandas as pd


from airbnb_base_logger import logger


def main():
    """
    Invokes the methods from this service and generates a dict with this format:
        {
        "stats": {
            "histogram_data": [
                {
                    "price_range": "0-50",
                    "count": 21
                    },
                {
                    "price_range": "50-100",
                    "count": 56
                    },
                {
                    "price_range": "100-max",
                    "count": 23
                    }
            ],

            "pie_chart_data": [
                {
                    "room_type": "Private room",
                    "count": 123
                    },
                {
                    "room_type": "Entire home/apt",
                    "count": 53
                    },
                {
                    "room_type": "Hotel room",
                    "count": 13
                    },
                {
                    "room_type": "Shared room",
                    "count": 9
                    }
            ]
            .....
        }
    }
    :return:
    """
    price_range = price_categories()
    rooms = room_types()
    acropilis_prices = price_based_on_monument_dist("Dist_Acropolis")
    syntagma_prices = price_based_on_monument_dist("Dist_Syntagma")
    accommodates_price = price_based_on_accommodates()
    reviews_price = reviews()
    price_vs_area = price_based_on_area()
    return {"stats": {"histogram_data": price_range, "pie_chart_data": rooms, "bar_char_data_1": acropilis_prices,
                      "bar_char_data_2": syntagma_prices, "bar_char_data_3": accommodates_price,
                      "bar_char_data_4": reviews_price, "bar_char_data_5": price_vs_area}}


def price_categories() -> List:
    """
    Counts the airbnb based on three price ranges. 
    From 0-50, 50-100 and 100 and over it. 
    """

    airbnb_df = pd.read_csv(os.getcwd() + "/repo/airbnb.csv")
    range0_50 = airbnb_df[airbnb_df['price'] <= 50].shape[0]
    range50_100 = airbnb_df[(airbnb_df['price'] > 50) & (
        airbnb_df['price'] <= 100)].shape[0]
    range100_max = airbnb_df[airbnb_df['price'] > 100].shape[0]

    dict_to_return = [{"price_range": "0-50", "count": range0_50},
                      {"price_range": "50-100", "count": range50_100},
                      {"price_range": "100-max", "count": range100_max}]

    return dict_to_return


def room_types() -> List:
    """
    Counts the airbnb based on their room type. There are four
    categories  Entire home/apt, Private room, Hotel room, Shared room
    """
    airbnb_df = pd.read_csv(os.getcwd() + "/repo/airbnb.csv")

    private_room = int(airbnb_df['room_type'].value_counts()['Private room'])
    entire_home_apt = int(
        airbnb_df['room_type'].value_counts()['Entire home/apt'])
    hotel_room = int(airbnb_df['room_type'].value_counts()['Hotel room'])
    Shared_room = int(airbnb_df['room_type'].value_counts()['Shared room'])

    dict_to_return = [{"room_type": "Private room", "count": private_room},
                      {"room_type": "Entire home/apt", "count": entire_home_apt},
                      {"room_type": "Hotel room", "count": hotel_room},
                      {"room_type": "Shared room", "count": Shared_room}]

    return dict_to_return


def price_based_on_monument_dist(s) -> List:
    """
    Calculates average price of houses grouped by their distance from
    Acropolis. Group 1: 0-1km, Group 2: 1-2 km, Group 3: 2-4 km, 
    Group 4: 4-max km
    """

    airbnb_df = pd.read_csv(os.getcwd() + "/repo/airbnb.csv")

    # Crete a mask based on the distance from Acropolis and the calculate the mean of the price column
    price0_1 = airbnb_df[airbnb_df[s] <= 1]['price'].mean()
    price1_2 = airbnb_df[(airbnb_df[s] > 1) & (
        airbnb_df[s] <= 2)]['price'].mean()
    price2_3 = airbnb_df[(airbnb_df[s] > 2) & (
        airbnb_df[s] <= 3)]['price'].mean()
    price3_4 = airbnb_df[(airbnb_df[s] > 3) & (
        airbnb_df[s] <= 4)]['price'].mean()
    price4_5 = airbnb_df[(airbnb_df[s] > 4) & (
        airbnb_df[s] <= 5)]['price'].mean()
    price5_max = airbnb_df[airbnb_df[s] > 5]['price'].mean()

    if s == 'Dist_Acropolis':
        msg = 'Distance_from_Acropolis'
    elif s == 'Dist_Syntagma':
        msg = 'distance_from_Syntagma'

    dict_to_return = [{msg: "0-1 km", "avg_price": price0_1},
                      {msg: "1-2 km", "avg_price": price1_2},
                      {msg: "2-3 km", "avg_price": price2_3},
                      {msg: "3-4 km", "avg_price": price3_4},
                      {msg: "4-5 km", "avg_price": price4_5},
                      {msg: "5-max km", "avg_price": price5_max}]

    return dict_to_return


def price_based_on_accommodates() -> List:
    """
    Counts the airbnb price based on acoomodates. 
    """

    airbnb_df = pd.read_csv(os.getcwd() + "/repo/airbnb.csv")

    range1_2 = airbnb_df.loc[airbnb_df['accommodates'] <= 2, ["price"]].sum(
    )[0] / airbnb_df.loc[airbnb_df['accommodates'] <= 2].shape[0]

    range3_5 = airbnb_df.loc[(airbnb_df['accommodates'] < 2) & (airbnb_df['accommodates'] <= 5), ["price"]].sum(
    )[0] / airbnb_df.loc[(airbnb_df['accommodates'] < 2) & (airbnb_df['accommodates'] <= 5)].shape[0]

    range6_8 = airbnb_df.loc[(airbnb_df['accommodates'] < 5) & (airbnb_df['accommodates'] <= 8), ["price"]].sum(
    )[0] / airbnb_df.loc[(airbnb_df['accommodates'] < 5) & (airbnb_df['accommodates'] <= 8)].shape[0]

    range9_max = airbnb_df.loc[airbnb_df['accommodates'] > 8, [
        "price"]].sum()[0] / airbnb_df.loc[airbnb_df['accommodates'] > 8].shape[0]

    dict_to_return = [{"accommodates": "1-2", "avg_price": range1_2},
                      {"accommodates": "3-5", "avg_price": range3_5},
                      {"accommodates": "6-8", "avg_price": range6_8},
                      {"accommodates": "9-max", "avg_price": range9_max}]

    return dict_to_return


def reviews():
    """
    Counts the airbnb price based on acoomodates room type. 
    """

    airbnb_df = pd.read_csv(os.getcwd() + "/repo/airbnb.csv")

    range0_1 = airbnb_df.loc[airbnb_df['reviews_per_month'] <= 1, ["price"]].sum(
    )[0] / airbnb_df.loc[airbnb_df['reviews_per_month'] <= 1].shape[0]

    range1_2 = airbnb_df.loc[(airbnb_df['reviews_per_month'] < 1) & (airbnb_df['reviews_per_month'] <= 2), ["price"]].sum(
    )[0] / airbnb_df.loc[(airbnb_df['reviews_per_month'] < 1) & (airbnb_df['reviews_per_month'] <= 2)].shape[0]

    range2_4 = airbnb_df.loc[(airbnb_df['reviews_per_month'] < 2) & (airbnb_df['reviews_per_month'] <= 4), ["price"]].sum(
    )[0] / airbnb_df.loc[(airbnb_df['reviews_per_month'] < 2) & (airbnb_df['reviews_per_month'] <= 4)].shape[0]

    range4_max = airbnb_df.loc[airbnb_df['reviews_per_month'] > 4, [
        "price"]].sum()[0] / airbnb_df.loc[airbnb_df['reviews_per_month'] > 4].shape[0]

    dict_to_return = [{"reviews_per_month": "0-1", "avg_price": range0_1},
                      {"reviews_per_month": "1-2", "avg_price": range1_2},
                      {"reviews_per_month": "2-4", "avg_price": range2_4},
                      {"reviews_per_month": "4-max", "avg_price": range4_max}]

    return dict_to_return


def price_based_on_area() -> List:
    """
    Calculates average price based on area
    """

    airbnb_df = pd.read_csv(os.getcwd() + "/repo/airbnb.csv")

    s = airbnb_df.groupby('neighbourhood', as_index=False)['price'].mean()

    list_to_return = []
    for index, row in s.iterrows():
        list_to_return.append(
            {"area": row['neighbourhood'],
             "avg_price": row['price']
             }
        )
    return list_to_return
