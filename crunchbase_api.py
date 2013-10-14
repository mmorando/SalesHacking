mitch 


import json, urllib
key = 'not_gonna_show_you_my_key'



url = 'http://api.crunchbase.com/v/1/search.js?query=advertising'
response = urllib.urlopen(url).read()
result = json.loads(response)


for r in result:
    print r


for r in result['results']:
    print r

company = result['results'][0]
name = company['name']



qry_url = 'http://api.crunchbase.com/v/1/company/%s.js?key=%s' % (urllib.quote(name), key)
qry_response = urllib.urlopen(qry_url).read()
qry_result = json.loads(response)


qry_result['email_address']
qry_result['blog_url']
qry_result['phone_number']


my_results = []
for r in result['results']:
    sales_data = {}
    name = r['name']
    qry_url = 'http://api.crunchbase.com/v/1/company/%s.js?key=%s' % (urllib.quote(name), key)
    qry_response = urllib.urlopen(qry_url).read()
    qry_result = json.loads(qry_response)
    sales_data['email'] = qry_result['email_address']
    sales_data['blog'] = qry_result['blog_url']
    sales_data['phone'] = qry_result['phone_number']
    my_results.append(sales_data)
    



for r in result['results']:
    sales_data = {}
    name = r['name']
    print "Running", name
    qry_url = 'http://api.crunchbase.com/v/1/company/%s.js?key=%s' % (urllib.quote(name), key)
    qry_response = urllib.urlopen(qry_url).read()
    qry_result = json.loads(qry_response)
    sales_data['company'] = name
    if qry_result.has_key('email_address'): 
        sales_data['email'] = qry_result['email_address']
    if qry_result.has_key('blog_url'):
        sales_data['blog'] = qry_result['blog_url']
    if qry_result.has_key('phone_number'):
        sales_data['phone'] = qry_result['phone_number']
    my_results.append(sales_data)