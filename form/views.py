from django.shortcuts import render
import joblib
import pandas as pd

# Create your views here.
reloadmodel=joblib.load('./models/trained_model.pkl')
def index(request):
	return render(request,'form_template.html',{'link':'http://127.0.0.1:8000/'})


def predict(request):
	if (request.method == 'POST'):
		tem={}
		tem['ApplicantIncome']=request.POST.get('ApplicantIncome')
		tem['CoapplicantIncome']=request.POST.get('CoapplicantIncome')
		tem['LoanAmount']=request.POST.get('LoanAmount')
		tem['Loan_Amount_Term']=request.POST.get('Loan_Amount_Term')
		tem['Gender']=request.POST.get('Gender')
		tem['Married']=request.POST.get('Married')
		tem['Dependents']=request.POST.get('Dependents')
		tem['Education']=request.POST.get('Education')
		tem['Self_Employed']=request.POST.get('Self_Employed')
		tem['Credit_History']=request.POST.get('Credit_History')
		tem['Property_Area']=request.POST.get('Property_Area')
	print(tem)
	obj_val=[tem['Gender'],tem['Married'],tem['Dependents'],tem['Education'],tem['Self_Employed'],tem['Property_Area'],tem['Credit_History']]
	list1=['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount','Loan_Amount_Term']
	list2=['Gender_0.0','Gender_1.0','Married_0.0','Married_1.0','Dependents_0.0','Dependents_1.0','Dependents_2.0','Dependents_3.0','Education_0.0','Education_1.0','Self_Employed_0.0','Self_Employed_1.0','Credit_History_0.0','Credit_History_1.0','Property_Area_0','Property_Area_1','Property_Area_2']
	tem_new={}
	for i in list1:
		tem_new[i]=tem[i]
	for i in list2:
		if(i in obj_val):
			tem_new[i]=1
		else:
			tem_new[i]=0
	print(tem_new)
	x1=pd.DataFrame({'a':tem_new}).transpose()
	approval=reloadmodel.predict(x1)[0]
	if (approval==1):
		msg='Congratulations!!,Your application for the loan has approved.'
	else:
		msg='Sorry!!,\nYour not eligeble for this loan.'

	context={'approval':msg,'link':'http://127.0.0.1:8000/'}
	return render(request,'result.html',context)