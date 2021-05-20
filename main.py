import requests
import tkinter as tk
import datetime

def getCovidData():
    api = "https://www.hpb.health.gov.lk/api/get-current-statistical"
    json_data = requests.get(api).json()
    
    total_cases = str('{:,}'.format(json_data['data']['local_total_cases']))
    active_cases = str('{:,}'.format(json_data['data']['local_active_cases']))
    recovered = str('{:,}'.format(json_data['data']['local_recovered']))
    deaths = str('{:,}'.format(json_data['data']['local_deaths']))
    new_cases = str('{:,}'.format(json_data['data']['local_new_cases']))
    in_observation = str('{:,}'.format(json_data['data']['local_total_number_of_individuals_in_hospitals']))
    total_pcr = str('{:,}'.format(json_data['data']['total_pcr_testing_count']))
    new_deaths = str('{:,}'.format(json_data['data']['local_new_deaths']))

    updated_at = json_data['data']['update_date_time']
    dt = datetime.datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S')
    
    year = dt.year
    month = (datetime.datetime.strptime(str(dt.month), "%m")).strftime("%B")
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    last_updated_time = "{}-{}-{} \t{}:{}:{}".format(year, month, day, hour, minute, second)   

    label2.config(text = "Covid-19 Tracker - Sri Lanka")
    label.config(text =
        "\n" + "Last Updated: " + last_updated_time + "\n" +
        "\n" + "Total Cases: " + total_cases +
        "\n" + "Active Cases: " + active_cases +
        "\n" + "Recovered: " + recovered +
        "\n" + "Deaths: " + deaths +
        "\n" + "Local New Cases: " + new_cases +
        "\n" + "In Observation: " + in_observation +
        "\n" + "Total PCR Testing: " + total_pcr +
        "\n" + "New Local Deaths in Last 24 Hours: " + new_deaths
    )
    
canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title("Corona Tracking App")  

f = ("poppins", 17, "bold")
heading = ("poppins", 25, "bold", "underline")
button = tk.Button(canvas, font = f, text = "Reload", command = getCovidData)
button.pack(pady = 20)

label2 = tk.Label(canvas, font= heading)
label2.pack()
label = tk.Label(canvas, font=f)
label.pack(pady=20)

getCovidData()
canvas.mainloop()
