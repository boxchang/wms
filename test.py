from suds import client

url = "http://10.96.101.136/jwsdata/services/Data?wsdl"

# 访问url地址返回一个client对象
web_s = client.Client(url)
print(web_s)
params = web_s.factory.create("ns2:JobRecordV02")
params.lift = 1
params.accessPoint = 1    #1:一樓   2:二樓
params.shelf = "02"  # 01;02;03
params.job = '1000727161'
print(params)
res = web_s.service.sendJobBufferV02(params)
print(res)