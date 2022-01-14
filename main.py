import tkinter as tk
from tkinter import * 
import tkinter.font as tkFont
import datetime

#Tkinter Init
root = tk.Tk()
root.title("Work Monitor")
#setting title
root.title("Work Monitor")
#setting window size
width=370
height=245
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.config(bg="black")

#Global Variables
topics = []
topStatus = []
topTime = []
flag_screen2 = 0
startTime = datetime.time()
activeTopic = StringVar()
pastTime = datetime.time()
On = False



def clearAll():
    global flag_screen2
    flag_screen2 = 0
    for frame in root.winfo_children():
        frame.destroy()



def screen1():
    clearAll()
    
    # topStatus = ["Not Started","Not Started","Not Started","Not Started","Not Started","Not Started","Not Started"]
    # topTime = [datetime.time(),datetime.time(),datetime.time(),datetime.time(),datetime.time(),datetime.time(),datetime.time()]

    
    titleFrame = Frame(root)
    titleFrame.pack()
    titleFrame.config(bg="black")
    welcomeLabel = Label(titleFrame, text="Good Morning", font =('arial', 20, 'bold'), bg="black", fg="#00FF00")
    welcomeLabel.pack(padx=26, pady=30)

    startButton = Button(titleFrame, text="Start DAY!!", command=startButton_command, 
                            width = 10, height = 2,bg="black", fg="#00FF00", 
                            font = ('arial', 10, 'bold'), activebackground="#00FF00", activeforeground="white")
    startButton.pack(padx=26, pady=30), 


def screen2():
    global flag_screen2
    clearAll()
    flag_screen2 = 1
    height = 200 + (len(topics) * 30)
    geo = "600x" + str(height)
    root.geometry(geo)
    
    #Frame to dislplay Date and Time
    workFrame = Frame(root)
    workFrame.pack()
    workFrame.config(bg="black")
    dateLabel = Label(workFrame, text="Date:", font =('arial', 14, 'bold'), bg="black", fg="#00FF00")
    dateoutLabel = Label(workFrame, text="########", font =('arial', 14, 'bold'), bg="black", fg="#00FF00")
    timeLabel = Label(workFrame, text="Time:", font =('arial', 14, 'bold'), bg="black", fg="#00FF00")
    timeoutLabel = Label(workFrame, text="########", font =('arial', 14, 'bold'), bg="black", fg="#00FF00")
    dateLabel.grid(row=0, column=0, padx=10, pady=10)
    dateoutLabel.grid(row=0, column=1, padx=10, pady=10)
    timeLabel.grid(row=0, column=2, padx=10, pady=10)
    timeoutLabel.grid(row=0, column=3, padx=10, pady=10)

    #Frame to set the current activity
    clicked = StringVar()
    activityFrame = Frame(root)
    activityFrame.pack()
    activityFrame.config(bg="black")
    HeadLabel = Label(activityFrame, text="Current Activity:", font =('arial', 10, 'normal'), bg="black", fg="#00FF00")
    HeadLabel.grid(row=0, column=0, padx=10, pady=10)
    
    buttonMenu = OptionMenu(activityFrame, clicked, *topics)
    buttonMenu.config( bg="black", fg="#00FF00", font = ('arial', 12, 'normal'), activebackground="#00FF00")
    buttonMenu.grid(row=0, column=1, padx=10, pady=10)

    statusLabel = Label(activityFrame, text="Status:", font =('arial', 12, 'normal'), bg="black", fg="#00FF00")
    statusLabel.grid(row=0, column=2, padx=10, pady=10)
    statusoutLabel = Label(activityFrame, text="########", font =('arial', 12, 'normal'), bg="black", fg="#00FF00")
    statusoutLabel.grid(row=0, column=3, padx=10, pady=10)

    actionButton = Button(activityFrame, text="Start", command=lambda: actionButton_command(clicked, actionButton),
                            width = 10, height = 1,bg="black", fg="#00FF00", 
                            font = ('arial', 10, 'bold'), activebackground="#00FF00", activeforeground="white")
    actionButton.grid(row=1, column=1, padx=10, pady=10)

    endDayButton = Button(activityFrame, text="End Day", command=lambda: endDay(),
                            width = 10, height = 1,bg="black", fg="#00FF00", 
                            font = ('arial', 10, 'bold'), activebackground="#00FF00", activeforeground="white")
    endDayButton.grid(row=1, column=2, padx=10, pady=10)


    #Frame to display the Activities
    topicFrame = Frame(root)
    topicFrame.pack()
    topicFrame.config(bg="black")

    Label(topicFrame, text="Topic", font =('arial', 14, 'bold'), bg="black", fg="#00FF00").grid(row=0, column=0, sticky=W, padx=40)
    Label(topicFrame, text="Status", font =('arial', 14, 'bold'), bg="black", fg="#00FF00").grid(row=0, column=1, sticky=W, padx=20)
    Label(topicFrame, text="Time", font =('arial', 14, 'bold'), bg="black", fg="#00FF00").grid(row=0, column=2, sticky=W, padx=20)
    
    status = []
    time = []

    for i in range(len(topics)):
        Label(topicFrame, text=topics[i], font =('arial', 12, 'normal'), bg="black", fg="#00FF00").grid(row=i+1, column=0, sticky=W, padx=40)
        status.append(Label(topicFrame, text=topStatus[i], font =('arial', 12, 'normal'), bg="black", fg="#00FF00"))
        status[i].grid(row=i+1, column=1, sticky=W)
        time.append(Label(topicFrame, text=topTime[i].strftime("%H:%M:%S"), font =('arial', 12, 'normal'), bg="black", fg="#00FF00"))
        time[i].grid(row=i+1, column=2, sticky=W)
    

    #Add Topic
    addTopicFrame = Frame(root)
    addTopicFrame.pack()
    addTopicFrame.config(bg="black")
    addTopicLabel = Label(addTopicFrame, text="Add Topic:", font =('arial', 12, 'bold'), bg="black", fg="#00FF00")
    addTopicLabel.grid(row=0, column=0, padx=10, pady=10)
    addTopicEntry = Entry(addTopicFrame, width=20, bg="green", fg="black", font =('arial', 12, 'bold'))
    addTopicEntry.grid(row=0, column=1, padx=10, pady=10)
    addTopicButton = Button(addTopicFrame, text="Add", command=lambda: addTopic(addTopicEntry),
                            width = 10, height = 1,bg="black", fg="#00FF00", 
                            font = ('arial', 10, 'bold'), activebackground="#00FF00", activeforeground="white")
    addTopicButton.grid(row=0, column=2, padx=10, pady=10)

    update(dateoutLabel, timeoutLabel, status, time, clicked, statusoutLabel)


def update(dateoutLabel, timeoutLabel, status, time, clicked, statusoutLabel):
    global flag_screen2, startTime, activeTopic, topics, topStatus, topTime
    if flag_screen2 == 0:
        return
    else:
        now = datetime.datetime.now()
        nowDate = now.strftime("%d/%m/%Y")
        nowTime = now.strftime("%I:%M:%S %p")
        dateoutLabel.config(text=nowDate)
        timeoutLabel.config(text=nowTime)
        for i in range(len(topics)):
            if activeTopic == topics[i]:
                spentTime = datetime.datetime.now() - startTime
                hour = (spentTime.days*24) +int(spentTime.seconds/3600) + pastTime.hour
                minute = int(spentTime.seconds/60) + pastTime.minute
                seconds = spentTime.seconds%60 + pastTime.second
                if seconds >= 60:
                    seconds -= 60
                    minute += 1
                topTime[i] = datetime.time(hour, minute, seconds)
            
            if topStatus[i] == "In Progress":
                status[i].config(text = topStatus[i], font=('arial',12,'bold'), fg="red")
            else:
                status[i].config(text=topStatus[i], font=('arial',12,'normal'),fg="#00FF00")
            time[i].config(text=topTime[i])          

            if clicked.get() == topics[i]:
                statusoutLabel.config(text=topStatus[i])
                

        root.after(100, lambda: update(dateoutLabel, timeoutLabel, status, time, clicked, statusoutLabel))




def startButton_command():
    global topics, topStatus, topTime
    topics = []
    with open("Topics.csv",'r') as file:
        while(True):
            row = file.readline()  
            if(row == ''):
                break
            topics.append(row.removesuffix('\n'))
    # print(topics)   

    topStatus = []
    topTime = []
    
    for i in range(len(topics)):
        topStatus.append("Not Started")
        topTime.append(datetime.time())

    screen2()

def actionButton_command(clicked, actionButton):
    global On, activeTopic, topics, topStatus, topTime, startTime, pastTime, logFlag
    if On == True:
        for i in range(len(topics)):
            if activeTopic == topics[i]:
                On = False
                topStatus[i] = "Done"
                spentTime = datetime.datetime.now() - startTime
                hour = (spentTime.days*24) +int(spentTime.seconds/3600) + pastTime.hour
                minute = int(spentTime.seconds/60) + pastTime.minute
                seconds = spentTime.seconds + pastTime.second
                topTime[i] = datetime.time(hour, minute, seconds)
                actionButton.config(text="Start", fg="#00FF00")
                log(activeTopic, startTime)
                activeTopic = ""
                
    else:
        for i in range(len(topics)):
            if clicked.get() == topics[i]:
                topStatus[i] = "In Progress"
                activeTopic = topics[i]
                startTime = datetime.datetime.now()
                pastTime = topTime[i]
                On = True
                actionButton.config(text="Stop", fg="red")

def log(activeTopic, startTime):
    spentTime = datetime.datetime.now() - startTime
    hour = (spentTime.days*24) +int(spentTime.seconds/3600)
    minute = int(spentTime.seconds/60) 
    seconds = spentTime.seconds 
    spent = datetime.time(hour, minute, seconds)
    now = datetime.datetime.now()
    nowDate = now.strftime("%d/%m/%Y")
    nowTime = now.strftime("%I:%M:%S %p")
    write = activeTopic + "," + nowDate + ',' + startTime.strftime("%I:%M:%S %p") + ',' + nowTime + ',' + spent.strftime("%X") + '\n'
    with open('log.csv', 'a') as f:
        f.write(write) 

def newlog(newactivity):
    now = datetime.datetime.now()
    nowDate = now.strftime("%d/%m/%Y")
    nowTime = now.strftime("%I:%M:%S %p")
    temp = datetime.time()
    write = newactivity + ',' + nowDate + ',' + nowTime + ',' + temp.strftime("%X") + ',' + temp.strftime("%X") + ',' + 'New Addition' +'\n'
    with open('log.csv', 'a') as f:
        f.write(write) 

def endDay():
    global topTime, topics, topStatus
    with open('EndDay_Log.csv','a') as file:
        file.write('\n' + "Date" + "," + datetime.datetime.now().strftime("%d/%m/%Y") + '\n')
        for i in range(len(topics)):
            file.write(topics[i] + "," + topStatus[i] + ',' + topTime[i].strftime("%X") + '\n')        
    screen1()

def addTopic(addTopicEntry):
    global topics, topStatus, topTime
    topics.append(addTopicEntry.get())
    newtopic = addTopicEntry.get()
    with open("Topics.csv",'a') as file:
        file.write(addTopicEntry.get() + '\n')
    topStatus.append("Not Started")
    topTime.append(datetime.time())
    newlog(newtopic)
    addTopicEntry.delete(0, END)
    screen2()

if __name__ == "__main__":
    screen1()
    root.mainloop()
