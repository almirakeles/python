job_title = "data analyst"
job_location = "Istanbul"
job_salary = 250000

print(f"JOB:   {job_title}\nLOCATION :   {job_location}\nSALARY :    ${job_salary :,.0f}")


def display_info_(title,location,salary):
    return print(f"JOB:  {title}\nLOCATION:   {location}\nSALARY:    ${job_salary : ,.0f}")



#CLASSES, OBJECTS, METHODS, ATTRIBUTES




class JobPost:
    def __init__(self, title, location, salary):
        self.title = title
        self.location = location
        self.salary = salary
    def display_info(self):
        return print(f"JOB:  {self.title}\nLOCATION:   {self.location}\nSALARY:    ${self.salary : ,.0f}")    
job_1 = JobPost(job_title, job_location, job_salary)
job_1.display_info()
        
