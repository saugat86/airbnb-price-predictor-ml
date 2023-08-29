import csv
import logging
import os
import string


from airbnb_base_logger import logger


def get_all_airbnb(neighbourhood="all", price_min="all", price_max="all", room_type="all", accommodates="all"):
    """
    Retrieves all airbnb data
    :param neighbourhood
    :param price_min
    :param price_max
    :param room_type
    :param accommodates
    return: dict with all airbnb to return and metadata
    """

    with open(os.getcwd() + '/repo/airbnb.csv', encoding="utf8") as list_file:
        reader = csv.DictReader(list_file)

        airbnb_data = list(reader)
        if (neighbourhood == "all" and price_min == "all" and price_max == "all" and room_type == "all" and accommodates == "all"):
            return {
                "meta": {"count": len(airbnb_data)},
                "airbnb_data": airbnb_data
            }

        if (neighbourhood != "all"):
            airbnb_data = [
                airbnb
                for airbnb in airbnb_data
                if airbnb['neighbourhood'].lower() == neighbourhood.lower()
            ]

        if (price_min != "all"):
            airbnb_data = [
                airbnb
                for airbnb in airbnb_data
                if int(airbnb['price']) >= int(price_min.lower())
            ]
        if (price_max != "all"):
            airbnb_data = [
                airbnb
                for airbnb in airbnb_data
                if int(airbnb['price']) <= int(price_max.lower())
            ]

        if (room_type != "all"):
            airbnb_data = [
                airbnb
                for airbnb in airbnb_data
                if airbnb['room_type'].lower() == room_type.lower()
            ]

        if (accommodates != "all"):
            airbnb_data = [
                airbnb
                for airbnb in airbnb_data
                if int(airbnb['accommodates']) == int(accommodates)
            ]

        return {
            "meta": {"count": len(airbnb_data)},
            "airbnb_data": airbnb_data
        }


def get_airbnb_by_id(id):
    """
    Retrieves the airbnb with the given id if exists.
    :param airbnb_id: The id of the airbnb to return
    :return: dict the requested airbnb or None if not found
    """
    with open(os.getcwd() + '/repo/airbnb.csv') as f:
        reader = csv.DictReader(f)

        data = list(reader)

        for airbnb in data:
            if str(airbnb["id"]) == str(id):
                return {"airbnb": airbnb}

        return None


# TODO
def save(airbnb: dict):
    """
    Similar to update rewrites the file when a new airbnb needs to be saved.
    :param airbnb:
    :return:
    """

    return 42


def delete_airbnb(id):
    """
    Deletes the airbnb with the given id if exists.
    If not exists it will return the information.
    If something goes wrong it will log the exception and return None

    :param airbnb_id: The id of the employee to return
    :return: dict the requested employee or None if not found
    """
    logging.info(f"Attempting to delete airbnb {id}")
    try:
        found = False
        with open(os.getcwd() + "/repo/airbnb.csv", "r+") as f:

            data = list(csv.reader(f))
            import pprint

            for record in data:
                if record[0] == str(id):
                    found = True

            if not found:
                logger.error(f"Could not delete airbnb {id}: Not Found")
                return {"error": "not found"}

        with open(os.getcwd() + "/repo/airbnb.csv", "w+") as f:
            writer = csv.writer(f)
            for airbnb in data:
                if airbnb[0] != str(id):
                    writer.writerow(airbnb)

        return {"success": True}
    except Exception as exception:
        logger.error(f"Could not delete airbnb {exception}")
        return None

    finally:
        pass
