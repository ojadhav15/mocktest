from urllib.parse import quote_plus

from django.shortcuts import render
from django.http import HttpResponse
from .forms import Csv_form
from .models import Csv_model
import csv
import pandas as pd
from sqlalchemy import create_engine, types
# Create your views here.
def Csv_view(r):

    form=Csv_form()

    if r.method=='POST':
        form=Csv_form(r.POST,r.FILES)
        #print(form)
        if form.is_valid():
            form.save()

            return HttpResponse('<h1>Successfully file uploded<h1>')

    return render(r,'csv_app/upload_csv.html',{'form':form})

def dump_csv(request):
    try:
        connection_str = "mysql+pymysql://root:%s@localhost:3306/restart_db" % quote_plus("sadhana@5366")
        #engine = create_engine("postgres://user:%s@host/database" % quote_plus("p@ss"))
        engine = create_engine(connection_str)  # enter your password and database names here

        df = pd.read_csv(r"C:\Users\DELL\PycharmProjects\new_restart\file_view_project\Upload_csv\employee_details.csv", sep=',', quotechar='\'',
                         encoding='utf8')  # Replace Excel_file_name with your excel sheet name
        column=[i.strip().replace(' ','_') for i in df.columns]
        df.columns=column
        df.to_sql('emp_table', con=engine, index=False,
                  if_exists='append')  # Replace Table_name with your sql table name
        return HttpResponse('<h1>Successfully file dump<h1>')
    except Exception as e:
        print(e)

    finally:
        engine.dispose()

#engine = create_engine('mysql://root:*Enter password here*@localhost/*Enter Databse name here*') # enter your password and database names here

#df = pd.read_csv("Excel_file_name.csv",sep=',',quotechar='\'',encoding='utf8') # Replace Excel_file_name with your excel sheet name
#df.to_sql('Table_name',con=engine,index=False,if_exists='append') # Replace Table_name with your sql table name




