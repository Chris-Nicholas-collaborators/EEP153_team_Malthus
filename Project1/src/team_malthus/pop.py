import datetime
from typing import Any

import wbdata

# with open("../src/team_malthus/iso_countries.txt") as file:
# for item in file:
# country_codes.append(item.strip())

# due to problems with path differences between importing
# this in the top-level notebook versus the unit test,
# just inline this list for now ...

country_codes = [
    "ABW",
    "AFE",
    "AFG",
    "AFR",
    "AFW",
    "AGO",
    "ALB",
    "AND",
    "ARB",
    "ARE",
    "ARG",
    "ARM",
    "ASM",
    "ATG",
    "AUS",
    "AUT",
    "AZE",
    "BDI",
    "BEA",
    "BEC",
    "BEL",
    "BEN",
    "BFA",
    "BGD",
    "BGR",
    "BHI",
    "BHR",
    "BHS",
    "BIH",
    "BLA",
    "BLR",
    "BLZ",
    "BMN",
    "BMU",
    "BOL",
    "BRA",
    "BRB",
    "BRN",
    "BSS",
    "BTN",
    "BWA",
    "CAA",
    "CAF",
    "CAN",
    "CEA",
    "CEB",
    "CEU",
    "CHE",
    "CHI",
    "CHL",
    "CHN",
    "CIV",
    "CLA",
    "CME",
    "CMR",
    "COD",
    "COG",
    "COL",
    "COM",
    "CPV",
    "CRI",
    "CSA",
    "CSS",
    "CUB",
    "CUW",
    "CYM",
    "CYP",
    "CZE",
    "DEA",
    "DEC",
    "DEU",
    "DJI",
    "DLA",
    "DMA",
    "DMN",
    "DNK",
    "DNS",
    "DOM",
    "DSA",
    "DSF",
    "DSS",
    "DZA",
    "EAP",
    "EAR",
    "EAS",
    "ECA",
    "ECS",
    "ECU",
    "EGY",
    "EMU",
    "ERI",
    "ESP",
    "EST",
    "ETH",
    "EUU",
    "FCS",
    "FIN",
    "FJI",
    "FRA",
    "FRO",
    "FSM",
    "FXS",
    "GAB",
    "GBR",
    "GEO",
    "GHA",
    "GIB",
    "GIN",
    "GMB",
    "GNB",
    "GNQ",
    "GRC",
    "GRD",
    "GRL",
    "GTM",
    "GUM",
    "GUY",
    "HIC",
    "HKG",
    "HND",
    "HPC",
    "HRV",
    "HTI",
    "HUN",
    "IBB",
    "IBD",
    "IBT",
    "IDA",
    "IDB",
    "IDN",
    "IDX",
    "IMN",
    "IND",
    "INX",
    "IRL",
    "IRN",
    "IRQ",
    "ISL",
    "ISR",
    "ITA",
    "JAM",
    "JOR",
    "JPN",
    "KAZ",
    "KEN",
    "KGZ",
    "KHM",
    "KIR",
    "KNA",
    "KOR",
    "KWT",
    "LAC",
    "LAO",
    "LBN",
    "LBR",
    "LBY",
    "LCA",
    "LCN",
    "LDC",
    "LIC",
    "LIE",
    "LKA",
    "LMC",
    "LMY",
    "LSO",
    "LTE",
    "LTU",
    "LUX",
    "LVA",
    "MAC",
    "MAF",
    "MAR",
    "MCO",
    "MDA",
    "MDE",
    "MDG",
    "MDV",
    "MEA",
    "MEX",
    "MHL",
    "MIC",
    "MKD",
    "MLI",
    "MLT",
    "MMR",
    "MNA",
    "MNE",
    "MNG",
    "MNP",
    "MOZ",
    "MRT",
    "MUS",
    "MWI",
    "MYS",
    "NAC",
    "NAF",
    "NAM",
    "NCL",
    "NER",
    "NGA",
    "NIC",
    "NLD",
    "NOR",
    "NPL",
    "NRS",
    "NRU",
    "NXS",
    "NZL",
    "OED",
    "OMN",
    "OSS",
    "PAK",
    "PAN",
    "PER",
    "PHL",
    "PLW",
    "PNG",
    "POL",
    "PRE",
    "PRI",
    "PRK",
    "PRT",
    "PRY",
    "PSE",
    "PSS",
    "PST",
    "PYF",
    "QAT",
    "ROU",
    "RRS",
    "RUS",
    "RWA",
    "SAS",
    "SAU",
    "SDN",
    "SEN",
    "SGP",
    "SLB",
    "SLE",
    "SLV",
    "SMR",
    "SOM",
    "SRB",
    "SSA",
    "SSD",
    "SSF",
    "SST",
    "STP",
    "SUR",
    "SVK",
    "SVN",
    "SWE",
    "SWZ",
    "SXM",
    "SXZ",
    "SYC",
    "SYR",
    "TCA",
    "TCD",
    "TEA",
    "TEC",
    "TGO",
    "THA",
    "TJK",
    "TKM",
    "TLA",
    "TLS",
    "TMN",
    "TON",
    "TSA",
    "TSS",
    "TTO",
    "TUN",
    "TUR",
    "TUV",
    "TZA",
    "UGA",
    "UKR",
    "UMC",
    "URY",
    "USA",
    "UZB",
    "VCT",
    "VEN",
    "VGB",
    "VIR",
    "VNM",
    "VUT",
    "WLD",
    "WSM",
    "XKX",
    "XZN",
    "YEM",
    "ZAF",
    "ZMB",
    "ZWE",
]


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
        raise ValueError("age values invalid")


def get_indicator_id(age: int, sex: str):
    """Get the right 5-year indicator this age falls into."""
    # get lower bound - do modulo 5
    lower_bucket_bound = (int(age / 5)) * 5
    upper_bucket_bound = lower_bucket_bound + 4
    upper_bucket_bound_str = None
    if upper_bucket_bound > 79:
        upper_bucket_bound = "UP"
        upper_bucket_bound_str = "UP"
    else:
        upper_bucket_bound_str = str(upper_bucket_bound)
        if upper_bucket_bound < 10:
            upper_bucket_bound_str = "0" + str(upper_bucket_bound)

    lower_bucket_bound_str = str(lower_bucket_bound)
    if lower_bucket_bound < 10:
        lower_bucket_bound_str = "0" + lower_bucket_bound_str
    indicator = "SP.POP." + lower_bucket_bound_str + upper_bucket_bound_str
    # presumes queries are already validated
    if sex == "m":
        indicator += ".MA"
    else:
        indicator += ".FE"

    sex_label = None
    if sex == "m":
        sex_label = "male"
    else:
        sex_label = "female"
    indicator_label = f"{sex_label}_{lower_bucket_bound}_{upper_bucket_bound}"
    return indicator, indicator_label


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
        of 70-74, 75-79, 80 and above. high ages are clamped to 84
    place -- an ISO 3166 3-letter country or region identifier
    """
    age_range_parts = age_range.split("-")
    low_age_str = age_range_parts[0]
    high_age_str = age_range_parts[1]
    # trying to cast to int will throw a ValueErrors
    low_age = int(low_age_str)
    high_age = int(high_age_str)
    if high_age > 84:
        high_age = 84
    validate(year, sex, low_age, high_age, place)

    # walk through the years, and identify the relevant indicators to fetch.
    indicators = {}
    population_count = 0
    data_date = datetime.datetime(year, 1, 1), datetime.datetime(year, 1, 1)

    for age in range(low_age, high_age + 1):
        if sex == "p" or sex == "m":
            indicator_to_use, indicator_label = get_indicator_id(age, "m")
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
            indicator_to_use, indicator_label = get_indicator_id(age, "f")
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


def population_df(country: Any):
    """Get a dataframe with global age breakdowns,
    indexed by Region or Country."""
    indicators = {}
    # just blindly go through the age range in male and female
    # deduping along the way
    for age in range(0, 81):
        for sex in ["m", "f"]:
            next_indicator, next_indicator_label = get_indicator_id(age, sex)
            if next_indicator not in indicators:
                indicators[next_indicator] = next_indicator_label
    world = wbdata.get_dataframe(indicators, country)
    return world


if __name__ == "__main__":
    test_pop = population(year=2020, sex="p", age_range="13-24", place="USA")
    print(test_pop)

    test_df = population_df(country=["USA", "NAM"])
    print("done")
