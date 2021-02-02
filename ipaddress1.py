import ipaddress
ip=ipaddress.ip_address(u'129.135.162.3')
print(ip.is_loopback)
print(ip.version)
ap=ipaddress.ip_address(u'::1')
print(ap.is_loopback)
print(ap.version)

mynet=ipaddress.ip_network('192.0.2.0/24')

print(mynet[3])
print(mynet[173])
for nodeip in mynet:
	print(nodeip)
	
print(ip in mynet)
print(ap in mynet)
	
print(mynet.netmask)



def isvalidip(ip):
	valid=False
	try:
	   ip = ipaddress.ip_address(ip)
	   valid = True
	except ValueError:
	   valid=False
	return valid

print(isvalidip("127.0.0.1"))
print(isvalidip("127.0.0.500"))