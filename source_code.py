import os
import numpy as np
import pandas as pd
from csv import writer
from datetime import datetime as dt
import matplotlib.pyplot as plt

os.chdir(r'E:\NM\Sem 3\gpa_project')

# initialising empty lists
ICA, TEE, TotalM, rounded_TM, gp_multiplied, credit_multiplied = [], [], [], [], [], [] 
ICA_P_F, TEE_P_F, TM_P_F, final = [], [], [], [] # P <- Pass, F <- Fail

# to calculate grade point student got by passing final marks scored in each subject
# and appending to an empty list 'gp_multiplied'
def grade_point(t): 
    if ( T>=85 and T<=100):
        gp_multiplied.append(4.00)
    elif ( T>=81 and T<=84.99 ):
        gp_multiplied.append(3.75)
    elif ( T>=77 and T<=80.99 ):
        gp_multiplied.append(3.50)
    elif ( T>=73 and T<=76.99 ):
        gp_multiplied.append(3.25)
    elif ( T>=69 and T<=72.99 ):
        gp_multiplied.append(3.00)
    elif ( T>=65 and T<=68.99 ):
        gp_multiplied.append(2.75)
    elif ( T>=61 and T<=64.99 ):
        gp_multiplied.append(2.50)
    elif ( T>=57 and T<=60.99 ):
        gp_multiplied.append(2.25)
    elif ( T>=50 and T<=56.99 ):
        gp_multiplied.append(2.00)
    elif ( T>=40 and T<=49.99 ):
        gp_multiplied.append(1.15)
    else:
        gp_multiplied.append(0) 
 
#  "round-half-to-even" rounding method 
def round_TM(x):
    if x >= 0:
        return int(x + 0.5)
    else:
        return int(x - 0.5)

def comment(gpa):
    if (gpa > 4):
        print('ErRoR')
    elif (gpa >= 3.5 and gpa <= 4):
        print('Hurray, you have done EXCELLENT')
    elif (gpa >= 3 and gpa <= 3.49 ):    
        print('You have done GOOD, can IMPROVE')
    elif (gpa >= 2 and gpa<= 2.99):
        print('You can IMPROVE')
    else:
        print('You have to work HARDER')
     
#!!! remove line no.147 to 174 and line no.274 to 298 and add a funtion() to reduce lines of code!!!
sum = 0

print('******* STME GPA CALCULATOR *******')

name = input('Enter Name: ')
sap_id = int(input('Enter SAP ID: '))
now=dt.now()

data = [now,name,sap_id] # to gather information and save in list (later CSV file) 

print('\nSelect any one')
print('1. Predict GPA')
print('2. Result Analysis (Data Visualization)')
#print('3. Prediction model')
op = int(input('action from above (int):')) # taking users input for above options 

if op==1:
    
    sm=int(input('\nSelect Semester (1. Sem1 || 2. Sem2): '))
    
    if sm==1:
        
        subject=['Calculus','Programming for Problem Solving',
                 'Basic Electrical and Electronics Engineering','Elements of Biology',
                 'Engineering Graphics and Design','English Communication',
                 ' Professional Ethics','Constitution of India',
                 'Design Thinking']
        sem1_subs_credit=[4,4,3,3,3,1,1,0,0]
        sem1_subs_credit_Total = 19
    
        print('\nNOTE: \nEnter Internal Continous Assignment Marks(ICA out of 50)')
        print(' & Term End Examination Marks(TEE out of 100): ')
        
        for i in range(0,5):
            print(f'\nMarks in {subject[i]}:')
            
            icaM = int(input('ICA: '))
            if 0 <= icaM <= 50:
                ICA.append(icaM) # storing ica marks in 'ICA' list
            else:
                print('Entered marks out of range\nEnter ICA in the range of 50')
                icaM = int(input('Valid ICA: '))
                if 0 <= icaM <= 50:
                    ICA.append(icaM) # storing the correct ICA marks in 'ICA' list
                else:
                    print('Invalid ICA marks')
                    
            teeM = int(input('TEE: '))
            if 0 <= teeM <= 100:       
                TEE.append(teeM)# storing term end marks in 'TEE' list
            else:
                print('Entered marks out of range\nEnter TEE in range of 100')
                teeM = int(input('TEE: '))
                if 0 <= teeM <= 100:       
                    TEE.append(teeM) # storing the correct term end marks in 'TEE' list
                else:
                    print('Invalid TEE marks')
                    
        for i in range(0,5):
            TEE[i]=TEE[i]/2
        for i in range(5,9):
            TEE.append(0) 
            
        for j in range(5,9):
            print(f'\nMarks in {subject[j]}:')
            icaM = int(input('ICA: '))
            if 0<= icaM <= 50:
                ICA.append(icaM)
            else:
                print('Entered marks out of range\nEnter ICA in the range of 50')
                icaM = int(input('ICA: '))
                if 0<= icaM <= 50:
                    ICA.append(icaM)
                else:
                    print('Invalid ICA marks')
                    
        for j in range(5,9):
            ICA[j]= ICA[j]*2
            
        for k in range(0,9):
            TotalM.append(ICA[k] + TEE[k])
            
        #round TM
        for d in TotalM:
            D = round_TM(d) # Function call 
            rounded_TM.append(D) 
        
        for l in range(0,9):
            data.append(rounded_TM[l]) # Storing marks in list 
        
        for i in range(5,9):
            TEE[i]=22
            ICA[i]= ICA[i]/2
            
        for i in range(0,9):      
            if (ICA[i] >= 20):
                ICA_P_F.append('P')
            elif (ICA[i] < 20):
                ICA_P_F.append('F')
                
        for i in range(0,9):  
            if (TEE[i] >= 20):
                TEE_P_F.append('P')
            elif (TEE[i] < 20):
                TEE_P_F.append('F')
                 
        for i in range(0,9): 
            if (TotalM[i] >= 50):
                TM_P_F.append('P')
            elif (TotalM[i] < 50):
                TM_P_F.append('F')
        
        for i in range(0,9):
            if (ICA_P_F[i] == 'P' and TEE_P_F[i]== 'P' and TM_P_F[i] == 'P'):
                final.append('Pass')
            else:
                final.append('Fail')
        
        dt = [final, ICA_P_F, TEE_P_F, TM_P_F]
        
        for T in rounded_TM:
            grade_point(T) #function call
              
        for c in range(0,9):
            credit_multiplied.append(sem1_subs_credit[c] * gp_multiplied[c])
                            
        for s in credit_multiplied:
            sum+=s
            
        gpa = sum / sem1_subs_credit_Total
        data.append(gpa) 
        
        for i in range(4):
            data.append(dt[i])
        
        with open('sem1_gpa.csv', 'a') as f_object:
            writer(f_object).writerow(data)
            f_object.close()
            
        print('\n`````````````````````')        
        print("GPA=",gpa)
        comment(gpa) 
            
    elif sm==2:
        subject=['Linear Algebra and Differential Equations',
                 'Physics','Digital Circuits and Computer Architecture',
                 'Principles of Economics and Management','Python for data analysis',
                 'Environmental Science','Digital Manufacturing Laboratory',
                 'Electrical and Electronics Workshop','Critical Thinking ']
        
        ICA, TEE, TotalM, gp_multiplied, credit_multiplied = [], [], [], [], []
        
        sem2_subs_credit=[4,4,4,3,2,2,1,1,0]
        sem2_subs_credit_Total = 21
    
        print('\nEnter Internal Continous Assignment Marks(ICA out of 50)')
        print(' & Term End Examination Marks(TEE out of 100): ')
        
        for i in range(0,5):
            print(f'\nMarks in {subject[i]}:')
            
            icaM = int(input('ICA: '))
            if 0 <= icaM <= 50:
                ICA.append(icaM)
            else:
                print('Entered marks out of range\nEnter ICA in the range of 50')
                icaM = int(input('Valid ICA: '))
                if 0 <= icaM <= 50:
                    ICA.append(icaM)
                else:
                    print('Invalid ICA marks')
                    
            teeM = int(input('TEE: '))
            if 0 <= teeM <= 100:       
                TEE.append(teeM)
            else:
                print('Entered marks out of range\nEnter TEE in the range of 100')
                teeM = int(input('TEE: '))
                if 0 <= teeM <= 100:       
                    TEE.append(teeM)
                else:
                    print('Invalid TEE marks')
                    
        for i in range(0,5):
            TEE[i]=TEE[i]/2
        for i in range(5,9):
            TEE.append(0)
            
        for j in range(5,9):
            print(f'\nMarks in {subject[j]}:')
            icaM = int(input('ICA: '))
            if 0<= icaM <= 50:
                ICA.append(icaM)
            else:
                print('Entered marks out of range\nEnter ICA in the range of 50')
                icaM = int(input('ICA: '))
                if 0<= icaM <= 50:
                    ICA.append(icaM)
                else:
                    print('Invalid ICA marks')
                    
        for j in range(5,9):
            ICA[j]= ICA[j]*2
            
        for k in range(0,9):
            TotalM.append(ICA[k] + TEE[k])
        #round TM
        for d in TotalM:
            D = round_TM(d) # Function call
            rounded_TM.append(D)
        
        for l in range(0,9):
            data.append(rounded_TM[l]) # Storing marks in File
        
        for i in range(5,9):
            TEE[i]=22
            ICA[i]= ICA[i]/2
            
        for i in range(0,9):      
            if (ICA[i] >= 20):
                ICA_P_F.append('P')
            elif (ICA[i] < 20):
                ICA_P_F.append('F')
                
        for i in range(0,9):  
            if (TEE[i] >= 20):
                TEE_P_F.append('P')
            elif (TEE[i] < 20):
                TEE_P_F.append('F')
                
        for i in range(0,9): 
            if (TotalM[i] >= 50):
                TM_P_F.append('P')
            elif (TotalM[i] < 50):
                TM_P_F.append('F')
        
        for i in range(0,9):
            if (ICA_P_F[i] == 'P' and TEE_P_F[i]== 'P' and TM_P_F[i] == 'P'):
                final.append('Pass')
            else:
                final.append('Fail')
        
        dt = [final, ICA_P_F, TEE_P_F, TM_P_F]
        
        for T in rounded_TM:
            grade_point(T) #function call

        for c in range(0,9):
            credit_multiplied.append(sem2_subs_credit[c] * gp_multiplied[c])
                            
        for s in credit_multiplied:
            sum+=s
            
        gpa = sum / sem2_subs_credit_Total
        data.append(gpa)
        
        for i in range(4):
            data.append(dt[i])
            
        with open('sem2_gpa.csv', 'a') as f_object:
            writer(f_object).writerow(data)
            f_object.close()
            
        print('\n`````````````````````')
        print("GPA=",gpa)
        comment(gpa)

if op ==2:
    sm=int(input('\nSelect Semester (1. Sem1 || 2. Sem2): '))
   
    # Set options to display all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    if sm==1:
        dt = pd.read_csv('sem1_gpa.csv')
        subject=['CALCULUS','C++','BEEE','BIOLOGY','EGD','ENGLISH',
                 'ETHICS','CONSTITUTION','DESIGN THINKING']
        
    elif sm==2:
        dt = pd.read_csv('sem2_gpa.csv')
        subject=['LADE','Physics','DCCA','PEM','Python',
                 'EVS','DML','EEWS','Critical Thinking ']
        
    print(f'\nData of Registered students (SEM {sm}): ')
    columns_drop = ['ICA_Pass_Fail','TEE_Pass_Fail','TotalM_Pass_Fail']
    dt.drop(columns_drop, axis=1, inplace=True)
    print(dt,'\n') # complete data of CSV
    
    df = pd.DataFrame(dt)
    columns_to_drop = ['Date & Time','Name','SAP ID','GPA']
    df.drop(columns_to_drop, axis=1, inplace=True)
    # Cleaned data of CSV
    
    print('       ~ ~ ~ Analysis: ~ ~ ~')
    
    num_rows = df.shape[0]# students count
    print("\n1. Number of students REGISTERED:", num_rows)
    
    print("\n2. Passing/Failing Percentage (Subjectwise): ")
    pass_counts = [0] * len(subject)
    fail_counts = [0] * len(subject)

    sub_pf = dt['Final_Pass_Fail']
    
    # Calculate pass and fail counts for each subject
    for row in sub_pf:
        if isinstance(row, str):
            pass_fail_list = eval(row)  # Convert string representation to actual list
            if len(pass_fail_list) == len(subject):
                for idx, status in enumerate(pass_fail_list):
                    if status == 'Pass':
                        pass_counts[idx] += 1
                    elif status == 'Fail':
                        fail_counts[idx] += 1

    # Calculate the total number of students
    total_students = len(sub_pf)
    
    # Calculate passing and failing percentages for each subject
    passing_percentages = [(count / total_students) * 100 for count in pass_counts]
    failing_percentages = [(count / total_students) * 100 for count in fail_counts]
    
    # Create a DataFrame to display the results
    result_df = pd.DataFrame({
        'Subjects': subject,
        'Passing Percentage': passing_percentages,
        'Failing Percentage': failing_percentages
    })    
    print(result_df)
    
    pass_count=[]
    for i in range(len(sub_pf)):
        count = 0
        if sub_pf[i].count('Pass') == 9:
            pass_count.append(1)
            
    passing_percentage = (len(pass_count) / len(sub_pf) ) * 100
    print('\n3. Overall passing percentage:',passing_percentage,'%')
    
    avg = np.mean(df) # pandas Series, of Average marks of each subjects
    print(f'\n4. Average marks scored by all in each SEM {sm} Subjects:')
    print(avg) 
    
    print('\n5. Failing Count: ')
    students_failing_1_subject = 0
    students_failing_2_subjects = 0
    students_failing_more_than_3_subjects = 0

    # Analyze students failing in 1 subject, 2 subjects, and more than 3 subjects
    for row in sub_pf:
        fail_count = row.count('Fail')
        if fail_count == 1:
            students_failing_1_subject += 1
        elif fail_count == 2:
            students_failing_2_subjects += 1
        elif fail_count >= 3:
            students_failing_more_than_3_subjects += 1

    print(f"Students failing in 1 subject: {students_failing_1_subject}")
    print(f"Students failing in 2 subjects: {students_failing_2_subjects}")
    print(f"Students failing in more than 3 subjects: {students_failing_more_than_3_subjects}")
    print('\n') 

    #piechart of overall passing and failing percentage (plot 1)
    y = np.array([passing_percentage, 100-passing_percentage])
    mylabels = ['Passing percentage', 'Failing percentage']
    myexplode = [0, 0.1]
    plt.pie(y, labels = mylabels, explode = myexplode,startangle = 90 , shadow = True)
    plt.legend(title = "Overall:")
    plt.show() 
    
    #linegraph of avg (plot 2)
    avg.plot(marker='*', linestyle='--', markersize=10, markeredgecolor='g')
    plt.xticks(rotation=45) 
    plt.xlabel('Subjects', fontsize=15)
    plt.ylabel('Marks', fontsize=15)
    plt.title('3. Average Marks In Respective Subjects', fontsize=15)
    plt.grid()
    plt.show()      
    
    # Reset display options to their defaults
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.width')
    pd.reset_option('display.max_colwidth') 