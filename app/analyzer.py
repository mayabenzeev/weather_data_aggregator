class Analyzer:
    def __init__(self, weather_data: dict, city: str):
        self.city = city
        self.weather_data = weather_data
        self.min_temprature = weather_data["daily"]["temperature_2m_min"]
        self.max_temprature = weather_data["daily"]["temperature_2m_max"]
        self.daylight_duration = weather_data["daily"]["daylight_duration"]
        self.rain_sum = weather_data["daily"]["rain_sum"]

        self.min_temp_units = weather_data["daily_units"]["temperature_2m_min"]
        self.max_temp_units = weather_data["daily_units"]["temperature_2m_max"]
        self.daylight_units = weather_data["daily_units"]["daylight_duration"]
        self.rain_units = weather_data["daily_units"]["rain_sum"]

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

        analysis["lowest_avg_temp"] = f"{lowest_avg_temp} {self.min_temp_units}"
        analysis["highest_avg_temp"] = f"{highest_avg_temp} {self.max_temp_units}"
        analysis["daylight_avg_duration"] = f"{(daylight_avg_duration / 60):.2f} minutes"
        analysis["rain_avg_amount"] = f"{rain_avg_amount} {self.rain_units}"

        return analysis
    
    def generate_info_report(self) -> dict:
        """
        Generate info report and return it as a beautified json.
        Args:
            weather_data: dict
        Returns:
            dict
        """
        info_report = {}
        info_report["city"] = self.city

        dates = self.weather_data["daily"]["time"]
        max_temps = self.weather_data["daily"]["temperature_2m_max"]
        min_temps = self.weather_data["daily"]["temperature_2m_min"]
        daylight_durations = self.weather_data["daily"]["daylight_duration"]
        rain_amounts = self.weather_data["daily"]["rain_sum"]

        for i, date in enumerate(dates):
            info_report[date] = {
                "max_temp": f"{max_temps[i]} {self.max_temp_units}",
                "min_temp": f"{min_temps[i]} {self.min_temp_units}",
                "daylight_duration": f"{daylight_durations[i]} {self.daylight_units}",
                "rain_amount": f"{rain_amounts[i]} {self.rain_units}"
            }

        return info_report


