
class Analyzer:
    def __init__(self, weather_data: dict, city: str):
        self.city = city
        self.weather_data = weather_data
        self.min_temprature = weather_data["daily"]["temperature_2m_min"]
        self.max_temprature = weather_data["daily"]["temperature_2m_max"]
        self.daylight_duration = weather_data["daily"]["daylight_duration"]
        self.rain_sum = weather_data["daily"]["rain_sum"]

    def generate_analysis(self) -> str:
        """
        Generate analysis and return it as a string.
        Args:
            weather_data: dict
        Returns:
            str
        """
        lowest_avg_temp = sum(self.min_temprature) / len(self.min_temprature)
        highest_avg_temp = sum(self.max_temprature) / len(self.max_temprature)
        daylight_avg_duration = sum(self.daylight_duration) / len(self.daylight_duration)
        rain_avg_amount = sum(self.rain_sum) / len(self.rain_sum)

        analysis_str = f"Report analysis for {self.city} - past 7 days:\n"
        analysis_str += f"Average lowest temperature:  {str(lowest_avg_temp)}\n"
        analysis_str += f"Average highest temperature:  {str(highest_avg_temp)}\n"
        analysis_str += f"Average daylight duration:  {str(daylight_avg_duration)}\n"
        analysis_str += f"Total rain amount:  {str(rain_avg_amount)}\n"
        return analysis_str

