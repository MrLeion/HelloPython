#coding=utf-8
import sys,os
import qiniu
from qiniu import Auth
from qiniu import BucketManager

 
access_key = 'your access_key'
secret_key = 'your secret_key'
bucket_name = 'your bucket_name'
bucket_domain = 'your bucket_domain'
q = Auth(access_key,secret_key)
bucket = BucketManager(q)
def upload(f,key):
	if os.path.splitext(f)[1] in ['.jpg','.png','.JPG','.PNG']:
		mime_type = "image/*"
		token = q.upload_token(bucket_name, key)
		ret, info = qiniu.put_file(token, key, f, mime_type=mime_type, check_crc=True)
		print(info)
adir = '/Users/tangzenglei/Desktop/test'

 
def scanDir():
	count = 0
	for parent,dirnames,filenames in os.walk(adir):
		print ('-----------------------')
		print ("parent is:" + parent)
		print ('-----------------------')
		count += len(filenames)
		for filename in filenames:
			filepath = os.path.join(parent,filename)
			key = filepath.replace('/Users/tangzenglei/Desktop/test/qiniu/','')
			print ("key is:" + key)
			upload(filepath,key)
	print (count)
scanDir()
