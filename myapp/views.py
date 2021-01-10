from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club
import yfinance as yf
from pandas_datareader import data as pdr
import datetime as dt
from django.http import JsonResponse
yf.pdr_override() 
# Create your views here.

class ClubChartView(TemplateView):

	def index(request):
		return render(request, 'clubs/index.html')

	def get_data(request):
	    df = pdr.get_data_yahoo('^GSPC', '2020-01-01')
	    df = df.reset_index()
	    df = df.iloc[:, :-1]

	    # 실수데이터를 정수로 축약
	    for col in df.columns[1:]:
        	df[col] = df[col].astype('int')

	    # value 들을 문자로 바꾼다
	    for col in df.columns:
        	df[col] = df[col].astype('str')
        	df_list = df.values.tolist()

	    data = {'titleSet' : 'S&P 500',
	            'dataSet'  : df_list}
	    return JsonResponse(data, safe=False)

	def get_data2(request):
	    df = pdr.get_data_yahoo('^GSPC', '2019-01-01')
	    df = df.reset_index()
	    df = df.iloc[:, :-1]

	    # 실수데이터를 정수로 축약
	    for col in df.columns[1:]:
        	df[col] = df[col].astype('int')

	    # value 들을 문자로 바꾼다
	    for col in df.columns:
        	df[col] = df[col].astype('str')
        	df_list = df.values.tolist()

	    data = {'titleSet' : 'S&P 500',
	            'dataSet'  : df_list}
	    return JsonResponse(data, safe=False)


	def get_data3(request):
	    df = pdr.get_data_yahoo('^GSPC', '2020-01-01')
	    df = df.reset_index()
	    df = df.iloc[:, :-1]

	    # 실수데이터를 정수로 축약
	    for col in df.columns[1:]:
        	df[col] = df[col].astype('int')

	    # value 들을 문자로 바꾼다
	    for col in df.columns:
        	df[col] = df[col].astype('str')
        	df_list = df.values.tolist()

	    data = {'titleSet' : 'S&P 500',
	            'dataSet'  : df_list}
	    return JsonResponse(data, safe=False)