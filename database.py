import mysql.connector
import pandas as pd
import pyodbc
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

'''
Creating tables in the database
'''

class Db:

    '''
    Connecting to the database
    '''
    def config():
        con = mysql.connector.connect(user='root', password='Brightpoint@12', host='127.0.0.1', database='resume_parsing')
        cursor = con.cursor()
        return con, cursor

    '''
    Creating Personal details tables
    '''
    def personal_details_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table personal_details (first_name varchar(100), last_name varchar(100), 
        middle_name varchar(100), email_id1 varchar(500), email_id2 varchar(500), phn_num1 varchar(50), 
        phn_num2 varchar(50), person_add varchar(500), git_link varchar(500), linkedIn_link varchar(500), 
        total_exp varchar(500)) ''')

        # cursor.execute('''ALTER TABLE vendor_master AUTO_INCREMENT=6000001''')
        conn.commit()

    '''
    Creating education tables
    '''
    def education_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table education (degree1 varchar(50), inst_name1 varchar(70), 
        join_year1 varchar(10), pass_year1 varchar(10), edu_percentage1 varchar(20), 
        edu_location1 varchar(30), degree2 varchar(50), inst_name2 varchar(70), 
        join_year2 varchar(10), pass_year2 varchar(10), edu_percentage2 varchar(50), 
        edu_location2 varchar(500), degree3 varchar(200), inst_name3 varchar(500), 
        join_year3 varchar(70), pass_year3 varchar(70), edu_percentage3 varchar(50), 
        edu_location3 varchar(500), degree4 varchar(200), inst_name4 varchar(500), 
        join_year4 varchar(70), pass_year4 varchar(70), edu_percentage4 varchar(50), 
        edu_location4 varchar(500), degree5 varchar(200), inst_name5 varchar(500), 
        join_year5 varchar(70), pass_year5 varchar(70), edu_percentage5 varchar(50), 
        edu_location5 varchar(500), degree6 varchar(200), inst_name6 varchar(500), 
        join_year6 varchar(70), pass_year6 varchar(70), edu_percentage6 varchar(50), 
        edu_location6 varchar(500)) ''')
        
        # cursor.execute('''ALTER TABLE item_master AUTO_INCREMENT=1000001''')
        conn.commit()
    
    '''
    Creating work experience tables
    '''
    def work_experience_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table work_experience (organization_name1 varchar(100), experience1 varchar(10), 
        designation1 varchar(50), joining_date1 varchar(30), relieving_date1 varchar(30), 
        job_role1 text, job_location1 varchar(50), organization_name2 varchar(100), experience2 varchar(10), 
        designation2 varchar(50), joining_date2 varchar(30), relieving_date2 varchar(30), 
        job_role2 text, job_location2 varchar(50), organization_name3 varchar(100), experience3 varchar(10), 
        designation3 varchar(50), joining_date3 varchar(30), relieving_date3 varchar(30), 
        job_role3 text, job_location3 varchar(50), organization_name4 varchar(100), experience4 varchar(10), 
        designation4 varchar(50), joining_date4 varchar(30), relieving_date4 varchar(30), 
        job_role4 text, job_location4 varchar(50), organization_name5 varchar(100), experience5 varchar(10), 
        designation5 varchar(50), joining_date5 varchar(30), relieving_date5 varchar(30), 
        job_role5 text, job_location5 varchar(50), organization_name6 varchar(100), experience6 varchar(10), 
        designation6 varchar(50), joining_date6 varchar(30), relieving_date6 varchar(30), 
        job_role6 text, job_location6 varchar(50), organization_name7 varchar(100), experience7 varchar(10), 
        designation7 varchar(50), joining_date7 varchar(30), relieving_date7 varchar(30), 
        job_role7 text, job_location7 varchar(50), organization_name8 varchar(100), experience8 varchar(10), 
        designation8 varchar(50), joining_date8 varchar(30), relieving_date8 varchar(30), 
        job_role8 text, job_location8 varchar(50), organization_name9 varchar(100), experience9 varchar(10), 
        designation9 varchar(50), joining_date9 varchar(30), relieving_date9 varchar(30), 
        job_role9 text, job_location9 varchar(50), organization_name10 varchar(100), experience10 varchar(10), 
        designation10 varchar(50), joining_date10 varchar(30), relieving_date10 varchar(30), 
        job_role10 text, job_location10 varchar(50))''')
        
        # cursor.execute('''ALTER TABLE item_master AUTO_INCREMENT=1000001''')
        conn.commit()

    
    '''
    Creating other information tables
    '''
    def other_information_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table other_information (lang_name text, int_name text, 
        skill_name text) ''')
        
        # cursor.execute('''ALTER TABLE item_master AUTO_INCREMENT=1000001''')
        conn.commit()    

    '''
    Creating certifications tables
    '''
    def certifications_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table certifications (certification_name1 varchar(100), 
        certification_org1 varchar(100), certification_date1 varchar(50), certification_desp1 text, 
        certification_name2 varchar(100), certification_org2 varchar(100), certification_date2 varchar(50), 
        certification_desp2 text, certification_name3 varchar(100), certification_org3 varchar(100), 
        certification_date3 varchar(50), certification_desp3 text, certification_name4 varchar(100), 
        certification_org4 varchar(100), certification_date4 varchar(50), certification_desp4 text, 
        certification_name5 varchar(100), certification_org5 varchar(100), certification_date5 varchar(50), 
        certification_desp5 text, certification_name6 varchar(100), certification_org6 varchar(100), 
        certification_date6 varchar(50), certification_desp6 text, certification_name7 varchar(100), 
        certification_org7 varchar(100), certification_date7 varchar(50), certification_desp7 text, 
        certification_name8 varchar(100), certification_org8 varchar(100), certification_date8 varchar(50), 
        certification_desp8 text, certification_name9 varchar(100), certification_org9 varchar(100), 
        certification_date9 varchar(50), certification_desp9 text, certification_name10 varchar(100), 
        certification_org10 varchar(100), certification_date10 varchar(50), certification_desp10 text) ''')
        
        # cursor.execute('''ALTER TABLE item_master AUTO_INCREMENT=1000001''')
        conn.commit()

    '''
    Creating projects tables
    '''
    def projects_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table projects (project_title1 varchar(150), proj_desc1 text, 
        start_at1 varchar(50), ended_on1 varchar(50), proj_role1 text, project_title2 varchar(150), 
        proj_desc2 text, start_at2 varchar(50), ended_on2 varchar(50), proj_role2 text, 
        project_title3 varchar(150), proj_desc3 text, start_at3 varchar(50), ended_on3 varchar(50), 
        proj_role3 text, project_title4 varchar(150), proj_desc4 text, start_at4 varchar(50), 
        ended_on4 varchar(50), proj_role4 text, project_title5 varchar(150), proj_desc5 text, 
        start_at5 varchar(50), ended_on5 varchar(50), proj_role5 text, project_title6 varchar(150), 
        proj_desc6 text, start_at6 varchar(50), ended_on6 varchar(50), proj_role6 text, 
        project_title7 varchar(150), proj_desc7 text, start_at7 varchar(50), ended_on7 varchar(50), 
        proj_role7 text, project_title8 varchar(150), proj_desc8 text, start_at8 varchar(50), 
        ended_on8 varchar(50), proj_role8 text, project_title9 varchar(150), proj_desc9 text, 
        start_at9 varchar(50), ended_on9 varchar(50), proj_role9 text, project_title10 varchar(150), 
        proj_desc10 text, start_at10 varchar(50), ended_on10 varchar(50), proj_role10 text) ''')
        
        # cursor.execute('''ALTER TABLE item_master AUTO_INCREMENT=1000001''')
        conn.commit()

    '''
    Inserting personal details details to the personal details table
    '''
    def personal_details_table_insert(data_frame):
        conn, cursor = Db.config()
        # Insert DataFrame to Table
        for row in data_frame.itertuples():
            res = cursor.execute('''INSERT INTO personal_details (first_name, last_name, middle_name,  email_id1, email_id2, 
                        phn_num1, phn_num2, person_add, git_link, linkedIn_link, total_exp)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                         (row.first_name, 
                         row.last_name, 
                         row.middle_name,
                         row.email_id1, 
                         row.email_id2, 
                         row.phn_num1,
                         row.phn_num2,  
                         row.person_add,
                         row.git_link, 
                         row.linkedIn_link, 
                         row.total_exp))
        conn.commit()

    '''
    Inserting personal details details to the personal details table
    '''
    def education_table_insert(data_frame):
        conn, cursor = Db.config()
        # Insert DataFrame to Table
        for row in data_frame.itertuples():
            res = cursor.execute('''INSERT INTO education (degree1, inst_name1, join_year1, pass_year1, 
                                edu_percentage1, edu_location1, degree2, inst_name2, join_year2, pass_year2, 
                                edu_percentage2, edu_location2, degree3, inst_name3, join_year3, pass_year3, 
                                edu_percentage3, edu_location3, degree4, inst_name4, join_year4, pass_year4, 
                                edu_percentage4, edu_location4, degree5, inst_name5, join_year5, pass_year5, 
                                edu_percentage5, edu_location5, degree6, inst_name6, join_year6, pass_year6, 
                                edu_percentage6, edu_location6)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                         %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                         (row.degree1, 
                         row.inst_name1, 
                         row.join_year1, 
                         row.pass_year1,
                         row.edu_percentage1, 
                         row.edu_location1,
                         row.degree2, 
                         row.inst_name2, 
                         row.join_year2, 
                         row.pass_year2,
                         row.edu_percentage2, 
                         row.edu_location2,
                         row.degree3, 
                         row.inst_name3, 
                         row.join_year3, 
                         row.pass_year3,
                         row.edu_percentage3, 
                         row.edu_location3,
                         row.degree4, 
                         row.inst_name4, 
                         row.join_year4, 
                         row.pass_year4,
                         row.edu_percentage4, 
                         row.edu_location4,
                         row.degree5, 
                         row.inst_name5, 
                         row.join_year5, 
                         row.pass_year5,
                         row.edu_percentage5, 
                         row.edu_location5,
                         row.degree6, 
                         row.inst_name6, 
                         row.join_year6, 
                         row.pass_year6,
                         row.edu_percentage6, 
                         row.edu_location6)) 
        conn.commit()

    '''
    Inserting work experience to the work experience table
    '''
    def work_experience_table_insert(data_frame):
        conn, cursor = Db.config()
        # Insert item_master data to Table
        for row in data_frame.itertuples():
            cursor.execute('''INSERT INTO work_experience (organization_name1, experience1, designation1, joining_date1, relieving_date1, job_role1, job_location1,
                                organization_name2, experience2, designation2, joining_date2, relieving_date2, job_role2, job_location2, 
                                organization_name3, experience3, designation3, joining_date3, relieving_date3, job_role3, job_location3, 
                                organization_name4, experience4, designation4, joining_date4, relieving_date4, job_role4, job_location4, 
                                organization_name5, experience5, designation5, joining_date5, relieving_date5, job_role5, job_location5, 
                                organization_name6, experience6, designation6, joining_date6, relieving_date6, job_role6, job_location6, 
                                organization_name7, experience7, designation7, joining_date7, relieving_date7, job_role7, job_location7, 
                                organization_name8, experience8, designation8, joining_date8, relieving_date8, job_role8, job_location8, 
                                organization_name9, experience9, designation9, joining_date9, relieving_date9, job_role9, job_location9, 
                                organization_name10, experience10, designation10, joining_date10, relieving_date10, job_role10, job_location10)
                                VALUES (
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                                (row.organization_name1,
                                row.experience1, 
                                row.designation1, 
                                row.joining_date1, 
                                row.relieving_date1,
                                row.job_role1,
                                row.job_location1,
                                row.organization_name2, 
                                row.experience2, 
                                row.designation2, 
                                row.joining_date2, 
                                row.relieving_date2,
                                row.job_role2,
                                row.job_location2,
                                row.organization_name3, 
                                row.experience3, 
                                row.designation3, 
                                row.joining_date3, 
                                row.relieving_date3,
                                row.job_role3,
                                row.job_location3,
                                row.organization_name4, 
                                row.experience4, 
                                row.designation4, 
                                row.joining_date4, 
                                row.relieving_date4,
                                row.job_role4,
                                row.job_location4,
                                row.organization_name5, 
                                row.experience5, 
                                row.designation5, 
                                row.joining_date5, 
                                row.relieving_date5,
                                row.job_role5,
                                row.job_location5,
                                row.organization_name6, 
                                row.experience6, 
                                row.designation6, 
                                row.joining_date6, 
                                row.relieving_date6,
                                row.job_role6,
                                row.job_location6,
                                row.organization_name7, 
                                row.experience7, 
                                row.designation7, 
                                row.joining_date7, 
                                row.relieving_date7,
                                row.job_role7,
                                row.job_location7,
                                row.organization_name8, 
                                row.experience8, 
                                row.designation8, 
                                row.joining_date8, 
                                row.relieving_date8,
                                row.job_role8,
                                row.job_location8,
                                row.organization_name9, 
                                row.experience9, 
                                row.designation9, 
                                row.joining_date9, 
                                row.relieving_date9,
                                row.job_role9,
                                row.job_location9,
                                row.organization_name10, 
                                row.experience10, 
                                row.designation10, 
                                row.joining_date10, 
                                row.relieving_date10,
                                row.job_role10,
                                row.job_location10))    
        conn.commit()

    '''
    Inserting other information to the other information table
    '''
    def other_information_insert(data_frame):
        conn, cursor = Db.config()
        # Insert item_master data to Table
        for row in data_frame.itertuples():
                cursor.execute('''INSERT INTO other_information (lang_name, int_name, skill_name)
                       VALUES (%s,%s,%s)''',
                       (row.lang_name, 
                       row.int_name, 
                       row.skills_name))    
        conn.commit()

    '''
    Inserting customer details to the customer table
    '''
    def certifications_insert(data_frame):
        conn, cursor = Db.config()
        # Insert item_master data to Table
        for row in data_frame.itertuples():
            cursor.execute('''INSERT INTO certifications (certification_name1, certification_org1, 
            certification_date1, certification_desp1, certification_name2, certification_org2, 
            certification_date2, certification_desp2, certification_name3, certification_org3, 
            certification_date3, certification_desp3, certification_name4, certification_org4, 
            certification_date4, certification_desp4, certification_name5, certification_org5, 
            certification_date5, certification_desp5, certification_name6, certification_org6, 
            certification_date6, certification_desp6, certification_name7, certification_org7, 
            certification_date7, certification_desp7, certification_name8, certification_org8, 
            certification_date8, certification_desp8, certification_name9, certification_org9, 
            certification_date9, certification_desp9, certification_name10, certification_org10, 
            certification_date10, certification_desp10)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                    (row.certification_name1, 
                    row.certification_org1, 
                    row.certification_date1, 
                    row.certification_desp1,
                    row.certification_name2, 
                    row.certification_org2, 
                    row.certification_date2, 
                    row.certification_desp2,
                    row.certification_name3, 
                    row.certification_org3, 
                    row.certification_date3, 
                    row.certification_desp3,
                    row.certification_name4, 
                    row.certification_org4, 
                    row.certification_date4, 
                    row.certification_desp4,
                    row.certification_name5, 
                    row.certification_org5, 
                    row.certification_date5, 
                    row.certification_desp5,
                    row.certification_name6, 
                    row.certification_org6, 
                    row.certification_date6, 
                    row.certification_desp6,
                    row.certification_name7, 
                    row.certification_org7, 
                    row.certification_date7, 
                    row.certification_desp7,
                    row.certification_name8, 
                    row.certification_org8, 
                    row.certification_date8, 
                    row.certification_desp8,
                    row.certification_name9, 
                    row.certification_org9, 
                    row.certification_date9, 
                    row.certification_desp9,
                    row.certification_name10, 
                    row.certification_org10, 
                    row.certification_date10, 
                    row.certification_desp10))    
        conn.commit()

    '''
    Inserting customer details to the customer table
    '''
    def projects_table_insert(data_frame):
        conn, cursor = Db.config()
        # Insert item_master data to Table
        for row in data_frame.itertuples():
            cursor.execute('''INSERT INTO projects (project_title1, proj_desc1, start_at1, 
            ended_on1, proj_role1, project_title2, proj_desc2, start_at2, 
            ended_on2, proj_role2, project_title3, proj_desc3, start_at3, 
            ended_on3, proj_role3, project_title4, proj_desc4, start_at4, 
            ended_on4, proj_role4, project_title5, proj_desc5, start_at5, 
            ended_on5, proj_role5, project_title6, proj_desc6, start_at6, 
            ended_on6, proj_role6, project_title7, proj_desc7, start_at7, 
            ended_on7, proj_role7, project_title8, proj_desc8, start_at8, 
            ended_on8, proj_role8, project_title9, proj_desc9, start_at9, 
            ended_on9, proj_role9, project_title10, proj_desc10, start_at10, 
            ended_on10, proj_role10)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                    (row.project_title1, 
                    row.proj_desc1, 
                    row.start_at1, 
                    row.ended_on1, 
                    row.proj_role1,
                    row.project_title2, 
                    row.proj_desc2, 
                    row.start_at2, 
                    row.ended_on2, 
                    row.proj_role2,
                    row.project_title3, 
                    row.proj_desc3, 
                    row.start_at3, 
                    row.ended_on3, 
                    row.proj_role3,
                    row.project_title4, 
                    row.proj_desc4, 
                    row.start_at4, 
                    row.ended_on4, 
                    row.proj_role4,
                    row.project_title5, 
                    row.proj_desc5, 
                    row.start_at5, 
                    row.ended_on5, 
                    row.proj_role5,
                    row.project_title6, 
                    row.proj_desc6, 
                    row.start_at6, 
                    row.ended_on6, 
                    row.proj_role6,
                    row.project_title7, 
                    row.proj_desc7, 
                    row.start_at7, 
                    row.ended_on7, 
                    row.proj_role7,
                    row.project_title8, 
                    row.proj_desc8, 
                    row.start_at8, 
                    row.ended_on8, 
                    row.proj_role8,
                    row.project_title9, 
                    row.proj_desc9, 
                    row.start_at9, 
                    row.ended_on9, 
                    row.proj_role9,
                    row.project_title10, 
                    row.proj_desc10, 
                    row.start_at10, 
                    row.ended_on10, 
                    row.proj_role10))    
        conn.commit()

    '''
    Extracting personal details from the personal details table
    '''
    def personal_details_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM personal_details'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
    '''
    Extracting education details from the education table
    '''
    def education_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM education'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
    '''
    Extracting work experience details from the work experience table
    '''
    def work_experience_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM work_experience'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs

    '''
    Extracting languages, interests names, skills from the other information table
    '''
    def other_information_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM other_information'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
    '''
    Extracting certifications details from the certifications table
    '''
    def certifications_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM certifications'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
    '''
    Extracting projects details from the projects table
    '''
    def projects_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM projects'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
# Db.personal_details_table_create()
# Db.education_table_create()
# Db.work_experience_table_create()
# Db.other_information_table_create()
# Db.certifications_table_create()
# Db.projects_table_create()

