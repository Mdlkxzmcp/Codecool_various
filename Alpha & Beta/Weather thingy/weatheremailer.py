# -*- coding: utf-8 -*-
import weather
import mailer
import filehandler


def main():
    emails = filehandler.get_emails()
    schedule = filehandler.get_schedule()
    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails, schedule, forecast)

if __name__ == '__main__':
    main()
