from consumo_api import get_weather_city


print("BIENENIDO A LA APP DE CLIMA")



print("Ingresar 1 para buscar por ciudad ")
print("Ingresar 2 para buscar por lat y long")
print("Ingresar 8 para salir")  
print()

user = int(input("Porfavor, Ingrese su opcion:" )) 


while ( user == 1 or user== 2 ):

    print("Ingresar 3 para ver pronostico de ahora")
    print("Ingresar 4 para ver pronostico dentro de 4 dias")
    
    print()
    pronostico = int( input ("Porfavor, Ingrese su opcion:"))   


    # pronostico de ahora por ciudad
    if user == 1 and pronostico == 3:
        city = input("Ingresar una ciudad: ")
        params  = {}
        params["q"] = city
        params["appid"] = "a819530cf94d3ae1253831c55d4217af"
        params["units"] = "metric"
        
        url = "https://api.openweathermap.org/data/2.5/weather"

        clima = get_weather_city(url,params)

        print (clima["main"],clima["name"])


    # pronostico de ahora porlat lon  
    elif user == 2 and pronostico == 3:
        lat= input("Ingresar la latitud: ")
        lon=  input("Ingresar la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "a819530cf94d3ae1253831c55d4217af"

        url_coordenadas = "http://api.openweathermap.org/data/2.5/weather"

        clima = get_weather_city(url_coordenadas,params)

        print (clima["main"],clima["name"])



    # ver pronostico 4 dias ciudad
    if user == 1 and pronostico == 4:
        city = input("Ingresar una ciudad para pronostico de 4 dias: ")
        params  = {}
        params["q"] = city
        params["appid"] = "a819530cf94d3ae1253831c55d4217af"
        params["units"] = "metric"
        

        url = "https://api.openweathermap.org/data/2.5/forecast"

        clima = get_weather_city(url,params)

        print()
       
        fecha = clima["list"][1]["dt_txt"]
        datos = clima["list"][1]

        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)

        fecha = clima["list"][6]["dt_txt"]
        datos = clima["list"][6]
        print()
        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)

        fecha = clima["list"][13]["dt_txt"]
        datos = clima["list"][13]
        print()
        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)

        fecha = clima["list"][20]["dt_txt"]
        datos = clima["list"][20]
        print()
        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)

        fecha = clima["list"][27]["dt_txt"]
        datos = clima["list"][27]
        print()
        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)
       


    # ver pronostico 4 dias por lat lon
    elif user == 2 and pronostico == 4:
        lat= input("Ingresar la latitud: ")
        lon=  input("Ingresar la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "a819530cf94d3ae1253831c55d4217af"

        url_coordenadas = "https://api.openweathermap.org/data/2.5/forecast"

        clima = get_weather_city(url_coordenadas,params)

        print()
       
        fecha = clima["list"][1]["dt_txt"]
        datos = clima["list"][1]

        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)

        fecha = clima["list"][6]["dt_txt"]
        datos = clima["list"][6]
        print()
        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)

        fecha = clima["list"][13]["dt_txt"]
        datos = clima["list"][13]
        print()
        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)

        fecha = clima["list"][20]["dt_txt"]
        datos = clima["list"][20]
        print()
        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)

        fecha = clima["list"][27]["dt_txt"]
        datos = clima["list"][27]
        print()
        print("El tiempo para el dia",fecha, "es de: ")
        print (datos)


    print()
    print("Ingresar 1 para buscar por ciudad ")
    print("Ingresar 2 para buscar por lat y long")
    print("Ingresar 8 para salir")  
    
    print()

    user = int(input("Porfavor, Ingrese su opcion:" )) 

print("Gracias por usar nuestra app")