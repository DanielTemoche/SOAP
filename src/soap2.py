from zeep import Client


cliente = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')

print(cliente.service.NumberToWords(48))
print(cliente.service.NumberToDollars(48))

