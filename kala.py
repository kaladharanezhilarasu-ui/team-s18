total_classes = int(input("Enter the total number of classes: "))
attended_classes = int(input("Enter the number of classes attended: "))
attendance_percentage = (attended_classes / total_classes) * 100
print(f"Your attendance percentage is: {attendance_percentage:.2f}%")
if("attendance percentage >75%"):
  print("status:eligible")
else:
  print("status:not eligible")
    
