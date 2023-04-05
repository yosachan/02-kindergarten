class SchoolReport:
    school_name = "JK中学校" #クラス変数名
    # SchoolReport.school_name <=クラス変数にアクセス
    # print(self.school_name) <=クラス変数にアクセス
    
    def __init__(self, student_name, 
                 math_score, jp_score, en_score):
        self.student_name = student_name #インスタンス変数
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score
  
    def calc_avg_score(self):
        self.sum_score = (self.math_score
                     + self.jp_score + self.en_score)
        avg_score = self.sum_score / 3
        return avg_score
              
sr_a = SchoolReport("田中　A", 100, 30, 50)
avg_a = sr_a.calc_avg_score()
print(sr_a.sum_score)

sr_b = SchoolReport("鈴木　B", 20, 59, 20)
avg_b = sr_b.calc_avg_score()

sr_c = SchoolReport("斎藤　C", 19, 22, 19)
avg_c = sr_c.calc_avg_score()

print(f"Aさんの3教科平均点： {avg_a}")
print(f"Bさんの3教科平均点： {avg_b}")
print(f"Cさんの3教科平均点： {avg_c}")

print(sr_a.school_name)
SchoolReport.school_name = "JK高校"
print(sr_a.school_name)

