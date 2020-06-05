"""
It is a simple Program that displays all the covid-19 affected cases in India,
where we can display and check the condition of the covid-19 in India in following ways:
1)Display the total Cases in India
2)Display all the states in India.
3)Display the condition of a particular state.
"""
import time
import requests
from plyer import notification #I had imported the Notification class to create windows notification, so that the covid 19 cases would give a notification in Windows.
from bs4 import BeautifulSoup
"""
I did't use the Notification Panel, in this Project,instead I just displayed it 
in the console window.
You can use the Notification panel to display the covid cases, statwise
on Windows Notification.You Just have to Call the Notify app below and transfer
the State Name and the string of the cases in the state. 
"""
"""
def notifyapp(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:coronavirus.ico",
        timeout=5
    )
"""
# To get the HTML, data from the url of the mentioned site.
def htmlData(url):
    r=requests.get(url)
    return r.text
# Get the details of a particular state.
def statewise(states,ch):
    d=int(ch)-1
    stt=states[d]
    print("State Name:\t\t\tActive Cases\tCured/Discharged\tDeaths\tTotal Confirmed Cases")
    print(f"{stt[1]}\t\t\t{stt[2]}\t\t\t{stt[3]}\t\t\t\t{stt[4]}\t\t\t{stt[5]}")
    time.sleep(1)
# Get the details of total cases in India
def totalcases(t1):
    first=t1[0]
    total=[]
    for element in t1:
        total.append(element.strip())
    first1=first[7:]
    print("Active Cases\t\tCured/Discharged\t\tDeaths\t\tTotal Confirmed Cases")
    print(f"{first1}\t\t\t{total[1]}\t\t\t\t{total[2]}\t\t\t{total[3]}")
    time.sleep(1)
# Get the details of all the states in India
def allcases(states):
    #print("\t\tState Name:\t\t\tActive Cases\t\tCured/Discharged\t\tDeaths\t\tTotal Confirmed Cases")
    print("All the Affected States and their conditions: \n")
    for i in states:
        time.sleep(1)
        print(f"{i[0]}\tState Name: {i[1]}\t\tActive Cases: {i[2]}\t\tCured/Discharged: {i[3]}\t\tDeaths: {i[4]}\t\tTotal Confirmed Cases : {i[5]}\n")

if __name__ == '__main__':
    #notifyapp("Hello","Why")

    #Get the Html data  from the covid govt site
    htmltext=htmlData("https://www.mohfw.gov.in/")
    #Parsing the recieved Html data
    soup = BeautifulSoup(htmltext, 'html.parser')

    #(soup.prettify())

    #Processing the Data data to get the list of all the states and the total affected cases
    l=[]
    datastr=""
    for i in soup.find_all('tbody'):
        datastr=i.get_text()
    l=datastr.split("\n\n")
    for j in l:
        if j=='':
            l.remove(j)
    states=l[:35]
    total=l[37:41]
    """print(states)
    print(total)"""
    dl = []
    for s in states:
        ptr = s
        g = ptr.split("\n")
        if '' in g:
            g.remove('')
        dl.append(g)
    """print(dl)
    print(total)"""

    #Infinitely Running Menu to display the options
    while True:
        print("****************Corona Virus Updating System*******************")
        print("1.Total Cases in India")
        print("2.All States Detailed")
        print("3.State Wise Update")
        print("4.Exit System")
        ch1=input("Enter a choice number ")
        #For total case history in Country
        if ch1=='1':
            totalcases(total)
        #For the cases of all the states
        elif ch1=='2':
            allcases(dl)
        #For the case history of a particular state.
        elif ch1=='3':
            print("\n\n***List Of States****\n\n")
            print("1.Andaman and Nicobar Islands\n2.Andhra Pradesh\n3.Arunachal Pradesh\n4.Assam")
            print("5.Bihar\n6.Chandigarh\n7.Chhattisgarh\n8.Dadar Nagar Haveli\n9.Delhi\n10.Goa\n"
                  "11.Gujarat\n12.Haryana\n13.Himachal Pradesh\n14.Jammu and Kashmir\n"
                  "15.Jharkhand\n16.Karnataka\n17.Kerala\n18.Ladakh	\n19.Madhya Pradesh\n"
                  "20.Maharashtra\n21.Manipur\n22.Meghalaya\n23.Mizoram\n24.Nagaland\n"
                  "25.Odisha\n26.Puducherry\n27.Punjab\n28.Rajasthan\n29.Sikkim\n30.Tamil Nadu\n"
                  "31.Telengana\n32.Tripura\n33.Uttarakhand\n34.Uttar Pradesh\n35.West Bengal\n\n")
            time.sleep(1)
            c=input("Enter the serial no of state as shown in menu : ")
            try:
                if int(c)>0 and int(c)<=35:
                    statewise(dl,c)
                else:
                    print("You entered an incorrect serial no ")
            except ValueError:
                print("You have entered an incorrent statement, please input a correct serial no ")
        elif ch1=='4':
            print("Thank You for using our System!")
            time.sleep(1)
            break
        else:
            print("Invalid Choice Try Again : ")
            time.sleep(1)













