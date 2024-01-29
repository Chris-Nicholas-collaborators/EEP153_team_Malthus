import wbdata
import datetime
import sys
from typing import Any

country_codes = []

with open("./src/team_malthus/iso_countries.txt") as file:
    for item in file:
        country_codes.append(item.strip())


def validate(
    year: int,
    sex: str,
    low_age: int,
    high_age: int,
    place: str,
    dataframe_flag: bool = False,
    options: Any = None,
) -> None:
    """Validate inputs to the population function."""
    if (year < 2000) or (year > 2020):
        raise ValueError("year must be between 2000 and 2020")
    if sex not in ["m", "f", "p"]:
        raise ValueError("sex must be m, f, or p (for total)")

    if (
        (low_age < 0)
        or (low_age > 79)
        or (high_age < 1)
        or (high_age > 120)
        or (low_age > high_age)
    ):
        print("invalid date range: low must be between 0 and 80 ; high < 120")
        sys.exit(-1)

    low_age = None
    high_age = None


def get_indicator_id(age: int, sex: str) -> str:
    """Get the right 5-year indicator this age falls into."""
    # get lower bound - do modulo 5
    lower_bucket_bound = (int(age / 5)) * 5
    upper_bucket_bound = lower_bucket_bound + 4
    if upper_bucket_bound > 79:
        upper_bucket_bound = "UP"
    indicator = "SP.POP." + str(lower_bucket_bound) + str(upper_bucket_bound)
    # presumes queries are already validated
    if sex == "m":
        indicator += ".MA"
    else:
        indicator += ".FE"

    return indicator


def population(year: int, sex: str, age_range: str, place: str) -> int:
    """Function to get population estimates for a single year and place.

    Variables:
    year -- the year requested
    sex -- one of 'm' for male, 'f' for female, 'p' for total
    age_range -- age range of the form low:high inclusive. Numbers above
        80 will return the entire "80 and up" range, whereas other values will
        include a linear proportion of the 5-year range bucket. For example,
        a range of 13-21 will obtain 40% of the population ages 10-14, all of
        ages 15-19, and 40 % of the ages 20-24 buckets. 70-90 will return all
        of 70-74, 75-79, 80 and above. 90-100 will throw an error.
    place -- an ISO 3166 3-leter country or region identifier
    """
    age_range_parts = age_range.split("-")
    low_age_str = age_range_parts[0]
    high_age_str = age_range_parts[1]
    # trying to cast to int will throw a ValueErrors
    low_age = int(low_age_str)
    high_age = int(high_age_str)
    validate(year, sex, low_age, high_age, place)

    # walk through the years, and identify the relevant indicators to fetch.
    indicators = {}
    population_count = 0
    data_date = datetime.datetime(year, 1, 1), datetime.datetime(year, 1, 1)

    for age in range(low_age, high_age + 1):
        if sex == "p" or sex == "m":
            indicator_to_use = get_indicator_id(age, "m")
            this_indicator = None
            if indicator_to_use not in indicators:
                # cache it
                fetched_indicator = wbdata.get_data(
                    indicator_to_use, country=place, data_date=data_date
                )
                indicators[indicator_to_use] = fetched_indicator
            this_indicator = indicators[indicator_to_use]
            population_count += int((0.2) * this_indicator[0]["value"])
        if sex == "p" or sex == "f":
            indicator_to_use = get_indicator_id(age, "f")
            this_indicator = None
            if indicator_to_use not in indicators:
                # cache it
                fetched_indicator = wbdata.get_data(
                    indicator_to_use, country=place, data_date=data_date
                )
                indicators[indicator_to_use] = fetched_indicator
            this_indicator = indicators[indicator_to_use]
            population_count += int((0.2) * this_indicator[0]["value"])

    return population_count


if __name__ == "__main__":
    test_pop = population(
        year=2020,
        sex="p",
        age_range="13-24",
        place="USA")
    print(test_pop)
