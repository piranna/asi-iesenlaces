import xmlrpclib

s = xmlrpclib.ServerProxy("http://localhost:8080/xmlrpc/")

print s.suma(10, 15)
print s.mayusculas('hola')


