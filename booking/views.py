from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from booking.models import Car
import json


# Create your views here.


conn = mysql.connector.MySQLConnection(host='127.0.0.1',port='3306',
                                       database='Car_rental',
                                       user='root',
                                       password='')

def home(request):
	return render(request,'home.html');



def get_nearby_loc(lat,log,conn):
	cursor = conn.cursor()
	cursor.execute(""" SELECT id,driver_name,number_plate,latitude,longitude, ( 6371 * acos( cos( radians(%s) ) * cos( radians( latitude ) ) 
* cos( radians( longitude ) - radians(%s) ) + sin( radians(%s) ) * sin(radians(latitude)) ) ) AS distance 
FROM Cars 
HAVING distance < 30 
ORDER BY distance 
LIMIT 0 , 3; """,(lat,log,lat))

	data = cursor.fetchall()
	return [list(i)[3:5] for i in data],[list(i) for i in data]



def search(request):
	lat = request.GET['latitude']
	log = request.GET['longitude']
	res,json_res = get_nearby_loc(lat,log,conn)
	res = res +[[float(lat),float(log)]]
	output = []
	for i in res:
		dic = {"latitude":i[0],"longitude":i[1]}
		output.append(dic)
	print(output)
	print(json_res)
	return render(request,"result.html",{'points': output,'output':json_res})

def stats(request):
	cars = Car.objects.all()
	return render(request,'stats.html',{'car':cars})
	

def AddDriver(request):
	if request.method == 'GET':
		try:
			name = request.GET.get('name')
			car_num = request.GET.get('car_number')
			contact = request.GET.get('contact')
			lat = request.GET.get('latitude')
			log = request.GET.get('longitude')
			print(name,car_num,contact,lat,log)
			cursor = conn.cursor()
			sql = "INSERT INTO Cars (driver_name,number_plate,contact,latitude,longitude) VALUES (%s,%s,%s,%s,%s)"
			val = (name,car_num,contact,lat,log)
			print(name,car_num,contact,lat,log)
			cursor.execute(sql,val)
			conn.commit()
			return render(request,'driver.html')
		except:
			return render(request,'driver.html')

