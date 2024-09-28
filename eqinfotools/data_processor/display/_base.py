from abc import ABC, abstractmethod
from datetime import datetime
from eqinfotools.constants import VALID_DATE_FORMATS


class DisplayEQData(ABC):
    def __init__(self, eq_list, eq_stats):
        self._eq_list = eq_list
        self._eq_stats = eq_stats

    def display_overview(self):
        month_and_year = self._get_month_and_year()
        strongest_eq_location = self._get_strongest_eq_location()
        strongest_eq_mag = self._get_strongest_eq_mag()
        weakest_eq_location = self._get_weakest_eq_location()
        weakest_eq_mag = self._get_weakest_eq_mag()
        total_recorded = self._get_total_recorded()
        total_m8_0_or_greater = self._get_total_m8_0_or_greater()
        total_m6_to_m7_9 = self._get_total_m6_to_m7_9()
        total_m4_0_to_5_9 = self._get_total_m4_0_to_5_9()
        total_below_m4_0 = self._get_total_below_m4_0()

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

    @abstractmethod
    def display_all_entries():
        pass

    def _get_strongest_eq_location(self):
        return self._eq_stats["strongest"]["location"]

    def _get_strongest_eq_mag(self):
        return self._eq_stats["strongest"]["magnitude"]

    def _get_weakest_eq_location(self):
        return self._eq_stats["weakest"]["location"]

    def _get_weakest_eq_mag(self):
        return self._eq_stats["weakest"]["magnitude"]

    def _get_total_recorded(self):
        return self._eq_stats["recorded_eqs"]["total"]

    def _get_total_m8_0_or_greater(self):
        return self._eq_stats["recorded_eqs"]["total_per_magnitude"]["m8_0_or_greater"]

    def _get_total_m6_to_m7_9(self):
        return self._eq_stats["recorded_eqs"]["total_per_magnitude"]["m6_to_7_9"]

    def _get_total_m4_0_to_5_9(self):
        return self._eq_stats["recorded_eqs"]["total_per_magnitude"]["m4_0_to_5_9"]

    def _get_total_below_m4_0(self):
        return self._eq_stats["recorded_eqs"]["total_per_magnitude"]["below_m4_0"]

    def _get_month_and_year(self):
        date_format = VALID_DATE_FORMATS["DEFAULT"][0]

        start_date = datetime.strptime(self._eq_stats["date_range"]["start_date"], date_format)
        end_date = datetime.strptime(self._eq_stats["date_range"]["end_date"], date_format)

        if start_date.month == end_date.month:
            return start_date.strftime("%B %Y")
        else:
            if start_date.year == end_date.year:
                return start_date.strftime("%B") + "–" + end_date.strftime("%B %Y")
            else:
                return start_date.strftime("%B %Y") + "–" + end_date.strftime("%B %Y")