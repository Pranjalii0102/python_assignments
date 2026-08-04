def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" *40)
        print("      DYNAMIC REPORT GENERATOR")
        print("=" * 40)
        result = func(*args, **kwargs)
        print("=" * 40)
        return result
    return wrapper

class Report:
    template ="Default Report Template"

    def __init__(self,title,content):
        self.title=title
        self.content=content

    @classmethod 
    def change_template(cls,new_template):
        cls.template=new_template

    def __str__(self):
        return f"Title  : {self.title} \nContent : {self.content}\nTemplate:{Report.template}"
    
    def __call__(self):
        print(f"Generating report {self.title}...")

    @report_decorator
    def generate_report(self):
            print(self)

print("Enter report details")
title=input("Enter Report Title:")
content=input("Enter report content:")

report = Report(title, content)

print("\nCurrent report :")
report.generate_report()

new_template=input("\nEnter New report template :")
Report.change_template(new_template)

print("\nUpdated Report :")
report.generate_report()

report()