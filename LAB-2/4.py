class Patient:
  #write a constructor
  def __init__(self, id, name, age, bloodgroup, next=None, prev=None):
    self.id = id
    self.name = name
    self.age = age
    self.bloodgroup = bloodgroup
    self.next = next
    self.prev = prev
from re import escape
#Task-4
class WRM:

  def __init__(self):
    #Creating the dummy head
    self.dh = Patient(None,None,None,None,None,None)
    self.dh.next = self.dh
    self.dh.prev = self.dh

  def registerPatient(self,id, name, age, bloodgroup):
    new_patient = Patient(id, name, age, bloodgroup)
    new_patient.next = self.dh
    new_patient.prev = self.dh.prev
    self.dh.prev.next = new_patient
    self.dh.prev = new_patient
    print(f"Patient {name} is registered successfully.")

  def servePatient(self):
    if self.dh.next == self.dh:
      print("No patients in the queue.")
      return None
    else:
      served_patient = self.dh.next
      print(f"Serving patient: {served_patient.name} (ID: {served_patient.id})")
      self.dh.next = served_patient.next
      served_patient.next.prev = self.dh
      return served_patient

  def showAllPatient(self):
    if self.dh.next == self.dh:
      print("No patients in the queue.")
      return
    else:
      current = self.dh.next
      print("Patients in the waiting list:")
      while current != self.dh:
        print(f"Name: {current.name}\n ID: {current.id}\n Age: {current.age}\n Blood Group: {current.bloodgroup}")
        current=current.next


  def canDoctorGoHome(self):
    if self.dh.next == self.dh:
      print("Yes, the doctor can go home.")
      return True
    else:
      print("No, there are patients waiting.")
      return False

  def cancelAll(self):
    if self.dh.next == self.dh:
      print("No patients to cancel.")
      return
    else:
      self.dh.next = self.dh
      self.dh.prev = self.dh
      print("All appointments have been canceled.")

  def ReverseTheLine(self):
    if self.dh.next == self.dh:
      print("No patients in the queue to reverse.")
      return
    current = self.dh
    while True:
        temp = current.next
        current.next = current.prev
        current.prev = temp
        current = temp
        if current == self.dh:
            break
    print("The waiting line has been reversed.")
#Write a Tester Code in this cell
print("**Welcome to Waiting Room Management System**")
wrm = WRM()

# Register some patients
wrm.registerPatient(1, "Luffy", 22, "A+")
wrm.registerPatient(2, "Brook", 60, "O-")
wrm.registerPatient(3, "Zoro", 40, "O+")
wrm.registerPatient(4, "Sanji", 35, "AB+")

print("\n**Current Waiting List**")
wrm.showAllPatient()

print("\n**Serving the Next Patient**")
wrm.servePatient()

print("\n**Updated Waiting List**")
wrm.showAllPatient()

print("\n**Can the Doctor Go Home?**")
wrm.canDoctorGoHome()

print("\n**Reversing the Waiting Line**")
wrm.ReverseTheLine()

print("\n**Waiting List After Reversing**")
wrm.showAllPatient()

print("\n**Canceling All Appointments**")
wrm.cancelAll()

print("\n**Can the Doctor Go Home Now?**")
wrm.canDoctorGoHome()

print("\n**Attempting to Serve a Patient When the List is Empty**")
wrm.servePatient()

print("\n**Final Waiting List**")
wrm.showAllPatient()
