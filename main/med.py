import infermedica_api

from medget import medget
infermedica_api.configure(app_id='349a2f56', app_key='cca4f464530bc1b49433057c2470fd44')

request = medget()
request.get_data('male', 12)
request.add_symptoms([{'id':'s_21','status':'present'},{'id':'s_98','status':'present'},{'id':'s_107','status':'present'}, ]) 
a = request.get_question()
#print(a)
'''for i in a:
    print(i['choices'])
    print(i['id'])
    print(i['name']) 
'''
print(request.get_result())
