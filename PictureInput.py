import re
filename= input("Text filename:");
#input_file_name = 'input_file.txt'
#output_file_name = 'austin_output_file.txt'
#input_file_handle = open(filename, 'r')
#output_file_handle = open(filename, 'w')
with open(filename)as f:
	contents=f.read();
	edit1= contents.replace("async",""); 
	edit1= edit1.replace('href',"")
	edit1= edit1.replace('title',"")
	edit1= edit1.replace('charset="utf-8"></script>',"")
	edit1= edit1.replace('<a',"")
	edit1= edit1.replace('src="//embedr.flickr.com/assets/client-code.js"',"")
	edit1= edit1.replace('data-flickr-embed="true"',"")
	edit1= re.sub(r'\=.*?\img','',edit1)
	edit1= re.sub(r'\href=".*?\/"','',edit1)
	edit1= re.sub(r'\height=".*?\"','',edit1)
	edit1= re.sub(r'\></a.*?\ipt','',edit1)
	#edit1= re.sub(r'\le<.*?\img','',edit1)
#	edit1= re.sub(r'\t.*?g','',edit1,flags=re.DOTALL)
	edit1= edit1.split('\n');
	edit1= [s[4:-1] for s in edit1]
	edit1= edit1[:69]
	count=0
	def print_output(s,c):
		print("<p>" + str(c) )
		c=c+1	
		print("<>br><img",s) 
		print("")
	for s in edit1:
		print_output(s,count+1);
		count = count + 1
#	edit2= edit1.replace('"data-flickr-embed="true"',"") 
#	edit3= {x.replace("async","") for x in edit2}
#	edit4= {x.replace('charset="utf-8"></script>',"") for x in edit3}
#	edit5= {x.replace('<a',"") for x in edit4}
#	edit6= {x.replace('src="//embedr.flickr.com/assets/client-code.js"',"") for x in edit5}
	#edit2=[];
#adf
	#for i in edit1:
		#a= re.search('src=(.+?).jpg', edit1);
		#if a:
			#edit2.extend(a);



