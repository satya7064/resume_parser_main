import easyocr

easyreader= easyocr.Reader(['en'],gpu=False,detector=True)
import numpy as np
import pandas as pd
import PIL
#from IPython.display import display,Image
from haystack import Document, Pipeline
from haystack.nodes import FARMReader
from haystack.utils import print_answers
from pdf2image import convert_from_path
from PIL import ImageDraw, Image
import os
import os.path
import json
import database

def extraction(file):
     file_name = os.path.splitext(os.path.basename(file))[0]
     new_reader = FARMReader(model_name_or_path=r"C:\Users\Satya prasad Mohanty\Downloads\Resume_parsing_fourty_ep\Resume_parsing_06122022\my_model_27032023")
     # new_reader = FARMReader(model_name_or_path=r"my_model4")
     images = convert_from_path(file, poppler_path="C:/Program Files (x86)/poppler-0.68.0/bin")
     for i in range(len(images)):
          # Save pages as images in the pdf
          images[i].save('./fileDir/page'+ str(i) +'.jpeg', 'JPEG')
          # images[i].save('./Resume_parsing_06122022/fileDir/page'+ str(i) +'.jpeg', 'JPEG')
     def draw_boxes(image,bounds,color='yellow',width=2):
          draw=ImageDraw.Draw(image)
          for bound in bounds:
               p0,p1,p2,p3=bound[0]
               draw.line([*p0,*p1,*p2,*p3,*p0], fill=color,width=width)
          return image
     path = './fileDir/'
     # path = './Resume_parsing_06122022/fileDir/'
     fileList = os.listdir(path)
     context=''
     print(" ")
     print("No.of pages found:", len(fileList))
     print(" ")
     print("Saving pages as images:")
     for i in fileList:
          imge_file = os.path.join('./fileDir/'+ i)
          # imge_file = os.path.join('./Resume_parsing_06122022/fileDir/'+ i)
          print(imge_file)
          img = Image.open(imge_file)
          im = np.array(img)
          bounds = easyreader.readtext(im, min_size=0, slope_ths=0.2, ycenter_ths=0.5,height_ths=0.5,y_ths=0.3,low_text=0.5,text_threshold=0.7,width_ths=0.8,paragraph=True,decoder='beamsearch', beamWidth=10)
          draw_boxes(img,bounds)
          for i in range(len(bounds)):
               context=context+bounds[i][1]+'\n'
     print(" ")
     print("Extracting text from images")
     print(" ")
     print(context)
     print(" ")
     print("Running model on text")
     print(" ")

     threshold_medium = 0.5 # earlier value 0.6
     threshold_high = 0.7
     threshold_low = 0.4  # earlier value 0.5

     # reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")
     p = Pipeline()
     p.add_node(component=new_reader, name="reader", inputs=["Query"])
     first_name = p.run(query="first_name", documents=[Document(content=context)])
     last_name = p.run(query="last_name", documents=[Document(content=context)])
     middle_name = p.run(query="middle_name", documents=[Document(content=context)])
     email_id1= p.run(query="email_id1", documents=[Document(content=context)])
     email_id2= p.run(query="email_id2", documents=[Document(content=context)])
     phone_number1 = p.run(query="phone_number1", documents=[Document(content=context)])
     phone_number2 = p.run(query="phone_number2", documents=[Document(content=context)])
     # phn_num3 = p.run(query="phone_number3", documents=[Document(content=context)])
     person_address = p.run(query="person_address", documents=[Document(content=context)])
     git_link = p.run(query="git_link", documents=[Document(content=context)])
     linkedIn_link = p.run(query="linkedIn_link", documents=[Document(content=context)])
     total_experience = p.run(query="total_experience", documents=[Document(content=context)])

     myData={}
     if ((first_name['answers'][0].score >= threshold_medium) and (first_name['answers'][0].score <= 1) ):
          myData[first_name.get('query')]=first_name['answers'][0].answer
     else:
          myData['first_name'] = '-'
     if ((last_name['answers'][0].score >= threshold_medium) and (last_name['answers'][0].score <= 1) ):
          myData[last_name.get('query')]=last_name['answers'][0].answer
     else:
          myData['last_name'] = '-'
     if ((middle_name['answers'][0].score >= threshold_medium) and (middle_name['answers'][0].score <= 1) ):
          myData[middle_name.get('query')]=middle_name['answers'][0].answer
     else:
          myData['middle_name'] = '-'
     if ((email_id1['answers'][0].score >= threshold_high) and (email_id1['answers'][0].score <= 1) ):
          myData[email_id1.get('query')]=email_id1['answers'][0].answer
     else:
          myData['email_id1'] = '-'
     if ((email_id2['answers'][0].score >= threshold_high) and (email_id2['answers'][0].score <= 1) ):
          myData[email_id2.get('query')]=email_id2['answers'][0].answer
     else:
          myData['email_id2'] = '-'
     if ((phone_number1['answers'][0].score >= threshold_high) and (phone_number1['answers'][0].score <= 1) ):
          myData[phone_number1.get('query')]=phone_number1['answers'][0].answer
     else:
          myData['phone_number1'] = '-'
     if ((phone_number2['answers'][0].score >= threshold_high) and (phone_number2['answers'][0].score <= 1) ):
          myData[phone_number2.get('query')]=phone_number2['answers'][0].answer
     else:
          myData['phone_number2'] = '-'
     if ((person_address['answers'][0].score >= threshold_high) and (person_address['answers'][0].score <= 1) ):
          myData[person_address.get('query')]=person_address['answers'][0].answer
     else:
          myData['person_address'] = '-'
     if ((git_link['answers'][0].score >= threshold_high) and (git_link['answers'][0].score <= 1) ):
          myData[git_link.get('query')]=git_link['answers'][0].answer
     else:
          myData['git_link'] = '-'
     if ((linkedIn_link['answers'][0].score >= threshold_high) and (linkedIn_link['answers'][0].score <= 1) ):
          myData[linkedIn_link.get('query')]=linkedIn_link['answers'][0].answer
     else:
          myData['linkedIn_link'] = '-'
     if ((total_experience['answers'][0].score >= threshold_high) and (total_experience['answers'][0].score <= 1) ):
          myData[total_experience.get('query')]=total_experience['answers'][0].answer
     else:
          myData['total_experience'] = '-'
     
     '''
     Checking amount is present or not,
     if amount is present check description, order quantity and net price
     otherwise terminate
     '''
     data1={}
     for i in range(1,6):
          no_of_degrees = i    
          x = str(i)
          degree = p.run(query="degree"+x, documents=[Document(content=context)])
          if ((degree['answers'][0].score >= threshold_high) and (degree['answers'][0].score <= 1) and degree['answers'][0].answer is not None):
               data1[degree.get('query')]=degree['answers'][0].answer

               institution_name = p.run(query="institution_name"+x, documents=[Document(content=context)])
               joining_year = p.run(query="joining_year"+x, documents=[Document(content=context)])
               passing_year = p.run(query="passing_year"+x, documents=[Document(content=context)])
               education_percentage = p.run(query="education_percentage"+x, documents=[Document(content=context)])
               education_location = p.run(query="education_location"+x, documents=[Document(content=context)])

               
               if ((institution_name['answers'][0].score >= threshold_high) and (institution_name['answers'][0].score <= 1) ):
                    data1[institution_name.get('query')]=institution_name['answers'][0].answer
               else:
                    data1['institution_name'+x] = '-'
                    
               if ((joining_year['answers'][0].score >= threshold_high) and (joining_year['answers'][0].score <= 1) ):
                    data1[joining_year.get('query')]=joining_year['answers'][0].answer
               else:
                    data1['joining_year'+x] = '-'

               if ((passing_year['answers'][0].score >= threshold_medium) and (passing_year['answers'][0].score <= 1) ):
                    data1[passing_year.get('query')]=passing_year['answers'][0].answer
               else:
                    data1['passing_year'+x] = '-'

               if ((education_percentage['answers'][0].score >= threshold_high) and (education_percentage['answers'][0].score <= 1) ):
                    data1[education_percentage.get('query')]=education_percentage['answers'][0].answer
               else:
                    data1['education_percentage'+x] = '-'

               if ((education_location['answers'][0].score >= threshold_high) and (education_location['answers'][0].score <= 1) ):
                    data1[education_location.get('query')]=education_location['answers'][0].answer
               else:
                    data1['education_location'+x] = '-'

          else:
               no_of_degrees = i-1
               data1['no_of_degrees']=no_of_degrees
               break
          
     for i in range(1, 6):  # earlier value (1,10)
          no_of_organizations = i    
          x = str(i)
          organization_name = p.run(query="organization_name"+x, documents=[Document(content=context)])
          if ((organization_name['answers'][0].score >= threshold_medium) and (organization_name['answers'][0].score <= 1) and organization_name['answers'][0].answer is not None):
               data1[organization_name.get('query')]=organization_name['answers'][0].answer

               experience = p.run(query="experience"+x, documents=[Document(content=context)])
               designation = p.run(query="designation"+x, documents=[Document(content=context)])
               joining_date = p.run(query="joining_date"+x, documents=[Document(content=context)])
               relieving_date = p.run(query="relieving_date"+x, documents=[Document(content=context)])
               job_role = p.run(query="job_role"+x, documents=[Document(content=context)])
               job_location = p.run(query="job_location"+x, documents=[Document(content=context)])

               if ((experience['answers'][0].score >= threshold_medium) and (experience['answers'][0].score <= 1) ):
                    data1[experience.get('query')]=experience['answers'][0].answer
               else:
                    data1['experience'+x] = '-'
                    
               if ((designation['answers'][0].score >= threshold_medium) and (designation['answers'][0].score <= 1) ):
                    data1[designation.get('query')]=designation['answers'][0].answer
               else:
                    data1['designation'+x] = '-'

               if ((joining_date['answers'][0].score >= threshold_medium) and (joining_date['answers'][0].score <= 1) ):
                    data1[joining_date.get('query')]=joining_date['answers'][0].answer
               else:
                    data1['joining_date'+x] = '-'

               if ((relieving_date['answers'][0].score >= threshold_medium) and (relieving_date['answers'][0].score <= 1) ):
                    data1[relieving_date.get('query')]=relieving_date['answers'][0].answer
               else:
                    data1['relieving_date'+x] = '-'

               if ((job_role['answers'][0].score >= threshold_medium) and (job_role['answers'][0].score <= 1) ):
                    data1[job_role.get('query')]=job_role['answers'][0].answer
               else:
                    data1['job_role'+x] = '-'

               if ((job_location['answers'][0].score >= threshold_medium) and (job_location['answers'][0].score <= 1) ):
                    data1[job_location.get('query')]=job_location['answers'][0].answer
               else:
                    data1['job_location'+x] = '-'

          else:
               no_of_organizations = i-1
               data1['no_of_organizations']=no_of_organizations
               break
     
     for i in range(1, 6):  # earlier value (1,10)
          no_of_certfications = i    
          x = str(i)
          certification_name = p.run(query="certification_name"+x, documents=[Document(content=context)])
          if ((certification_name['answers'][0].score >= threshold_high) and (certification_name['answers'][0].score <= 1) and certification_name['answers'][0].answer is not None):
               data1[certification_name.get('query')]=certification_name['answers'][0].answer

               certification_organization = p.run(query="certification_organization"+x, documents=[Document(content=context)])
               certification_date = p.run(query="certification_date"+x, documents=[Document(content=context)])
               certification_desp = p.run(query="certification_desp"+x, documents=[Document(content=context)])
               if ((certification_organization['answers'][0].score >= threshold_high) and (certification_organization['answers'][0].score <= 1) ):
                    data1[certification_organization.get('query')]=certification_organization['answers'][0].answer
               else:
                    data1['certification_organization'+x] = '-'
                    
               if ((certification_date['answers'][0].score >= threshold_high) and (certification_date['answers'][0].score <= 1) ):
                    data1[certification_date.get('query')]=certification_date['answers'][0].answer
               else:
                    data1['certification_date'+x] = '-'

               if ((certification_desp['answers'][0].score >= threshold_high) and (certification_desp['answers'][0].score <= 1) ):
                    data1[certification_desp.get('query')]=certification_desp['answers'][0].answer
               else:
                    data1['certification_desp'+x] = '-'
          else:
               no_of_certfications = i-1
               data1['no_of_certfications']=no_of_certfications
               break

     for i in range(1,6):   # earlier value (1,10)
          no_of_projects = i    
          x = str(i)
          project_title = p.run(query="project_title"+x, documents=[Document(content=context)])
          if ((project_title['answers'][0].score >= threshold_high) and (project_title['answers'][0].score <= 1) and project_title['answers'][0].answer is not None):
               data1[project_title.get('query')]=project_title['answers'][0].answer

               project_description = p.run(query="project_description"+x, documents=[Document(content=context)])
               started_at = p.run(query="started_at"+x, documents=[Document(content=context)])
               Ended_on = p.run(query="Ended_on"+x, documents=[Document(content=context)])
               Project_role = p.run(query="Project_role"+x, documents=[Document(content=context)])
               
               if ((project_description['answers'][0].score >= threshold_medium) and (project_description['answers'][0].score <= 1) ):
                    data1[project_description.get('query')]=project_description['answers'][0].answer
               else:
                    data1['project_description'+x] = '-'
                    
               if ((started_at['answers'][0].score >= threshold_high) and (started_at['answers'][0].score <= 1) ):
                    data1[started_at.get('query')]=started_at['answers'][0].answer
               else:
                    data1['started_at'+x] = '-'

               if ((Ended_on['answers'][0].score >= threshold_high) and (Ended_on['answers'][0].score <= 1) ):
                    data1[Ended_on.get('query')]=Ended_on['answers'][0].answer
               else:
                    data1['Ended_on'+x] = '-'

               if ((Project_role['answers'][0].score >= threshold_medium) and (Project_role['answers'][0].score <= 1) ):
                    data1[Project_role.get('query')]=Project_role['answers'][0].answer
               else:
                    data1['Project_role'+x] = '-'
          else:
               no_of_projects = i-1
               data1['no_of_projects']=no_of_projects
               break

     language_name = p.run(query="language_name", documents=[Document(content=context)])
     interest_name = p.run(query="interest_name", documents=[Document(content=context)])
     skills_name = p.run(query="skills_name", documents=[Document(content=context)])
     data2={}
     if ((language_name['answers'][0].score >= threshold_high) and (language_name['answers'][0].score <= 1) ):
          data2[language_name.get('query')]=language_name['answers'][0].answer
     else:
          data2['language_name'] = '-'

     if ((interest_name['answers'][0].score >= threshold_high) and (interest_name['answers'][0].score <= 1) ):
          data2[interest_name.get('query')]=interest_name['answers'][0].answer
     else:
          data2['interest_name'] = '-'

     if ((skills_name['answers'][0].score >= threshold_medium) and (skills_name['answers'][0].score <= 1) ):
          data2[skills_name.get('query')]=skills_name['answers'][0].answer
     else:
          data2['skills_name'] = '-'
 
     myData.update(data1)
     myData.update(data2)
     for item in myData.items():
        print(item)
     path = './fileDir/'
     for file_name in os.listdir(path):
          file = path + file_name
          os.remove(file)

     df = pd.DataFrame(myData,index=[0])
     df=df.fillna(' ')
     f_name = "resume_output.json"
     save_file = open('./output_files/'+f_name, "w")  
     json.dump(myData, save_file, indent = 6)  
     save_file.close()
    
     return myData
def db_data(data):
      
     p_info={}
     # if data['first_name'] is None:
     #      p_info['first_name'] = '-'
     # else:
     p_info['first_name']=data['first_name']

     # if data['last_name'] is None:
     #      p_info['last_name'] = '-'
     # else:
     p_info['last_name']=data['last_name'] 

     # if data['middle_name'] is None:
     #      p_info['middle_name'] = '-'
     # else:
     p_info['middle_name']=data['middle_name']

     p_info['email_id1']=data['email_id1']

     # if data['email_id2'] is None:
     #      p_info['mail_id2'] = '-'
     # else:
     p_info['email_id2']=data['email_id2']

     # if data['phn_num1'] is None:
     #      p_info['phn_num1'] = '-'
     # else:
     p_info['phn_num1']=data['phone_number1']

     # if data['phn_num2'] is None:
     #      p_info['phn_num2'] = '-'
     # else:
     p_info['phn_num2']=data['phone_number2']
   
     # if data['per_add'] is None:
     #      p_info['person_add'] = '-'
     # else:
     p_info['person_add']=data['person_address']

     # if data['git_link'] is None:
     #      p_info['git_link'] = '-'
     # else:
     p_info['git_link']=data['git_link']

     # if data['linkedIn_link'] is None:
     #      p_info['linkedIn_link'] = '-'
     # else:
     p_info['linkedIn_link']=data['linkedIn_link']

     # if data['total_exp'] is None:
     #      p_info['total_exp'] = '-'
     # else:
     p_info['total_exp']=data['total_experience']

     edu_info={}
     z = int(data['no_of_degrees'])
     for y in range(1, z+1):
          a = str(y)
          edu_info['degree'+a]=data['degree'+a]
          edu_info['inst_name'+a]=data['institution_name'+a]
          edu_info['join_year'+a]=data['joining_year'+a]
          edu_info['pass_year'+a]=data['passing_year'+a] 
          edu_info['edu_percentage'+a]=data['education_percentage'+a]
          edu_info['edu_location'+a]=data['education_location'+a]

     for y in range(z+1, 11):
        a = str(y)
        edu_info['degree'+a]='-'
        edu_info['inst_name'+a]='-'
        edu_info['join_year'+a]='-'
        edu_info['pass_year'+a]='-'
        edu_info['edu_percentage'+a]='_'
        edu_info['edu_location'+a]='_'

     work_exp={}
     z = int(data['no_of_organizations'])
     for y in range(1, z+1):
          a = str(y)
          work_exp['organization_name'+a]=data['organization_name'+a]
          work_exp['experience'+a]=data['experience'+a]
          work_exp['designation'+a]=data['designation'+a]
          work_exp['joining_date'+a]=data['joining_date'+a] 
          work_exp['relieving_date'+a]=data['relieving_date'+a]
          work_exp['job_role'+a]=data['job_role'+a] 
          work_exp['job_location'+a]=data['job_location'+a] 

     for y in range(z+1, 11):
        a = str(y)
        work_exp['organization_name'+a]='-'
        work_exp['experience'+a]='-'
        work_exp['designation'+a]='-'
        work_exp['joining_date'+a]='-'
        work_exp['relieving_date'+a]='_'
        work_exp['job_role'+a]='_'
        work_exp['job_location'+a]='_'

     certif={}
     z = int(data['no_of_certfications'])
     for y in range(1, z+1):
          a = str(y)
          certif['certification_name'+a]=data['certification_name'+a]
          certif['certification_org'+a]=data['certification_organization'+a]
          certif['certification_date'+a]=data['certification_date'+a]
          certif['certification_desp'+a]=data['certification_desp'+a] 

     for y in range(z+1, 11):
        a = str(y)
        certif['certification_name'+a]='-'
        certif['certification_org'+a]='-'
        certif['certification_date'+a]='-'
        certif['certification_desp'+a]='-'

     project={}  
     z = int(data['no_of_projects'])
     for y in range(1, z+1):
          a = str(y)
          project['project_title'+a]=data['project_title'+a]
          project['proj_desc'+a]=data['project_description'+a]
          project['start_at'+a]=data['started_at'+a]
          project['ended_on'+a]=data['Ended_on'+a] 
          project['proj_role'+a]=data['project_role'+a] 

     for y in range(z+1, 11):
        a = str(y)
        project['project_title'+a]='-'
        project['proj_desc'+a]='-'
        project['start_at'+a]='-'
        project['ended_on'+a]='-'
        project['proj_role'+a]='_'  
     
     other_info={}

     # if data['language_name'] is None:
     #      other_info['lang_name'] = '-'
     # else:
     other_info['lang_name']=data['language_name']

     # if data['interest_name'] is None:
     #      other_info['int_name'] = '-'
     # else:
     other_info['int_name']=data['interest_name'] 

     # if data['skills_name'] is None:
     #      other_info['skills_name'] = '-'
     # else:
     other_info['skills_name']=data['skills_name']

     '''
     Storing the extracted details in particular tables
     '''

     df1 = pd.DataFrame(data=p_info, index=[0])
     # print('-------------')
     # print(df1)
     database.Db.personal_details_table_insert(df1)

     df2 = pd.DataFrame(data=edu_info, index=[0])
     # print('-------------')
     # print(df2)
     database.Db.education_table_insert(df2)

     df3 = pd.DataFrame(data=work_exp, index=[0])
     # print('-------------')
     # print(df3)
     database.Db.work_experience_table_insert(df3)

     df4 = pd.DataFrame(data=other_info, index=[0])
     # print('-------------')
     # print(df4)
     database.Db.other_information_insert(df4)

     df5 = pd.DataFrame(data=certif, index=[0])
     # print('-------------')
     # print(df5)
     database.Db.certifications_insert(df5)

     df6 = pd.DataFrame(data=project, index=[0])
     # print('-------------')
     # print(df6)
     database.Db.projects_table_insert(df6)
    


