class Doctor:
    def __init__(self,name,ID,contact,specialty,qualification,patient_info):
        self.name = name
        self.ID = ID
        self.contact = contact
        self.specialty = specialty
        self.qualification = qualification
        self.obj_patient = patient_info 
        print(__init__(a,b,c,d,e,f,g,d)
    def DisplayInfo(self):
        return ("Doctor", self.name,"\nID Number",int(self.ID), 'a qualified', self.qualification, "\nSpecializes in", self.specialty,"\nare dealing with",self.obj_patient.Display(),"\nTheir phone number is: ", int(self.contact))
    def Write_Prescription(self,Date,Disease,Medicine,Dosage,Issued_by):
        self.obj_prescription = Prescription(Date,Disease,Medicine,Dosage,Issued_by)
        return self.obj_prescription.Display()
    def DisplayPrescription(self):
        return (self.obj_prescription.Display())

#__init__(self,'Rana',33346,333467778,'lungs','MBBS',Patient1))
#Doctor1.DisplayInfo()
#Doctor1.Write_Prescription('18/02/20','Covid-19','Dexamethasone',1,'Dr.Rana')

#Pharmacist

class Pharmacist:
    def __init__(self,name,ID,contact,prescription):
        self.name = name
        self.ID = ID
        self.contact = contact
        self.obj_doctor = prescription
    def Display_Pharm(self):
        return ("Pharmacist:",self.name,"\nID:",self.ID,"\nContact Number:",self.contact)
    def Medicine_Bill(self):
        return (self.obj_doctor.DisplayPrescription())
        
#p=Pharmacist('Conner','180',987,Doctor1)
#p.Medicine_Bill()