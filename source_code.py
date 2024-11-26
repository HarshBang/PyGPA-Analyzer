import numpy as np
import pandas as pd
import random

csds_semwise_subjects = {'sem1': ['Calculus', 'Programming for Problem Solving', 'Basic Electrical and Electronics Engineering','Engineering Graphics and Design', 'Elements of Biology', 'English Communication', 'Professional Ethics','Constitution of India', 'Design Thinking'],
                        
                        'sem2': ['Linear Algebra and Differential Equations', 'Physics', 'Digital Circuits and Computer Architecture', 'Principles of Economics and Management', 'Python for data analysis', 'Environmental Science', 'Digital Manufacturing Laboratory', 'Electrical and Electronics Workshop', 'Critical Thinking'],
                       
                        'sem3': ['Optimization methods', 'Data Structures and Algorithms', 'Probability and Statistics', 'Data Wrangling', 'Discrete Mathematics', 'Management Accounting for Engineers', 'Technical Communication', 'Community service'],
                        
                        'sem4': ['Machine learning', 'Introduction to Data, Signal, and Image Analysis', 'Statistical Methods', 'Database Management Systems', 'Web Programming', 'Data handling and Visualization'],
                        
                        'sem5': ['Software Engineering', 'Computer Networks', 'Operating Systems', 'Department Elective I', 'Open Elective I', 'Open Elective II', 'Mobile Application development'],
                        
                        'sem6': ['Applied Artificial Intelligence', 'Neural Networks and Deep Learning', 'Advance Data Structure for Analytics', 'Department Elective II', 'Department Elective III', 'Open Elective III', 'Open Elective IV ', 'Interpersonal Skills'],
                        
                        'sem7': ['Cloud Computing', 'Big Data', 'Computer Vision', 'Department Elective IV', 'Department Elective V', 'Open Elective V', 'Capstone Project'],
                        
                        'sem8': ['Project'] }

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
                        'sem5': [6,1],
                        'sem6': [7,1],
                        'sem7': [6,1],
                        'sem8': [0,1] } 

ce_semwise_subjects = {'sem1': ['Calculus', 'Programming for Problem Solving', 'Physics', 'Elements of Biology', 'Engineering Graphics and Design', 'Professional Ethics','Constitution of India', 'Critical Thinking'],
                        
                        'sem2': ['Linear Algebra and Differential Equations', 'Basic Electrical and Electronics Engineering', 'Quantum and Statistical Physics', 'Management Accounting for Engineers', 'Python Programming', 'Environmental Science', 'English Communication', 'Digital Manufacturing Laboratory', 'Electrical and Electronics Workshop', 'Design Thinking'],
                       
                        'sem3': ['Data Structures and Algorithms', 'Probability and Statistics', 'Discrete Mathematics', 'Principles of Economics and Management', 'Digital Logic Design', 'Computer Networks', 'Data Extraction and Processing', 'Technical Communication', 'Community service'],
                        
                        'sem4': ['Complex Variables and Transforms', 'Microprocessor and Microcontroller', 'Computer Organization and Architecture', 'Design and Analysis of Algorithm', 'Database Management Systems', 'Theoretical Computer Science', 'Web Programming', 'Object Oriented Programming through JAVA'],
                        
                        'sem5': ['Software Engineering', 'Artificial Intelligence', 'Operating Systems', 'Image and Video Processing', 'Department Elective I', 'Open Elective I', 'Open Elective II'],
                        
                        'sem6': ['Cyber Security', 'Distributed Computing', 'Machine Learning', 'Department Elective II', 'Department Elective III', 'Open Elective III', 'Open Elective IV ', 'Interpersonal Skills'],
                        
                        'sem7': ['Cloud Computing', 'Department Elective IV', 'Department Elective V', 'Department Elective VI', 'Open Elective V', 'Capstone Project'],
                        
                        'sem8': ['Project'] }

ce_sem_sub_credits = {'sem1': [4,4,4,3,3,1,0,0,19], #format: [credits of no of subjs, total sem credit]
                        'sem2': [4,3,3,2,2,1,1,1,1,0,18],
                        'sem3': [4,3,3,3,3,3,2,1,0,22],
                        'sem4': [4,4,3,3,3,3,3,1,24],
                        'sem5': [3,3,3,3,3,3,3,21],
                        'sem6': [3,3,3,3,3,3,3,1,22],
                        'sem7': [3,3,3,3,3,4,19],
                        'sem8': [10,10] } 

ce_sem_subs_exam_type = {'sem1': [5,3], # format: [no of subjects having term end exam, no of sub only ica marks]
                        'sem2': [5,5],
                        'sem3': [6,3],
                        'sem4': [7,1],
                        'sem5': [7,0],
                        'sem6': [7,1],
                        'sem7': [5,1],
                        'sem8': [0,1] } 

grade_dict_scale_4 = { 4:'A+', 3.75:'A', 3.5:'A-', 3.25:'B+', 3:'B', 2.75:'B-', 2.5:'C+', 2.25:'C', 2:'C-', 1.5:'D', 0:'F' }

grade_dict_scale_10 = { 10:'O', 9:'A+', 8:'A', 7:'B+', 6:'B', 5:'C', 4:'P', 0:'F' }

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
    
def get_sem(sem_subs_exam_type):
    sem_num = int(input('\nEnter Semesters: '))
    sem='sem'+str(sem_num)
    pre_sem = 'sem'+str(sem_num-1) #for cgpa calculation
    
    if sem in sem_subs_exam_type:
        tee_sub_count, ica_sub_count = sem_subs_exam_type[sem]
        
    return sem, pre_sem, tee_sub_count, ica_sub_count 

def goal_matrix(sem, tee_sub_count, semwise_subjects, low_marks, grade_dict_scale):
    
    print(f'\nEnter ICA marks of {sem}: ')
    
    ica=[]
    for sub in semwise_subjects[sem][0:tee_sub_count]:
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
    
    for i in ica:
        for j in low_marks:
            tee = (j-i)*2
            tee_data.append(tee)
    
    modified_tee_data = [max(0, value) for value in tee_data]   
    modified_tee_data = ['-' if value > 100 else value for value in modified_tee_data]
    reshaped_tee_data = np.array(modified_tee_data).reshape(-1,  len(grade_dict_scale))
    
    df = pd.DataFrame(reshaped_tee_data)
    df.index=semwise_subjects[sem][0:tee_sub_count]
    df.columns=grade_dict_scale.values()
    
    print('Goal Matrix:') 
    print('Shows the minimum marks required to get respective column grade', end='\n')  
    display_set()
    print(df)    
    display_reset()    

def input_marks(sem, tee_sub_count, ica_sub_count, semwise_subjects):
    ICA , TEE = [], []
    
    print('\n* Note *')
    print('Enter Internal Continous Assignment Marks (ICA) out of 50')
    print('& Term End Examination Marks(TEE) out of 100: ')
        
    for i in range(0, tee_sub_count):
        print(f'\nMarks in {semwise_subjects[sem][i]}:')
        
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
        print(f'\nMarks in {semwise_subjects[sem][j]}:')
        
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

def old_grade_point(sub_FM, grades_scored): 
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
        
def new_grade_point(sub_FM, grades_scored):
    if (sub_FM>=90 and sub_FM<=100):
        grades_scored.append(10)
    elif(sub_FM>=80 and sub_FM<=89.99):
        grades_scored.append(9)
    elif(sub_FM>=70 and sub_FM<=79.99):
        grades_scored.append(8)
    elif(sub_FM>=60 and sub_FM<=69.99):
        grades_scored.append(7)
    elif(sub_FM>=55 and sub_FM<=59.99):
        grades_scored.append(6)
    elif(sub_FM>=50 and sub_FM<=54.99):
        grades_scored.append(5)
    elif(sub_FM>=40 and sub_FM<=49.99):
        grades_scored.append(4)
    elif(sub_FM>=0 and sub_FM<=39.99):
        grades_scored.append(0)
        
def cal_gpa(total_m, tee_sub_count, ica_sub_count, sem, category, grade_dict_scale, sem_sub_credits):
    grades_scored = []
    
    if(category=="old"):
        for sub_FM in total_m:
            old_grade_point(sub_FM, grades_scored)
    elif(category=="new"):
        for sub_FM in total_m:
            new_grade_point(sub_FM, grades_scored)
    
    sub_wise_grade_scored = [grade_dict_scale[key] for key in grades_scored]
    
    if sem in sem_sub_credits:
        sem_sub_credits, sem_total_credits = sem_sub_credits[sem][:-1], sem_sub_credits[sem][-1]
        
    credits_mul_grades = []
    for i in range(tee_sub_count + ica_sub_count):
        credits_mul_grades.append( sem_sub_credits[i] * grades_scored[i])
        
    _sum=0
    for j in credits_mul_grades:
        _sum += j
    
    gpa = _sum / sem_total_credits
    
    return gpa, sub_wise_grade_scored, _sum

def generate_marks(difficulty):
    if difficulty == "easy":
        ica = random.randint(43, 50)
        tee = random.randint(40, 50)
    elif difficulty=="medium":
        ica = random.randint(35, 43)
        tee = random.randint(35, 43)
    else:
        ica = random.randint(25,35)
        tee = random.randint(25,35)
    return ica, tee
        
    
def generate_plans(subjects, difficulty_levels, tee_sub_count, ica_sub_count, sem, category, grade_dict_scale, sem_sub_credits):
    plan = []
    icas = []
    tees = []
    
    for i in range(len(subjects)):
        ica, tee = generate_marks(difficulty_levels[i])
        icas.append(ica)
        tees.append(tee)
        plan.append({
            "subject": subjects[i],
            "ICA": ica,
            "TEE": tee
        })
        
    total_m = cal_total_marks(icas, tees, tee_sub_count, ica_sub_count)
    gpa, _, __ = cal_gpa(total_m, tee_sub_count, ica_sub_count, sem, category, grade_dict_scale, sem_sub_credits)
    return plan, gpa
    
def generate_multiple_planes(subjects, target_gpa, difficulty_levels, tee_sub_count, ica_sub_count, sem, category, grade_dict_scale, sem_sub_credits, num_plans=4):
    plans = []
    for i in range(num_plans):
        plan, gpa = generate_plans(subjects, difficulty_levels, tee_sub_count, ica_sub_count, sem, category=category, grade_dict_scale=grade_dict_scale, sem_sub_credits=sem_sub_credits)
        plans.append({"plan":plan, "gpa": round(gpa,2)})
        if gpa >= target_gpa:
            print(f"Plan {i+1} has GPA: {gpa} (meets/exceeds target GPA: {target_gpa})")
        else:
            print(f"Plan {i+1} has GPA: {gpa} (below target GPA: {target_gpa})")
    return plans

#--main--
def run_cli_gpa_calculator():
    print('* '*20+str(' STME PyGPA Analyzer ')+' *'*22)
    
    name = input('Enter Name: ')
            
    while True:
        try:
            sap_id = input('Enter SAP ID: ')
            
            # Validate SAP ID length
            if len(sap_id) != 11: 
                print('Invalid input. Please enter a complete SAP ID.')
                continue
            
            if not sap_id.isdigit():
                print('Invalid input. SAP ID must contain only digits.')
                continue
            
            first_digits = sap_id[:4]  # Extract the first four digits for classification
            category, department = "", ""
    
            if first_digits == "7057":  # CSDS department
                if sap_id[:6] in ["705722", "705723"]:
                    category = "old"
                else:
                    category = "new"  
                department = "csds"
            
            elif first_digits == "7002":  # CE department
                if sap_id[:6] in ["700222", "700223"]:
                    category = "old"
                else:
                    category = "new"  
                department = "ce"
            
            else:
                print('Invalid SAP ID. Enter correct SAP ID.')
                continue
            
            break
        
        except ValueError:
            print('Invalid input. Please enter a correct SAP ID.')
            
    if (department=="csds"):
        sem_subs_exam_type = csds_sem_subs_exam_type
        semwise_subjects = csds_semwise_subjects
        sem_sub_credits = csds_sem_sub_credits
        
    elif (department=="ce"):
        sem_subs_exam_type = ce_sem_subs_exam_type
        semwise_subjects = ce_semwise_subjects
        sem_sub_credits = csds_sem_sub_credits
        
    if(category=="old"):
        low_marks = [85, 81, 77, 73, 69, 65, 61, 57, 50, 40, 0]
        grade_dict_scale = grade_dict_scale_4
        
    elif(category=="new"):
        low_marks = [90, 80, 70, 60, 55, 50, 40, 0]
        grade_dict_scale = grade_dict_scale_10
        
    print(f'\nWelcome, {name}')
    print('Enter 1: Goal Matrix: Designs TEE preparation plans based on ICA marks')
    print('Enter 2: Target GPA Planner: Create plans tailored to your subject difficulty level (Beta Version)')
    print('Enter 3: Calculate GPA')
    
    
    select = int(input('-> '))
    
    sem, pre_sem, tee_sub_count, ica_sub_count  = get_sem(sem_subs_exam_type)
    
    if select == 1:
        goal_matrix(sem, tee_sub_count, semwise_subjects, low_marks, grade_dict_scale)
    
    elif select == 2:
        subjects = semwise_subjects[sem]
        target_gpa = float(input('Enter Target GPA: '))
        
        difficulty_levels = []  # Store difficulty levels for each subject
        for sub in subjects:
            while True:
                difficulty = input(f'Rate difficulty for {sub} (easy, medium, hard): ').lower()
                
                if (difficulty == "e"):
                    difficulty = "easy"
                elif (difficulty == "m"):
                    difficulty = "medium"
                elif (difficulty == "h"):
                    difficulty = "hard"
                
                if difficulty in ['easy', 'medium', 'hard']:
                    difficulty_levels.append(difficulty)
                    break
                else:
                    print("Invalid input. Enter 'easy', 'medium', 'hard' or 'e', 'm', 'h'.")
        
        plans = generate_multiple_planes(subjects, target_gpa, difficulty_levels, tee_sub_count, ica_sub_count, sem, category, grade_dict_scale, sem_sub_credits)
        
        for idx, plan_info in enumerate(plans):
            print(f"\nPlan {idx+1}: (GPA: {plan_info['gpa']})")
            for subj_plan in plan_info["plan"]:
                print(f"{subj_plan['subject']}: ICA = {subj_plan['ICA']}, TEE = {subj_plan['TEE']}")
                
    elif select == 3:
        if sem != 'sem1':
            pre_cgpa = float(input('\nEnter CGPA: '))
    
        ica_m, tee_m = input_marks(sem, tee_sub_count, ica_sub_count, semwise_subjects)
        
        total_m = cal_total_marks(ica_m, tee_m, tee_sub_count, ica_sub_count)
                
        SGPA, sub_wise_grade_scored, sem_gpa_numerator = cal_gpa(total_m, tee_sub_count, ica_sub_count, sem, category, grade_dict_scale, sem_sub_credits)
        print('\n==> SGPA:', round(SGPA, 2))
        
        if sem != 'sem1':
                
            new_CGPA = ((pre_cgpa* sem_sub_credits[pre_sem][-1]) + (sem_gpa_numerator)) / (sem_sub_credits[sem][-1] + sem_sub_credits[pre_sem][-1])  
            print('\n==> CGPA:', "{:.3f}".format(new_CGPA)[:-1])
    
if __name__ == "__main__":
    run_cli_gpa_calculator()
