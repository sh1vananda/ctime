from fastapi import HTTPException
import requests
from bs4 import BeautifulSoup

def get_time_for_location(country: str, city: str):
    url = f'https://www.timeanddate.com/worldclock/{country}/{city}'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Location not found or invalid URL")

    soup = BeautifulSoup(response.text, 'html.parser')
    
    time_element = soup.find('span', {'id': 'ct'})
    
    if time_element:
        return time_element.text.strip()
    
    raise HTTPException(status_code=404, detail="Time not found")