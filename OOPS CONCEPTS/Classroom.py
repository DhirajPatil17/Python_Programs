


class Classroom:
    classroom_list=[]
    def set_list(self,class_room_list):
        Classroom.classroom_list=class_room_list
    


    @staticmethod
    def search_classroom(class_room):
        if class_room.lower() in[i.lower() for i in Classroom.classroom_list]:
            return "Found"
        else:
            return -1
s1=Classroom()
s1.set_list(['classA','classB','classC','classD','classE','classF'])
print(s1.search_classroom('classB'))
            