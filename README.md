# GPA-Navigator-with-Exam-Prep-Companion-using-Python

This project is aimed at automating the calculation of students' Grade Point Averages (GPA) and providing insightful recommendations for Term End Exam (TEE) marks to enhance exam preparation. Developed for my University NMIMS School of Technology Management Engineering, CSE - Data Science branch.

## New Feature: Generate Goal Matrix

This tool now includes a powerful feature that allows users to generate a goal matrix based on the provided ICA (Internal Continuous Assessment) marks. The goal matrix provides minimum marks required for each grade, aiding students in setting realistic academic goals and optimizing their study strategies.

## Running the Program
When you run this program, it will prompt you to select one of the following options:

1. Generate Goal Matrix: Requires ICA marks as input for the selected semester.
2. Calculate SGPA and CGPA: Fast calculation that requires both ICA and TEE marks as input for the selected semester.

## How to use:

1. Ensure Python is installed on your computer.

2. To Record Data on local system (optional):

   I.  Open the code and locate line 7. Change the working directory to match your system's directory path. This ensures that the program saves data in the correct location.
   
      Example:
      os.chdir('/path/to/your/directory')
   
   II. Locate line 268 and replace the CSV file name with your CSV file name in the same directory for recording data. The current setting is 'recorded_data.csv'.
