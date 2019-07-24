class student(object):
	def __init__(self,name,number,degree):
	  self._name=name
	  self._number=number
	  self._degree=degree
	def get_name(self):
	  return self._name
	def get_number(self):
	  return self._number
	def get_degree(self):
	  return self._degree
	def set_degree(self,degree):
	  self._degree=degree
	def get_first_name(self):
	  return self._name.split()[0]
	def get_last_name(self):
	  return self._name.split()[1]
	def get_email(self):
	  return ("{0}.{1}@uq.net.au".format(self.get_first_name(),self.get_last_name()))
	def __str__(self):
	  return ("{0}({1},{2},{3})".format(self.get_name(),self.get_email(),self.get_number(),self.get_degree()))
	def __repr__(self):
	  return ("student({0},{1},{2})".format(self.get_name(),self.get_number(),self.get_degree()))


def check_student(student):
#This function is used to check whether each student has a unique student number
	f=[]
	for i in student:
	  ss=i.get_number()
	  if ss in f:
	    return False
	  f.append(ss)
	return True

class course(object):
	def __init__(self,code,name):
	  self._code=code
	  self._name=name
	def get_code(self):
	  return self._code
	def get_name(self):
	  return self._name

class student2(student):
	def __init__(self,name,number,degree):
	  super().__init__(name,number,degree)
	  self._grade={}
	def add_grade(self,course,grade):
	  self._grade[course]=grade
	  if course in self._grade.keys():
	    self._grade[course]=grade
	def gpa(self):
	  return sum(self._grade.values())/len(self._grade)
