import re
input_file_name = 'input_file.txt'
output_file_name = 'my_output_file.txt'
input_file_handle = open(input_file_name, 'r')
output_file_handle = open(output_file_name, 'w')
#filename= input("Text filename:");
with open(input_file_name)as f:
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
	edit1= re.sub(r'\</a.*?\ipt','',edit1)
	#edit1= re.sub(r'\le<.*?\img','',edit1)
#	edit1= re.sub(r'\t.*?g','',edit1,flags=re.DOTALL)
	edit1= edit1.split('\n');
	edit1= [s[4:] for s in edit1]
	edit1= edit1[:69]
	count=0
	def print_output(s):
		#height= re.search('height="(.*)"',s)
		#print(height)
		output_file_handle.write ("\n")
		output_file_handle.write ("<p>" + str(edit1.index(s)+1)+".")
		output_file_handle.write ("\n")
		output_file_handle.write ("<br><img "+s) 
		output_file_handle.write ("\n")

	for s in edit1:
		print_output(s);
	#	count = count + 1
#	edit2= edit1.replace('"data-flickr-embed="true"',"") 
#	edit3= {x.replace("async","") for x in edit2}
#	edit4= {x.replace('charset="utf-8"></script>',"") for x in edit3}
#	edit5= {x.replace('<a',"") for x in edit4}
#	edit6= {x.replace('src="//embedr.flickr.com/assets/client-code.js"',"") for x in edit5}
	#edit2=[];

	#for i in edit1:
		#a= re.search('src=(.+?).jpg', edit1);
		#if a:
			#edit2.extend(a);



#input_file_name = 'input_file.txt'
#output_file_name = 'austin_output_file.txt'
#input_file_handle = open(filename, 'r')
#output_file_handle = open(filename, 'w')
