#Create a class that will encapsulate the functionality of the To-Do List.
class ToDoList:
    def __init__(self):
        #initialize the to-do list structure
        self.months=['January','February','March','April','May','June','July','August','September','October','November','December']
        self.weeks=['Week 1','Week 2','Week 3','Week 4','Week 5']
        self.days_of_the_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.to_do_list={month: {week: {day: [[], []] for day in self.days_of_the_week}for week in self.weeks} for month in self.months}
        
    def displayTask(self, month, week, day, task):
        #prints the tasks for that specific date
        print(f"Tasks for {month}-{week}-{day}:")
        print("1. New Task:", self.to_do_list[month][week][day][0])
        print("2. Completed Task:", self.to_do_list[month][week][day][1])
        
    def addTask(self, month, week, day, task, status='new'):
        #the default status of a task is new
        if status=='new':
            self.to_do_list[month][week][day][0].extend(task)
        elif status=='Completed':
            self.to_do_list[month][week][day][1].extend(task)
        else:
            print("Invalid status. Task not added!")   
            
    def pinTask(self, month, week, day, task):
        if task in self.to_do_list[month][week][day][0]:
            status = 'New'
        elif task in self.to_do_list[month][week][day][1]:
            status = 'Completed'
        else:
            print(f"Task {task} not found.")
            
        #find the index for our task in the 'New' or 'Completed' sublists
        taskIndex = None
        for index, sublist in enumerate(self.to_do_list[month][week][day][0] if status == 'New' else self.to_do_list[month][week][day][1]):
            if task in sublist:
                taskIndex = index
                break
        if taskIndex is not None:    
            #Remove task from its current position
            removedTask = self.to_do_list[month][week][day][0 if status == 'New' else 1][taskIndex]
            self.to_do_list[month][week][day][0 if status == 'New' else 1].remove(removedTask)
            #pin to the top
            self.to_do_list[month][week][day][0 if status == 'New' else 1].insert(0,removedTask)
            print(f"Task {task} has been pinned at the top of {status} tasks")
        else:
            print(f"Task {task} is not in {status} tasks")
        
    def markAsCompleted(self, month, week, day, task):
        #marks a task as complete by moving it from 'New' to 'Completed'
        if task in self.to_do_list[month][week][day][0]:
          self.to_do_list[month][week][day][0].remove(task)  
          self.to_do_list[month][week][day][1].append(task)
          print(f"Task {task} is completed")
        else:
            print(f"Task {task} is not in new tasks")
            
            
#example usage
#create an instance of the ToDoList class
to_do_list_student =  ToDoList()  
     
#choose task and its date 
selectedMonth = 'December'
selectedWeek = 'Week 2'
selectedDay = 'Wednesday'
selectedTasks = ['Study Lists Data Structures','Study Python Programming Language','Relax']

#add and display the task
to_do_list_student.addTask(selectedMonth,selectedWeek,selectedDay,selectedTasks)
to_do_list_student.displayTask(selectedMonth,selectedWeek,selectedDay,selectedTasks)

#mark 'Study Lists Data Structures' as completed and display updated tasks
to_do_list_student.markAsCompleted(selectedMonth,selectedWeek,selectedDay,'Study Lists Data Structures')
to_do_list_student.displayTask(selectedMonth,selectedWeek,selectedDay,selectedTasks)

#pin task and display updated tasks
to_do_list_student.pinTask(selectedMonth,selectedWeek,selectedDay,'Relax')
to_do_list_student.displayTask(selectedMonth,selectedWeek,selectedDay,selectedTasks)






    

    