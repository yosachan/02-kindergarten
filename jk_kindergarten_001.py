class SchoolReport:
    def __init__(self, student_name):
        self.student_name = student_name
        
sr_a = SchoolReport("田中　A")
sr_b = SchoolReport("鈴木　B")
sr_c = SchoolReport("斎藤　C")
print(sr_a.student_name)
print(sr_b.student_name)
print(sr_c.student_name)
