class Instructor: 
    def _init(self): 
        self.instructor_name = None 
        self.experience = None 
        self.technology_skill = [] 
        self.avg_feedback = None 
    def set_instructor_name(self, instructor_name): 
            self.instructor_name = instructor_name 
    def get_instructor_name(self): 
            return self.instructor_name 
    def set_experience(self, experience): 
            self.experience = experience 
    def get_experience(self): 
            return self.experience 
    def set_technology_skill(self, technology_skill): 
            self.technology_skill = technology_skill 
    def get_technology_skill(self): 
            return self.technology_skill 
    def set_avg_feedback(self, avg_feedback): 
            self.avg_feedback = avg_feedback 
    def get_avg_feedback(self): 
            return self.avg_feedback 
    def check_eligibility(self): 
            if self.experience > 3 and self.avg_feedback >= 4.5: 
                return True 
            elif self.experience <= 3 and self.avg_feedback >= 4: 
                return True 
            else: return False 
    def allocate_course(self, technology): 
            if self.check_eligibility() == True: 
                if technology in self._technology_skill: 
                    return True 
                else: return False 
            else: return False 
instructor1 = Instructor() 
instructor1.set_instructor_name("Raunak Mitra") 
instructor1.set_experience(4) 
instructor1.set_avg_feedback(2) 
instructor1.set_technology_skill(["Python", "Java", "C++", "C"]) 
print(instructor1.allocate_course("Python"))