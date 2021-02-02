from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import table1
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import ReqSerializer
from rest_framework import status
from rest_framework import generics
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Avg, Count, Sum, Min, Max

# Create your views here.

@api_view(['POST'])
def home(request):
	tutorial_data = JSONParser().parse(request)
	data = ""
	length = 0
	column_name = []

	try:
		database_name = tutorial_data["database_name"]
		table_name = tutorial_data["data"]["table_name"]
		
		if table_name == "table1" and database_name == "database1":
			column_name = [field.name for field in table1._meta.get_fields()]
			data = list(table1.objects.values())
			length = len(data)
			status_code = status.HTTP_200_OK
		else:
			data="Wrong Table Name Or DB name"
			status_code = status.HTTP_400_BAD_REQUEST
	except:
		data = "Either database_name or table_name is not given."
	return JsonResponse({'column':column_name,'data': data, 'length':length}, status = status_code)


@api_view(['POST'])
def test_api(request):
	tutorial_data = JSONParser().parse(request)
	data = ""
	col_list= []
	length = 0
	status_code = status.HTTP_400_BAD_REQUEST
	try:
		database_name = tutorial_data["database_name"]
		table_name = tutorial_data["data"]["worksheet_id"]

		select_list = tutorial_data["data"]["select_list"]
		col_list = []
		for i in range(len(select_list)):
			column = tutorial_data["data"]["select_list"][i]
			col_list.append(column)

		
		if table_name == "table1" and database_name == "database1":
			final_data = [x['column'] for x in col_list]
			data_out = table1.objects.values_list(*final_data)
			data = list(data_out)
			
			length = len(data)
			status_code = status.HTTP_200_OK
		else:
			data = "wrong table name"
			status_code = status.HTTP_400_BAD_REQUEST
	except:
		data = "Either database_name or table_name is not given."
		status_code = status.HTTP_400_BAD_REQUEST
	return JsonResponse({'column':final_data,'data': data, 'length':length}, status = status_code)


@api_view(['POST'])
def test_api2(request):
	tutorial_data = JSONParser().parse(request)
	data = ""
	col_list= []
	length = 0
	status_code = status.HTTP_400_BAD_REQUEST
	try:
		database_name = tutorial_data["database_name"]
		table_name = tutorial_data["data"]["worksheet_id"]
		aggregate = tutorial_data["data"]["aggregate"]
		groupby = tutorial_data["data"]["groupby"]
		final_groupby = [x['column'] for x in groupby]
		gby_string = " ,".join(final_groupby)
		
		agg_list = []
		
		for i in range(len(aggregate)):
			column = tutorial_data["data"]["aggregate"][i]
			agg_list.append(column)

		
		if table_name == "table1" and database_name == "database1":
			
			for x in agg_list:
				val = x['column']
				if x['type'] == 'sum':
					data_out = table1.objects.values(str(gby_string)).annotate(sum_of_price=Sum(str(val)))
				elif x['type'] == 'avg':
					data_out = table1.objects.values(str(gby_string)).annotate(avg_of_price=Avg(str(val)))
				elif x['type'] == 'count':
					data_out = table1.objects.values(str(gby_string)).annotate(count_of_price=Count(str(val)))
				elif x['type'] == 'min':
					data_out = table1.objects.values(str(gby_string)).annotate(min_of_price=Min(str(val)))
				elif x['type'] == 'max':
					data_out = table1.objects.values(str(gby_string)).annotate(max_of_price=Max(str(val)))
				elif x['type'] == 'distinct count':
					data_out = table1.objects.values(str(gby_string)).annotate(dist_count_of_price=Count(str(val), distinct=True))
			
			dat_out = [x.keys() for x in data_out]
			
			for k in dat_out:
				col_list.append(list(k))
			
			labels = []
			
			if x['type'] == 'sum':
				for d in data_out:
					labels.append([d['city'], d['sum_of_price']])
			elif x['type'] == 'avg':
				for d in data_out:
					labels.append([d['city'], d['avg_of_price']])	
			elif x['type'] == 'count':
				for d in data_out:
					labels.append([d['city'], d['count_of_price']])
			elif x['type'] == 'min':
				for d in data_out:
					labels.append([d['city'], d['min_of_price']])
			elif x['type'] == 'max':
				for d in data_out:
					labels.append([d['city'], d['max_of_price']])
			elif x['type'] == 'distinct count':
				for d in data_out:
					labels.append([d['city'], d['dist_count_of_price']])

			data = list(labels)
			
			length = len(data)
			status_code = status.HTTP_200_OK
		else:
			
			data = "wrong table name"
			status_code = status.HTTP_400_BAD_REQUEST
	except:
		
		data = "Either database_name or table_name is not given."
		status_code = status.HTTP_400_BAD_REQUEST
	return JsonResponse({'column': col_list,'data': data, 'length':length})
	# return JsonResponse({'data': data, 'length':length})
