from django.shortcuts import render
from django.http import HttpResponse
from firebase import Firebase
import json

# Create your views here.


#def index(request):
#    return HttpResponse(u"Welcome to AlphaNodus Nest Controller")

def home(request):
    
    # Virtual DEvice
    #f=Firebase('https://developer-api.nest.com/devices/thermostats/N96fw5MnBnmwH4ZBZVOgvMwgbVqewXOS',auth_token="c.9tKvASa4R9fG9hx8kFb9QeUMzxo5OalPNFY9YswzKzENRKn51hNdnx6ctVVjQgRUiCbumqTgFZtWnBDtJFzXLFM8QgdlwtRjWtB3rgfDog5juDNHXdpON9XtNyzulgjMJnPYIbgS74bQ8cUc")   
    # ACL Device
    #f=Firebase('https://developer-api.nest.com/devices/thermostats/Q3Vcf1OhcRbUfcweDwMdCkNGApfAG1NY',auth_token="c.Q2DQ3IxfJwtrqg6vMRDjQHx4DBF30BoAwv8kOmV5wSCsTmFPTZR8gLxURcomK3tvWgvJAzpCFNfnZt7b56Va1YkxUaGwpgOXjBpX1gg7vPUj6ayinv8DCGSIzsx5Klz58xRVEtaS1ZBVlTyG")   
    
    #rst = f.get()
    #string = "Current Humidity is: \r\n" +  str(rst.get('humidity'))
    #return render(request, 'home.html', {'string': string})
    return render(request, 'home.html')

def set_temp(request):
    # Virtual DEvice
    f=Firebase('https://developer-api.nest.com/devices/thermostats/N96fw5MnBnmwH4ZBZVOgvMwgbVqewXOS',auth_token="c.9tKvASa4R9fG9hx8kFb9QeUMzxo5OalPNFY9YswzKzENRKn51hNdnx6ctVVjQgRUiCbumqTgFZtWnBDtJFzXLFM8QgdlwtRjWtB3rgfDog5juDNHXdpON9XtNyzulgjMJnPYIbgS74bQ8cUc")   
    # ACL Device
    #f=Firebase('https://developer-api.nest.com/devices/thermostats/Q3Vcf1OhcRbUfcweDwMdCkNGApfAG1NY',auth_token="c.Q2DQ3IxfJwtrqg6vMRDjQHx4DBF30BoAwv8kOmV5wSCsTmFPTZR8gLxURcomK3tvWgvJAzpCFNfnZt7b56Va1YkxUaGwpgOXjBpX1gg7vPUj6ayinv8DCGSIzsx5Klz58xRVEtaS1ZBVlTyG")   
    tar_temp = request.GET['a']
    tar_temp = int(tar_temp)
    f.put({"target_temperature_f":tar_temp})
    return HttpResponse(str(tar_temp))

def get_nest(request):
    # Virtual DEvice
    #f=Firebase('https://developer-api.nest.com/devices/thermostats/N96fw5MnBnmwH4ZBZVOgvMwgbVqewXOS',auth_token="c.9tKvASa4R9fG9hx8kFb9QeUMzxo5OalPNFY9YswzKzENRKn51hNdnx6ctVVjQgRUiCbumqTgFZtWnBDtJFzXLFM8QgdlwtRjWtB3rgfDog5juDNHXdpON9XtNyzulgjMJnPYIbgS74bQ8cUc")   
    # ACL Device
    f=Firebase('https://developer-api.nest.com/devices/thermostats/Q3Vcf1OhcRbUfcweDwMdCkNGApfAG1NY',auth_token="c.Q2DQ3IxfJwtrqg6vMRDjQHx4DBF30BoAwv8kOmV5wSCsTmFPTZR8gLxURcomK3tvWgvJAzpCFNfnZt7b56Va1YkxUaGwpgOXjBpX1gg7vPUj6ayinv8DCGSIzsx5Klz58xRVEtaS1ZBVlTyG")   
    rst = f.get()
    #hum = str(rst.get('humidity'))
    return HttpResponse(json.dumps(rst))
