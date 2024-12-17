import streamlit as st
import pandas as pd
import numpy as np

# Import the core functions from the original script
from source_code import (
    csds_semwise_subjects, ce_semwise_subjects,
    csds_sem_subs_exam_type, ce_sem_subs_exam_type,
    csds_sem_sub_credits, ce_sem_sub_credits,
    grade_dict_scale_4, grade_dict_scale_10,
    cal_total_marks, generate_multiple_planes,
)

def validate_sap_id(sap_id):
    # Validate SAP ID logic from original script
    if len(sap_id) != 11 or not sap_id.isdigit():
        return False, None, None
    
    first_digits = sap_id[:4]
    
    if first_digits == "7057":  # CSDS department
        category = "old" if sap_id[:6] in ["705722", "705723"] else "new"
        department = "csds"
    elif first_digits == "7002":  # CE department
        category = "old" if sap_id[:6] in ["700222", "700223"] else "new"
        department = "ce"
    else:
        return False, None, None
    
    return True, category, department

def get_department_config(department):
    if department == "csds":
        return (csds_sem_subs_exam_type, 
                csds_semwise_subjects, 
                csds_sem_sub_credits)
    else:  # ce
        return (ce_sem_subs_exam_type, 
                ce_semwise_subjects, 
                ce_sem_sub_credits)  # Note: using CSDS credits as per original script

def calculate_goal_matrix(ica_marks, tee_sub_count, semwise_subjects, low_marks, grade_dict_scale, sem):
    """
    Recreate the goal matrix calculation logic from the original script
    """
    tee_data = []
    
    for i in ica_marks:
        for j in low_marks:
            tee = (j - i) * 2
            tee_data.append(tee)
    
    # Modify TEE data to handle impossible scenarios
    modified_tee_data = [max(0, value) for value in tee_data]   
    modified_tee_data = ['-' if value > 100 else value for value in modified_tee_data]
    
    # Reshape the data to match the original matrix structure
    reshaped_tee_data = np.array(modified_tee_data).reshape(-1, len(grade_dict_scale))
    
    # Create DataFrame with subjects as index and grades as columns
    df = pd.DataFrame(reshaped_tee_data)
    df.index = semwise_subjects[sem][:tee_sub_count]
    df.columns = list(grade_dict_scale.values())
    
    return df

# Modify the Goal Matrix section in your main Streamlit app
def goal_matrix_section(sem, tee_sub_count, semwise_subjects, low_marks, grade_dict_scale):
    st.header("Goal Matrix")
    st.write("Shows minimum TEE marks required for different grades")
    
    # ICA Marks Input
    ica_marks = []
    for sub in semwise_subjects[sem][:tee_sub_count]:
        ica = st.number_input(f"ICA Marks for {sub} (out of 50)", 
                              min_value=0, max_value=50, key=f"goal_ica_{sub}")
        ica_marks.append(ica)
    
    if st.button("Generate Goal Matrix"):
        goal_matrix_df = calculate_goal_matrix(
            ica_marks, 
            tee_sub_count, 
            semwise_subjects, 
            low_marks, 
            grade_dict_scale, 
            sem
        )
        
        # Explanation of the matrix
        st.markdown("""
        ### Goal Matrix Explanation
        - Each row represents a subject having TEE
        - Each column represents a grade
        - Values show the minimum TEE marks needed to achieve that grade, 
          considering your current ICA marks
        - '-' indicates the grade is unachievable with current ICA marks
        """)
        
        # Display the goal matrix
        st.dataframe(goal_matrix_df)
        
def cal_gpa(total_m, tee_sub_count, ica_sub_count, sem, category, grade_dict_scale, sem_sub_credits):
    grades_scored = []
    
    if category == "old":
        for sub_FM in total_m:
            if sub_FM >= 85:
                grades_scored.append(4.00)
            elif sub_FM >= 81:
                grades_scored.append(3.75)
            elif sub_FM >= 77:
                grades_scored.append(3.50)
            elif sub_FM >= 73:
                grades_scored.append(3.25)
            elif sub_FM >= 69:
                grades_scored.append(3.00)
            elif sub_FM >= 65:
                grades_scored.append(2.75)
            elif sub_FM >= 61:
                grades_scored.append(2.50)
            elif sub_FM >= 57:
                grades_scored.append(2.25)
            elif sub_FM >= 50:
                grades_scored.append(2.00)
            elif sub_FM >= 40:
                grades_scored.append(1.15)
            else:
                grades_scored.append(0)
    else:  # new category
        for sub_FM in total_m:
            if sub_FM >= 90:
                grades_scored.append(10)
            elif sub_FM >= 80:
                grades_scored.append(9)
            elif sub_FM >= 70:
                grades_scored.append(8)
            elif sub_FM >= 60:
                grades_scored.append(7)
            elif sub_FM >= 55:
                grades_scored.append(6)
            elif sub_FM >= 50:
                grades_scored.append(5)
            elif sub_FM >= 40:
                grades_scored.append(4)
            else:
                grades_scored.append(0)
    
    # Use the numeric grades for lookup to prevent key errors
    sub_wise_grade_scored = [grade_dict_scale.get(key, 'F') for key in grades_scored]
    
    if sem in sem_sub_credits:
        sem_sub_credits_list, sem_total_credits = sem_sub_credits[sem][:-1], sem_sub_credits[sem][-1]
        
    credits_mul_grades = []
    for i in range(tee_sub_count + ica_sub_count):
        credits_mul_grades.append(sem_sub_credits_list[i] * grades_scored[i])
    
    _sum = sum(credits_mul_grades)
    gpa = _sum / sem_total_credits
    
    return gpa, sub_wise_grade_scored, _sum

def add_sidebar_footer():
    """
    Add a footer to the sidebar with copyright and GitHub link
    """
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
     <div style='text-align: center; font-size: 0.8em; color: gray;'>
    © 2024 PyGPA Analyzer <br> Developed by Harsh Bang | <a href='https://github.com/HarshBang' target='_blank'>GitHub Profile</a>
    </div>
    """, unsafe_allow_html=True)    

def main():
    st.title("STME HYD PyGPA Analyzer")
    st.sidebar.image('logo.svg', use_container_width=True)
    
    # Sidebar for Student Details
    st.sidebar.header("Student Information")
    
    name = st.sidebar.text_input("Enter your name")
    sap_id = st.sidebar.text_input("Enter your SAP ID")
    
    # Display different messages based on screen size and input details
    if name and sap_id:
        st.write(f"Hello, {name}.")
    else:
        st.write("To proceed, please enter your student information in the sidebar.")
    
    # Validate SAP ID
    if sap_id:
        is_valid, category, department = validate_sap_id(sap_id)
        
        if not is_valid:
            st.sidebar.error("Invalid SAP ID")
            return
        
        st.sidebar.success(f"Valid SAP ID for {department.upper()} Department")
        
        # Get department-specific configurations
        sem_subs_exam_type, semwise_subjects, sem_sub_credits = get_department_config(department)
        
        # Determine grading scale
        if category == "old":
            low_marks = [85, 81, 77, 73, 69, 65, 61, 57, 50, 40, 0]
            grade_dict_scale = grade_dict_scale_4
        else:
            low_marks = [90, 80, 70, 60, 55, 50, 40, 0]
            grade_dict_scale = grade_dict_scale_10
        
        # Main feature selection
        feature = st.radio("Select Feature", 
                           ["Goal Matrix", 
                            "Calculate GPA",
                            "Target GPA Planner"])
        
        # Semester Selection
        semesters = list(range(1, 9))
        sem_num = st.selectbox("Select Semester", semesters)
        sem = f'sem{sem_num}'
        
        # Get exam configuration for selected semester
        tee_sub_count, ica_sub_count = sem_subs_exam_type[sem]
        subjects = semwise_subjects[sem]
        
        if feature == "Goal Matrix":
            goal_matrix_section(sem, tee_sub_count, semwise_subjects, low_marks, grade_dict_scale)
        
        elif feature == "Target GPA Planner":
            st.header("Target GPA Planner (Beta Version)")
            
            if category == "old":
                # Limit input to 4.0 for old category
                target_gpa = st.number_input("Enter Target GPA", 
                                            min_value=0.0, max_value=4.0, value=3.5, step=0.1,
                                            help="For old grading system, CGPA is on a 4.0 scale")
            else:
                # Allow up to 10.0 for new category
                target_gpa = st.number_input("Enter Target GPA", 
                                            min_value=0.0, max_value=10.0, value=7.0, step=0.1,
                                            help="For new grading system, CGPA is on a 10.0 scale")
                
            # Difficulty selection for each subject
            difficulty_levels = []
            for sub in subjects:
                difficulty = st.selectbox(f"Difficulty for {sub}", 
                                          ["easy", "medium", "hard"])
                difficulty_levels.append(difficulty)
            
            # Generate plans
            if st.button("Generate Study Plans"):
                plans = generate_multiple_planes(
                    subjects, target_gpa, difficulty_levels, 
                    tee_sub_count, ica_sub_count, sem,
                    category=category,  # Add category
                    grade_dict_scale=grade_dict_scale,  # Add grade dictionary
                    sem_sub_credits=sem_sub_credits,  # Add semester credits
                    num_plans=4  # Optional: number of plans to generate
                )
                
                for idx, plan_info in enumerate(plans, 1):
                    st.subheader(f"Plan {idx} (GPA: {plan_info['gpa']})")
                    plan_details = pd.DataFrame(plan_info["plan"])
                    st.table(plan_details)
        
        elif feature == "Calculate GPA":
            st.header("GPA Calculator")
    
            # Handling first semester differently
            if sem_num > 1:
                if category == "old":
                    # Limit input to 4.0 for old category
                    prev_cgpa = st.number_input("Enter Current CGPA", 
                                                min_value=0.0, max_value=4.0, value=0.0, step=0.1,
                                                help="For old grading system, CGPA is on a 4.0 scale")
                else:
                    # Allow up to 10.0 for new category
                    prev_cgpa = st.number_input("Enter Previous CGPA", 
                                                min_value=0.0, max_value=10.0, value=0.0, step=0.1,
                                                help="For new grading system, CGPA is on a 10.0 scale")
            
            # Marks input
            st.subheader("Note: Enter ICA Marks out of 50 and TEE Marks out of 100")
            st.write("")
            
            ica_marks, tee_marks = [], []
            
            # Term End Exam Subjects
            for sub in subjects[:tee_sub_count]:
                st.write(f"{sub}:")
                ica = st.number_input("ICA Marks", 
                                      min_value=0, max_value=50, key=f"ica_{sub}")
                tee = st.number_input("TEE Marks", 
                                      min_value=0, max_value=100, key=f"tee_{sub}")
                ica_marks.append(ica)
                tee_marks.append(tee)
            
            # ICA Only Subjects
            for sub in subjects[tee_sub_count:]:
                st.write(f"{sub}:")
                ica = st.number_input("ICA Marks)", 
                                      min_value=0, max_value=50, key=f"ica_{sub}")
                ica_marks.append(ica)
                tee_marks.append(0)
            
            if st.button("Calculate GPA"):
                # Modify TEE marks calculation as in original script
                tee_marks_adjusted = [mark/2 for mark in tee_marks[:tee_sub_count]] + tee_marks[tee_sub_count:]
                
                # Adjust ICA marks for ICA-only subjects
                ica_marks_adjusted = (
                    ica_marks[:tee_sub_count] + 
                    [ica * 2 for ica in ica_marks[tee_sub_count:]]
                )
                
                final_marks = cal_total_marks(ica_marks_adjusted, tee_marks_adjusted, tee_sub_count, ica_sub_count)
                
                sgpa, sub_grades, sem_gpa_numerator = cal_gpa(
                    final_marks, tee_sub_count, ica_sub_count, 
                    sem, category, grade_dict_scale, sem_sub_credits
                )
                    
                grade_to_point = {value:key for key, value in grade_dict_scale.items()}
                grade_points = [grade_to_point[grade] for grade in sub_grades]
                
                # Create a results dataframe
                results_df = pd.DataFrame({
                    'Subject': subjects[:tee_sub_count + ica_sub_count],
                    'Credits':sem_sub_credits[sem][:-1],
                    'Final Marks': final_marks,
                    'Grade': sub_grades,
                    'Grade Point' : grade_points,
                    'Total': np.array(sem_sub_credits[sem][:-1]) * np.array(grade_points)
                })
                
                results_df.index = range(1, len(results_df) + 1)
                st.dataframe(results_df)
                
                # Display results
                st.success(f"Semester GPA: {sgpa:.2f}")
                
                # CGPA calculation for semesters after first
                if sem_num > 1:
                    prev_sem = f'sem{sem_num - 1}'
                    prev_sem_credits = sem_sub_credits[prev_sem][-1]
                    current_sem_credits = sem_sub_credits[sem][-1]
    
                    new_cgpa = ((prev_cgpa * prev_sem_credits) + sem_gpa_numerator) / (current_sem_credits + prev_sem_credits)
    
                    st.success(f"Cumulative GPA: {new_cgpa:.2f}")
               
    add_sidebar_footer()
                
if __name__ == "__main__":
    main()
