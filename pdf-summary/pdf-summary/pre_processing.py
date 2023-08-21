from seaplane import task 
import requests
from PyPDF2 import PdfReader
import os
import json 

@task(type='compute', id='pre-processing')
def pre_processing(data):
        # get the URL from the request 
        url = data['url']
        
        # download PDF 
        response = requests.get(url, allow_redirects=True)
        if response.status_code == 200:
            with open("my_pdf.pdf", 'wb') as file:
                file.write(response.content)
        else:
            print('Failed to download PDF.')

        # place holder to save PDF text
        pdf_text = ""

        # extract text
        count = 0
        reader = PdfReader('my_pdf.pdf')
        for page_number in range(len(reader.pages)):
            if count == 3:
                break
            page = reader.pages[page_number]
            page_content = page.extract_text()
            pdf_text += page_content
            count+=1

        # delete PDF
        os.remove('my_pdf.pdf')

        # construct prompt
        prompt = "write a summary of the following text. Make sure to maintain the scientific tone in the paper:  " + pdf_text
            
        # pass the required information to the next step
        return{
                'url' : str(url),
                'prompt' : prompt
                }