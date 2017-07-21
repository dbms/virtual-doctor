from medget import medget

a = medget()

a.get_data('male', 21)
a.add_symptoms([{'id': 's_22', 'status': 'present'}])
k = a.get_question()
print k
print a.check_risk()
l = a.get_result()
print l
