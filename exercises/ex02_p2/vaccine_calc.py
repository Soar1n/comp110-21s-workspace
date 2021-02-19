"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730331250"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population = int(input("Population: "))
    doses = int(input("Doses administered: "))
    doses_per_day = int(input("Doses per day: "))
    target_percent_vaccinated = int(input("Target_percent vaccinated: "))
    days_until = days_to_target(population, doses, doses_per_day, target_percent_vaccinated)
   
    Days_Store = days_to_target(population, doses, doses_per_day, target_percent_vaccinated)
    FutDay = future_date(days_until)
    print(">>>>" + str(days_until))
    print("Population: " + (str(population)))
    print("Doses administered: " + str(doses))
    print("Doses per day: " + str(doses_per_day))
    print("Target percent vaccinated: " + str(target_percent_vaccinated))

    print(f"We will reach {target_percent_vaccinated}% vaccination in {Days_Store} days, which falls on {FutDay}.")


# 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target_percent_vaccinated: int) -> int:
    """Days to target."""
    doses_administered2 = ((float(doses) / 2)) 
    doses_per_day2 = ((float(doses_per_day / 2)))
    population_percent = float(((target_percent_vaccinated * .01) * population))
    difference = population_percent - doses_administered2
    return round(difference / doses_per_day2)

# 3: Define future_date function


def future_date(days_until: int) -> str:
    """Future date."""
    today: datetime = datetime.today()
    dayz: timedelta = timedelta(float(days_until))
    tomorrow: datetime = today + dayz
    return (tomorrow.strftime("%B %d, %Y"))


if __name__ == "__main__":
    main()
