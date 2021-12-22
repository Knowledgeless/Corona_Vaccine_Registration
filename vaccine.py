
'''
    Code Of : Corona Vaccine Registration
    Author  : Knowledgeless 
'''

# Importing Modules
import numpy as np
import pandas as pd
import datetime as dt
import random as rd
import os

# Vaccine Registration Class
class VaccineRegistration:
    def info(self):
        # User INFO Inputs
        self.name = input("Name\t:  ")
        self.id = input("NID no\t:  ")
        self.address = input("Address\t:  ")
        self.age = input("Age\t:  ")
        self.phone = input("Phone\t:  ")

        self.registrationInfo()
    
    # Validation Checking Starts
    def nameValidation(self, Name):
        if True in [name.isdigit() for name in Name] or not Name:
            print("\tName Can't Have Digits or It Can't Be Empty\n")
            exit()
        else:
            return Name

    def idValidation(self, ID):
        if False in [id.isdigit() for id in ID] or len(ID) != 13 or not ID:
            print("\tCheck Your Id Number & Try Again\n")
            exit()
        else:
            return ID
    
    def phoneValidation(self, Phone):
        if False in [phone.isdigit() for phone in Phone] or len(Phone) != 11 or not Phone:
            print("\tWrong Phone Number\n")
            exit()
        else:
            return Phone
    def addressValidation(self, Address):
        if True in [address.isdigit() for address in Address] or not Address:
            print("\tAddress Is Not Valid\n")
            exit()
        else:
            return Address
    
    def ageValidation(self, Age):
        if False in [age.isdigit() for age in Age] or len(Age) > 2 or not Age:
            print("\tAge Is not Correct\n")
            exit()
        else:
            return Age
    # Validation Checking Ends

    # Available Vaccine List
    def vaccineName(self):
        names = ["Moderna", "Sinopharm", "Pfizer", "Sinovac", "Oxford-AstraZeneca"]
        return names[rd.randint(0, len(names))-1].upper()
    

    # Registration Process
    def registrationInfo(self):
        
        #vaccination Date Finding
        today = dt.date.today()
        self.start = pd.to_datetime(today+dt.timedelta(days=2))
        self.end = pd.to_datetime(today+dt.timedelta(days=10))
        first_vaccine = self.randomdates(self.start, self.end)
        second_vaccine = "30 Days Later After 'First Vaccine'. "
        vaccine_name = self.vaccineName()

        #Keeping Data With Validation
        self.user_data = [self.nameValidation(self.name), self.idValidation(self.id), self.addressValidation(self.address), self.ageValidation(self.age), self.phoneValidation(self.phone), first_vaccine, second_vaccine, vaccine_name]
        self.header = ["Name", "NID", "Address", "Age", "Phone", "1st Vaccine", "2nd Vaccine", "Vaccine Name"]

        # Saving Data As CSV
        self.data = self.user_data
        self.data = pd.DataFrame([self.data], columns=self.header)
        if os.path.isfile("Vaccine_Registration.csv"):
            self.data.to_csv("Vaccine_Registration.csv", mode = "a", index=False, header=False)
        else:
            self.data.to_csv("Vaccine_Registration.csv", mode = "a", index=False)

    # Picing Date For Vaccination
    def randomdates(self, start, end, n=1):
        start_u = start.value//10**9
        end_u = end.value//10**9
        dates = pd.to_datetime(np.random.randint(int(start_u), int(end_u), n), unit='s')
        date= str(dates[0])
        return date[:11]

    # Showing Data To User
    def userDisplay(self):
        title = self.header
        data = self.user_data
        print('\n\t',"-"*60)
        print("""
            \t\t+--------------------------+
            \t\t| Registration Successfull |
            \t\t+--------------------------+
        """)
        for i,j in zip(title, data):
            print("\t\t{}\t: {}".format(i, j))
        print("\n\n\t [+] Please Go To {} Hospital To Be Vaccineted.\n".format(self.address))
        print('\t',"-"*60, "\n")


# Users FAQ Class
class FAQ:
    # Questions
    def question(self):
        q1 = "Is there any age preferences?"
        q2 = "Can I be vaccineted if I have any diseases?"
        q3 = "Is there any problem if I miss my '1st Vaccinetion' date?"
        q4 = "Can I switch to another Corona Vaccine?"
        self.questions = [q1, q2, q3, q4]       # Making Questions List
        return self.questions

    # Answers
    def answer(self):
        a1 = "No, Vaccine is for everyone (Human) who is alive in this planet."
        a2 = "No, You can't. Conduct to '16263' as soon as possible."
        a3 = "No problem. But try to be vaccineted on time."
        a4 = "Sorry, It's not possible. Thanks for asking."
        self.answers = [a1, a2, a3, a4]         # Making Answers List
        return self.answers

    def askHelp(self):
        # Variable Keeping
        ques = self.question()
        ans = self.answer()
        print("""
            \t+----------------------------+
            \t|         Corona FAQ         |
            \t+----------------------------+
        """)
        for q, a in zip(ques, ans):
            print("\n\t[+] {} \n\t=> {}".format(q, a))
        print("\n")

if __name__ == "__main__":
    print("\n\t\tWelcome to Vaccine Registration\t")
    print("\t","-"*45)
    choice = int(input("""
        1. Registration
        2. Corona Q&A
        3. Exit\n\n\tChoice: """))

    # Creating Classes Object
    vaccine = VaccineRegistration()
    helper = FAQ()

    # Calling Funcitons To Perform
    if choice == 1:
        vaccine.info()
        vaccine.userDisplay()
    elif choice == 2:
        helper.askHelp()
    elif choice == 3:
        print("\n\tGood Bye. Happy Coding..!\n")
        exit()
    else:
        print("\nTry Again\n")