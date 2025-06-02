
class Analyzer:
    def __init__(self, weather_data: dict, city: str):
        self.city = city
        self.weather_data = weather_data
        self.min_temprature = weather_data["daily"]["temperature_2m_min"]
        self.max_temprature = weather_data["daily"]["temperature_2m_max"]
        self.daylight_duration = weather_data["daily"]["daylight_duration"]
        self.rain_sum = weather_data["daily"]["rain_sum"]

    def generate_analysis(self) -> dict:
        """
        Generate analysis and return it as a json.
        Args:
            weather_data: dict
        Returns:
            dict
        """
        analysis = {}
        analysis["city"] = self.city

        lowest_avg_temp = sum(self.min_temprature) / len(self.min_temprature)
        highest_avg_temp = sum(self.max_temprature) / len(self.max_temprature)
        daylight_avg_duration = sum(self.daylight_duration) / len(self.daylight_duration)
        rain_avg_amount = sum(self.rain_sum) / len(self.rain_sum)

        analysis["lowest_avg_temp"] = lowest_avg_temp
        analysis["highest_avg_temp"] = highest_avg_temp
        analysis["daylight_avg_duration"] = daylight_avg_duration
        analysis["rain_avg_amount"] = rain_avg_amount

        return analysis
    
    def generate_info_report(self) -> dict:
        """
        Generate info report and return it as a beutified json.
        Args:
            weather_data: dict
        Returns:
            dict
        """
        info_report = {}
        info_report["city"] = self.city

        max_units = self.weather_data["daily_units"]["temperature_2m_max"]
        min_units = self.weather_data["daily_units"]["temperature_2m_min"]
        daylight_units = self.weather_data["daily_units"]["daylight_duration"]
        rain_units = self.weather_data["daily_units"]["rain_sum"]

        dates = self.weather_data["daily"]["time"]
        max_temps = self.weather_data["daily"]["temperature_2m_max"]
        min_temps = self.weather_data["daily"]["temperature_2m_min"]
        daylight_durations = self.weather_data["daily"]["daylight_duration"]
        rain_amounts = self.weather_data["daily"]["rain_sum"]

        for date in dates:
            info_report[date] = {
                "max_temp": f"{max_temps[date]} {max_units}",
                "min_temp": f"{min_temps[date]} {min_units}",
                "daylight_duration": f"{daylight_durations[date]} {daylight_units}",
                "rain_amount": f"{rain_amounts[date]} {rain_units}"
            }

        return info_report


