import requests

def getCasesData():
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

    text = "Last Updated: " + updated_at + "\n" + "\n" + "Total Cases: " + total_cases + "\n" + "Active Cases: " + active_cases + "\n" + "Recovered: " + recovered + "\n" + "Deaths: " + deaths + "\n" + "New Local Cases: " + new_cases + "\n" + "In Observation: " + in_observation + "\n" + "Total PCR Testing: " + total_pcr + "\n" + "New Local Deaths in Last 24 Hours: " + new_deaths
    return text