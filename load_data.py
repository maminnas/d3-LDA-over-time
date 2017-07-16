import sys,os
# run this using django shell -- uncomment the last lines of this file
# $ django-admin shell < load_data.py

# Specify path and name to tsv files
topic_filepathname="../topics/topics.txt"
doc_filepathname="../topics/document_topic_distributions.txt"

# sys.path.append(djangoproject_home) 
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings' 
def populate_topic(file_path):
	import csv
	from lda.models import *
	dataReader = csv.reader(open(file_path), delimiter='\t', quotechar='"') 
	for row in dataReader:
		# print row
		if row[0] != 'topic':# Ignore the header row, import everything else 
			# print row[0], row[1]
			topic = topics()
			topic.topic_id = int(row[0])
			topic.words = row[1]
			topic.save()

def populate_doc_topic(file_path):
	import csv
	from lda.models import *
	dataReader = csv.reader(open(file_path), delimiter='\t', quotechar='"') 
	for i,row in enumerate(dataReader):
		if row[0] != 'id':# Ignore the header row, import everything else 
			# print row[0], row[1]
			# from lda.models import *
			distr = doc_topic_distrib()
			distr.doc_id = int(row[0])
			distr.title = row[1]
			distr.datetime = row[2]
			distr.t0 = float(row[3])
			distr.t1 = float(row[4])
			distr.t2 = float(row[5])
			distr.t3 = float(row[6])
			distr.t4 = float(row[7])
			distr.t5 = float(row[8])
			distr.t6 = float(row[9])
			distr.t7 = float(row[10])
			distr.t8 = float(row[11])
			distr.t9 = float(row[12])
			distr.t10 = float(row[13])
			distr.t11 = float(row[14])
			distr.t12 = float(row[15])
			distr.t13 = float(row[16])
			distr.t14 = float(row[17])
			distr.t15 = float(row[18])
			distr.t16 = float(row[19])
			distr.t17 = float(row[20])
			distr.t18 = float(row[21])
			distr.t20 = float(row[23])
			distr.t21 = float(row[24])
			distr.t22 = float(row[25])
			distr.t23 = float(row[26])
			distr.t24 = float(row[27])
			distr.t25 = float(row[28])
			distr.t26 = float(row[29])
			distr.t27 = float(row[30])
			distr.t28 = float(row[31])
			distr.t29 = float(row[32])
			distr.t30 = float(row[33])
			distr.t31 = float(row[34])
			distr.t32 = float(row[35])
			distr.t33 = float(row[36])
			distr.t34 = float(row[37])
			distr.t35 = float(row[38])
			distr.t36 = float(row[39])
			distr.t38 = float(row[41])
			distr.t39 = float(row[42])
			distr.t40 = float(row[43])
			distr.t41 = float(row[44])
			distr.t42 = float(row[45])
			distr.t43 = float(row[46])
			distr.t44 = float(row[47])
			distr.t45 = float(row[48])
			distr.t46 = float(row[49])
			distr.t47 = float(row[50])
			distr.t48 = float(row[51])
			distr.t49 = float(row[52])
			
			distr.save()
			if i%1000==0:
				print 'line:', i

# if __name__=='__main__':
# populate_topic(topic_filepathname)
# populate_doc_topic(doc_filepathname)