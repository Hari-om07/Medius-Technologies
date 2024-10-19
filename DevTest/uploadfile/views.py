from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings 
from .forms import uploadfile

def upload_file(request):
    if request.method == 'POST':
        form = uploadfile(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            #Process the type of the uploaded file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                return render(request,'upload/error.html',{'message': "Invalid file format. Only CSV and XLSX file is acceptable"})
            
            #generate a summary of file
            summary = df.describe().to_html(classes = 'summary-table', border = 0)

            #render the summary to result page
            return render(request, 'upload/result.html', {'summary':summary})
        
    else:
        form = uploadfile()

    return render(request, 'upload/upload.html', {'form':form})
