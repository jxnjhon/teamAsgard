class LearningMap():
    dict_skills = {}
    def add_studied_skills(self, skill):
        dict_skills[skill]=1
    def view_studied_skills(self, skill):
        skills_list = []
        for skill, value in dict_skills.items():
            if value == 1:
                skills_list.append(skill)
        return skills_list
    def view_unstudied_skills(self, skill):
        skills_list = []
        for skill, value in dict_skills.items():
            if value == 0:
                skills_list.append(skill)
        return skills_list
