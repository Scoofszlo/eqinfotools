from datetime import datetime
from eqinfoscraper.constants import VALID_DATE_FORMATS

def display_overview(eq_stats):
    month_and_year = _get_month_and_year(eq_stats)
    strongest_eq_location = eq_stats["strongest"]["location"]
    strongest_eq_mag = eq_stats["strongest"]["magnitude"]
    weakest_eq_location = eq_stats["weakest"]["location"]
    weakest_eq_mag = eq_stats["weakest"]["magnitude"]
    total_recorded = eq_stats["recorded_eqs"]["total"]
    total_m8_0_or_greater = eq_stats["recorded_eqs"]["total_per_magnitude"]["m8_0_or_greater"]
    total_m6_to_m7_9 = eq_stats["recorded_eqs"]["total_per_magnitude"]["m6_to_7_9"]
    total_m4_0_to_5_9 = eq_stats["recorded_eqs"]["total_per_magnitude"]["m4_0_to_5_9"]
    total_below_m4_0 = eq_stats["recorded_eqs"]["total_per_magnitude"]["below_m4_0"]

    result = f""""Overview for {month_and_year}"

Strongest       : M{strongest_eq_mag} @ {strongest_eq_location}
Weakest         : M{weakest_eq_mag} @ {weakest_eq_location}
Total Recorded  : {total_recorded}
        >=M8.0  : {total_m8_0_or_greater}
        M6–M7.9 : {total_m6_to_m7_9}
        M4–M5.9 : {total_m4_0_to_5_9}
        <=M4.0  : {total_below_m4_0}
"""
    print(result)

def display_all_entries(eq_list,
                        location=True,
                        date=True,
                        coordinates=True,
                        depth=True,
                        magnitude=True,
                        link=True,
                        image=True
                        ):
    
    attributes_to_display = []

    if location:
        attributes_to_display.append(["Location", "location"])
    if date:
        attributes_to_display.append(["Date", "date"])
    if coordinates:
        attributes_to_display.append(["Coordinates", "coordinates"])
    if depth:
        attributes_to_display.append(["Depth", "depth"])
    if magnitude:
        attributes_to_display.append(["Magnitude", "magnitude"])
    if link:
        attributes_to_display.append(["EQ Details Link", "eq_details_link"])
    if image:
        attributes_to_display.append(["Image Link", "image_link"])

    for every_entry in eq_list:
        for attribute in attributes_to_display:
            print(f"{attribute[0]}: {every_entry[attribute[1]]}")
        print()

def _get_month_and_year(eq_stats):
    date_format = VALID_DATE_FORMATS["PHIVOLCS"][0]

    start_date = datetime.strptime(eq_stats["date_range"]["start_date"], date_format)
    end_date = datetime.strptime(eq_stats["date_range"]["end_date"], date_format)

    if start_date.month == end_date.month:
        return str(start_date.strftime("%B %Y"))
    else:
        if start_date.year == end_date.year:
            return str(start_date.strftime("%B") + "–" + end_date.strftime("%B %Y"))
        else:
            return str(start_date.strftime("%B %Y") + "–" + end_date.strftime("%B %Y"))