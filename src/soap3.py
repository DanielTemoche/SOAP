from zeep import Client

cliente = Client(wsdl='https://cvnet.cpd.ua.es/servicioweb/publicos/pub_gestdocente.asmx?wsdl')
print(cliente.service.wsasidepto("C", "2012-12", "B142",""))