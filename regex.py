import re
#phone = "2004-959-559 # This is Phone Number"
phone="<sip_ip_address>255.255.255.256</sip_ip_address>"
port="<sip_port>5060</sip_port>"

# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print "Phone Num : ", num
#
# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)
# print "Phone Num : ", num

#My_Code
#num=re.sub(r'\D',"",phone)
#num=re.sub(r'#.*',"",phone)
#num=re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',"",phone)
ip_num=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',phone)
#print(ip_num.group())
port_num=re.search(r'\d{1,4}',port)
#print(port_num.group())
dic1={"sip_ip_address":ip_num.group(),"sip_port":port_num.group()}
for k,v in dic1.items():
    print(k , dic1[k])
