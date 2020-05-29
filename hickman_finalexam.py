"""
Author: Heather Hickman
Date: 5/6/2019
Program: hickman_finalexam.py
Summary: Write a class named Course that holds data about courses that will be taught in the Summer semester.
        The class should store the following data in attributes:
            course name, description, professor, number of sections offered
        Once you have written the class, write a program that creates three Course objects and stores the
        following data in them:

            Course Name     Description             Professor       # of sections
Course #1   IST 166         Network Fundamentals    TBA             1

Course #2   CPT 236         Intro to Java           Carman          2
                            programming

Course #3   IST161          Introduction to         Tessenear       2
                            Network Administration

Display the course information for each of the courses for the user to view.
"""
class Course:
    def __init__(self, courseName, description, professor, numSections):
        self.__courseName = courseName
        self.__description = description
        self.__professor = professor
        self.__numSections = numSections


    # define getters (accessors)
    def get_courseName(self):
        return self.__courseName

    def get_description(self):
        return self.__description

    def get_professor(self):
        return self.__professor

    def get_numSections(self):
        return self.__numSections


    # define setters (mutators)
    def set_courseName(self, courseName):
        self.__courseName = courseName

    def set__description(self, description):
        self.__description = description

    def set_professor(self, professor):
        self.__professor = professor

    def set_numSections(self, numSections):
        self.__numSections = numSections


    # define toString method and create a report for printing out the objects
    def courseReport(self):
            myCourseReport = ""
            myCourseReport += '{0:15}'.format("Course Name")
            myCourseReport += '{0:35}'.format("Description")
            myCourseReport += '{0:14}'.format("Professor")
            myCourseReport += "# of Sections\n"
            myCourseReport += ("-" * 77)
            return myCourseReport

    def __str__(self):
        myReturnString = ""
        myReturnString += '{0:15}'.format(self.get_courseName())
        myReturnString += '{0:35}'.format(self.get_description())
        myReturnString += '{0:16}'.format(self.get_professor())
        myReturnString += self.get_numSections()
        return myReturnString


# define a main function to instantiate instances of the class
# import Course is not needed because we are still inside the module that the class is written in
def main():
    course1 = Course("IST 166", "Network Fundamentals", "TBA", "1")
    course2 = Course("CPT 236", "Intro to Java Programming", "Carman", "2")
    course3 = Course("IST 161", "Intro to Network Administration", "Tessenear", "2")

    print(Course.courseReport(course1))
    print(course1)
    print(course2)
    print(course3)

main()