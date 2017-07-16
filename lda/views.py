# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms import ModelForm
from django import forms
from models import *
import json
import time

def clean_words(topic, n):
	for s in topic:
		w=''
		r=''
		i=0
		c=0
		while i < len(s.words) and c<n:
			w+=s.words[i]
			if s.words[i]==',':
				r+=w
				w=''
				c+=1
				while i<len(s.words) and s.words[i]!='|':
					i+=1
			i+=1
		s.words = r
	return topic

def index(request):
	topic = topics.objects.all()
	topic = clean_words(topic, 10)
	ser_topic = serializers.serialize('json', topic)
	context = { 'topics': ser_topic }
	return render(request, 'graph/graph.html', context)

def topic_over_time(request):
	print ("-----------------------")
	print ("Retrieving objects")
	t1=time.time()
	# data = doc_topic_distrib.objects.exclude(attributes = ["doc_id","title"]).values(datetime__year, datetime__month, datetime__day).aggregate(Max())
	data = doc_topic_distrib.objects.all()
	data = data[::100]
	t2=time.time()
	print ("objects retrieved in:", t2-t1)
	ser = serializers.serialize('json', list(data))
	t3 = time.time()
	print ("Serialized in:", t3-t2)
	# actual_data = [d['fields'] for d in ser]
	# output = json.dumps(actual_data)
	# print output
	return JsonResponse(ser, safe=False)
