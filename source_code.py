import os
import numpy as np
import pandas as pd
from csv import writer 
from datetime import datetime as dt

os.chdir(r'E:\NM\Sem 3\gpa_project') # change the path with your's csv file stored dir

csds_semwise_subjects = {'sem1': ['Calculus', 'Programming for Problem Solving', 'Basic Electrical and Electronics Engineering','Engineering Graphics and Design',
                                 'Elements of Biology', 'English Communication', 'Professional Ethics','Constitution of India', 'Design Thinking'],
                        
                        'sem2': ['Linear Algebra and Differential Equations', 'Physics', 'Digital Circuits and Computer Architecture', 'Principles of Economics and Management', 
                                 'Python for data analysis', 'Environmental Science', 'Digital Manufacturing Laboratory', 'Electrical and Electronics Workshop', 'Critical Thinking'],
                       
                        'sem3': ['Optimization methods', 'Data Structures and Algorithms', 'Probability and Statistics', 'Data Wrangling', 'Discrete Mathematics',
                                 'Management Accounting for Engineers', 'Technical Communication', 'Community service'],
                        
                        'sem4': ['Machine learning', 'Introduction to Data, Signal, and Image Analysis', 'Statistical Methods', 'Database Management Systems', 'Web Programming',
                                 'Data handling and Visualization'],
                        
                        'sem5': ['Software Engineering', 'Mobile Application development', 'Computer Networks', 'Operating Systems', 'Department Elective I',
                                 'Open Elective I', 'Open Elective II'],
                        
                        'sem6': ['Applied Artificial Intelligence', 'Neural Networks and Deep Learning', 'Advance Data Structure for Analytics', 'Department Elective II',
                                 'Department Elective III', 'Open Elective III', 'Open Elective IV ', 'Interpersonal Skills'],
                        
                        'sem7': ['Cloud Computing', 'Big Data', 'Computer Vision', 'Department Elective IV', 'Department Elective V', 'Open Elective V', 'Capstone Project'],
                        
                        'sem8': ['Project']
                        }

csds_sem_sub_credits = {'sem1': [4,4,3,3,3,1,1,0,0,19], #format: [credits of no of subjs, total sem credit]
                        'sem2': [4,4,4,3,2,2,1,1,0,21],
                        'sem3': [4,4,3,3,3,2,1,0,20],
                        'sem4': [4,4,3,3,3,2,19],
                        'sem5': [3,3,3,3,3,3,3,21],
                        'sem6': [4,3,3,3,3,3,3,1,23],
                        'sem7': [4,3,3,3,3,3,3,22],
                        'sem8': [10,10] 
                        } 

csds_sem_subs_exam_type = {'sem1': [5,4], # format: [no of subjects having term end exam, no of sub only ica marks]
                        'sem2': [5,4],
                        'sem3': [6,2],
                        'sem4': [6,0],
                        'sem5': [7,0],
                        'sem6': [7,1],
                        'sem7': [6,1],
                        'sem8': [0,1] 
                        } 

grade_dict ={ 4:'A+', 3.75:'A', 3.5:'A-',
             3.25:'B+', 3:'B', 2.75:'B-',
             2.5:'C+', 2.25:'C', 2:'C-',
             1.5:'D', 0:'F'
             }

def get_sem():
    sem_num = int(input('\nEnter Semesters: '))
    sem='sem'+str(sem_num)
    
    if sem in csds_sem_subs_exam_type:
        tee_sub_count, ica_sub_count = csds_sem_subs_exam_type[sem]
        
    return sem, tee_sub_count, ica_sub_count 
    
def input_marks(sem, tee_sub_count, ica_sub_count):
    ICA , TEE = [], []
    
    print('\n* Note *')
    print('Enter Internal Continous Assignment Marks (ICA) out of 50')
    print('& Term End Examination Marks(TEE) out of 100: ')
        
    for i in range(0, tee_sub_count):
        print(f'\nMarks in {csds_semwise_subjects[sem][i]}:')
        
        while True:
            try:
                icaM = int(input('ICA: '))
                if icaM<0 or icaM>50:
                    print('Invalid input. Put ICA marks out of 50.')
                else:
                    ICA.append(icaM)
                    break
            except ValueError:
                print('Invalid input. Please enter valid marks.')
                
        while True:
            try:
                teeM = int(input('TEE: '))
                if teeM<0 or teeM>100:
                    print('Invalid input. Put TEE marks out of 100.')
                else:
                    TEE.append(teeM)
                    break
            except ValueError:
                print('Invalid input. Please enter valid marks.')
                
    for i in range(0, tee_sub_count):
        TEE[i]=TEE[i]/2
    for i in range(tee_sub_count, tee_sub_count+ica_sub_count):
        TEE.append(0) 
    
    for j in range(tee_sub_count, tee_sub_count+ica_sub_count):
        print(f'\nMarks in {csds_semwise_subjects[sem][j]}:')
        
        while True:
            try:
                icaM = int(input('ICA: '))
                if icaM<0 or icaM>50:
                    print('Invalid input. Put ICA marks out of 50.')
                else:
                    ICA.append(icaM)
                    break
            except ValueError:
                print('Invalid input. Please enter valid marks.')
                    
    for j in range(tee_sub_count, tee_sub_count+ica_sub_count):
        ICA[j]= ICA[j]*2
        
    return ICA, TEE

#  "round-half-to-even" rounding method 
def round_TM(x):
    if x >= 0:
        return int(x + 0.5)
    else:
        return int(x - 0.5)
    
def cal_total_marks(ica_m, tee_m, tee_sub_count, ica_sub_count):
    TotalM, Rounded_TotalM = [], []
    
    for k in range (tee_sub_count + ica_sub_count):
        TotalM.append(ica_m[k] + tee_m[k])
        
    for d in TotalM:
        D = round_TM(d) # Function call 
        Rounded_TotalM.append(D) 
        
    return Rounded_TotalM

def pass_fail(ica_m, tee_m, total_m, tee_sub_count, ica_sub_count):
    ICA_P_F, TEE_P_F, TM_P_F, final = [], [], [], []
    
    for i in range(tee_sub_count, tee_sub_count+ica_sub_count):
        tee_m[i]=22
        ica_m[i]= ica_m[i]/2
        
    for i in range(0, tee_sub_count+ica_sub_count):      
        if (ica_m[i] >= 20):
            ICA_P_F.append('Pass')
        elif (ica_m[i] < 20):
            ICA_P_F.append('Fail')
            
    for i in range(0,tee_sub_count+ica_sub_count):  
        if (tee_m[i] >= 20):
            TEE_P_F.append('Pass')
        elif (tee_m[i] < 20):
            TEE_P_F.append('Fail')
             
    for i in range(0,tee_sub_count+ica_sub_count): 
        if (total_m[i] >= 50):
            TM_P_F.append('Pass')
        elif (total_m[i] < 50):
            TM_P_F.append('Fail')
    
    for i in range(0,tee_sub_count+ica_sub_count):
        if (ICA_P_F[i] == 'Pass' and TEE_P_F[i]== 'Pass' and TM_P_F[i] == 'Pass'):
            final.append('Pass')
        else:
            final.append('Fail') 
    
    return ICA_P_F, TEE_P_F, TM_P_F, final

def grade_point(sub_FM, grades_scored): 
    if ( sub_FM>=85 and sub_FM<=100):
        grades_scored.append(4.00)
    elif ( sub_FM>=81 and sub_FM<=84.99 ):
        grades_scored.append(3.75)
    elif ( sub_FM>=77 and sub_FM<=80.99 ):
        grades_scored.append(3.50)
    elif ( sub_FM>=73 and sub_FM<=76.99 ):
        grades_scored.append(3.25)
    elif ( sub_FM>=69 and sub_FM<=72.99 ):
        grades_scored.append(3.00)
    elif ( sub_FM>=65 and sub_FM<=68.99 ):
        grades_scored.append(2.75)
    elif ( sub_FM>=61 and sub_FM<=64.99 ):
        grades_scored.append(2.50)
    elif ( sub_FM>=57 and sub_FM<=60.99 ):
        grades_scored.append(2.25)
    elif ( sub_FM>=50 and sub_FM<=56.99 ):
        grades_scored.append(2.00)
    elif ( sub_FM>=40 and sub_FM<=49.99 ):
        grades_scored.append(1.15)
    else:
        grades_scored.append(0)
        
def cal_gpa(total_m, tee_sub_count, ica_sub_count, sem):
    grades_scored = []
    for sub_FM in total_m:
        grade_point(sub_FM, grades_scored)
    
    sub_wise_grade_scored = [grade_dict[key] for key in grades_scored]
    
    if sem in csds_sem_sub_credits:
        sem_sub_credits, sem_total_credits = csds_sem_sub_credits[sem][:-1], csds_sem_sub_credits[sem][-1]
        
    credits_mul_grades = []
    for i in range(tee_sub_count + ica_sub_count):
        credits_mul_grades.append( sem_sub_credits[i] * grades_scored[i])
        
    sum=0
    for j in credits_mul_grades:
        sum += j
    
    gpa = sum / sem_total_credits
    
    return gpa, sub_wise_grade_scored

def comment(GPA):
    if (GPA > 4):
        print('!!! ErRoR !!!')
    elif (GPA >= 3.5 and GPA <= 4):
        print('>>> Hurray, you have done EXCELLENT')
    elif (GPA >= 3 and GPA <= 3.49 ):    
        print('>>> You have done GOOD, can IMPROVE')
    elif (GPA >= 2 and GPA<= 2.99):
        print('--- You can IMPROVE ---')
    else:
        print('--- You have to work HARDER ---')

def record_data():
    row = [current_date, current_time, sap_id, name, sem]
    
    for i in range(0, tee_sub_count):
        tee_m[i]=tee_m[i]*2
    for j in range(tee_sub_count, tee_sub_count+ica_sub_count):
        tee_m[j]=0
        
    for i in range(0, tee_sub_count):
        row.append(csds_semwise_subjects[sem][i])
        row.append(ica_m[i])
        row.append(ica_pass_fail[i])
        row.append(tee_m[i])
        row.append(tee_pass_fail[i])
        row.append(total_m[i])
        row.append(total_pass_fail[i])
        row.append(sub_wise_grade_scored[i])
        row.append(overall_pass_fail[i])
    
    for i in range(tee_sub_count, tee_sub_count+ica_sub_count):
        row.append(csds_semwise_subjects[sem][i])
        row.append(ica_m[i])
        row.append(ica_pass_fail[i])
        row.append(sub_wise_grade_scored[i])
        row.append(ica_pass_fail[i]) # for overall pass fail
    
    row.append('SGPA: ')
    row.append(SGPA)
    
    remark = 'Fail' if any(i == 'Fail' for i in overall_pass_fail) else 'Pass'    
    row.append(remark)
    
    row.append('CGPA: ')
    row.append(CGPA) 
    
    with open('recorded_data.csv', 'a') as f_object: #change the csv file name with yours to record data
        writer(f_object).writerow(row)
        f_object.close()
        
    print('Recorded data successfully')

def display_set():
    # Set options to display all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
def display_reset():
    # Reset display options to their defaults
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.width')
    pd.reset_option('display.max_colwidth') 
    
def goal_matrix(sem, tee_sub_count):
    
    print(f'\nEnter ICA marks of {sem}: ')
    
    ica=[]
    for sub in csds_semwise_subjects[sem][0:tee_sub_count]:
        print(sub)
        while True:
            try:
                m = int(input('ICA: '))
                if m<0 or m>50:
                    print('Invalid input. Put ICA marks out of 50.')
                else:
                    ica.append(m)
                    print(end='\n')
                    break
            except ValueError:
                print('Invalid input. Please enter valid marks.')                
        
    tee_data = []
    low_marks = [85, 81, 77, 73, 69, 65, 61, 57, 50, 40, 0]
    
    for i in ica:
        for j in low_marks:
            tee = (j-i)*2
            tee_data.append(tee)
    
    modified_tee_data = [max(0, value) for value in tee_data]   
    modified_tee_data = ['-' if value > 100 else value for value in modified_tee_data]
    reshaped_tee_data = np.array(modified_tee_data).reshape(-1,  len(grade_dict))
    
    df = pd.DataFrame(reshaped_tee_data)
    df.index=csds_semwise_subjects[sem][0:tee_sub_count]
    df.columns=grade_dict.values()
    
    print('Goal Matrix:') 
    print('Shows the minimum marks required to get respective column grade', end='\n')  
    display_set()
    print(df)    
    display_reset() 

#--main--
print('* '*20+str(' STME PyGPA Analyzer ')+' *'*22)

name = input('Enter Name: ')
sap_id = int(input('Enter SAP ID: '))

current_datetime = dt.today()
current_date = current_datetime.date()
current_time = current_datetime.time()

print(f'\nWelcome, {name}')
print('Enter 1: TEE marks recomendation -- Goal Matrix')
print('Enter 2: Calculate GPA')
select = int(input('-> '))

if select == 1:

    sem, tee_sub_count, ica_sub_count  = get_sem()
    
    goal_matrix(sem, tee_sub_count)
        
elif select == 2:

    sem, tee_sub_count, ica_sub_count = get_sem()
    
    if sem != 'sem1':
        pre_cgpa = float(input('\nEnter current CGPA: '))

    ica_m, tee_m = input_marks(sem, tee_sub_count, ica_sub_count)
    
    total_m = cal_total_marks(ica_m, tee_m, tee_sub_count, ica_sub_count)
        
    ica_pass_fail , tee_pass_fail, total_pass_fail, overall_pass_fail = pass_fail(ica_m, tee_m, total_m, tee_sub_count, ica_sub_count)    
    
    SGPA, sub_wise_grade_scored = cal_gpa(total_m, tee_sub_count, ica_sub_count, sem)
    SGPA = round(SGPA, 2)
    print('\n==> SGPA:', SGPA)
    comment(SGPA)
    
    if sem == 'sem1':
        pre_cgpa = SGPA
        
    CGPA = (pre_cgpa + SGPA) / 2
    print('\n==> CGPA:', round(CGPA, 2))
    
    print('\nEnter 1: Save data')
    print('Enter 0: Do not Save data')
    select2 = int(input('-> '))
    if select2 == 1:
        record_data() 