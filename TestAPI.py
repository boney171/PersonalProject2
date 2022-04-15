import requests
import json
city = []

try:
     api_request= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92126&distance=5&API_KEY=A965BFEF-761E-4713-800A-0C166473C53B")
     api = json.loads(api_request.content)
except Exception as e:
      api = "Error..."

San_Diego = f"{api[0]['ReportingArea']}, {api[0]['StateCode']}, Air Quality Index: {api[0]['AQI']},{api[0]['Category']['Name']} "
 
city.append(San_Diego)


try:
     api_request1= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=30303&distance=5&API_KEY=A965BFEF-761E-4713-800A-0C166473C53B")
     api1 = json.loads(api_request1.content)
except Exception as e:
      api1 = "Error..."

Atlanta = f"{api1[0]['ReportingArea']}, {api[0]['StateCode']}, Air Quality Index: {api1[0]['AQI']},{api1[0]['Category']['Name']} "

city.append(Atlanta)


try:
     api_request2= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94114&distance=5&API_KEY=A965BFEF-761E-4713-800A-0C166473C53B")
     api2 = json.loads(api_request2.content)
except Exception as e:
      api2 = "Error..."

SanFran = f"{api2[0]['ReportingArea']}, {api2[0]['StateCode']}, Air Quality Index: {api2[0]['AQI']},{api2[0]['Category']['Name']} "

city.append(SanFran)


try:
     api_request3= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92503&distance=5&API_KEY=A965BFEF-761E-4713-800A-0C166473C53B")
     api3 = json.loads(api_request3.content)
except Exception as e:
      api3 = "Error..."

Riverside = f"{api3[1]['ReportingArea']}, {api3[1]['StateCode']}, Air Quality Index: {api3[1]['AQI']},{api3[1]['Category']['Name']} "

city.append(Riverside)


try:
     api_request4= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=27695&distance=25&API_KEY=A965BFEF-761E-4713-800A-0C166473C53B")
     api4 = json.loads(api_request4.content)
except Exception as e:
      api4 = "Error..."

Rayleigh = f"{api4[1]['ReportingArea']}, {api4[1]['StateCode']}, Air Quality Index: {api4[1]['AQI']},{api4[1]['Category']['Name']} "

city.append(Rayleigh)

print(Rayleigh)

try:
     api_request5= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60625&distance=25&API_KEY=A965BFEF-761E-4713-800A-0C166473C53B")
     api5 = json.loads(api_request5.content)
except Exception as e:
      api5 = "Error..."

Chicago = f"{api5[1]['ReportingArea']}, {api5[1]['StateCode']}, Air Quality Index: {api5[1]['AQI']},{api5[1]['Category']['Name']} "

city.append(Chicago)

print(Chicago)
