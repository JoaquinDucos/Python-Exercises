class Robot:
    def __init__(self,name, speed, job):
        self.name = name
        self.speed = speed
        self.job = job
 
    def clean_room(self,time):
        return(time/self.speed)
    def get_name(self):
        return(self.name)
    def get_job(self):
        return(self.job)
robot= Robot("iVaccum",10,"Cleaning")
robot.get_name()
robot.clean_room(20)
robot.get_job()