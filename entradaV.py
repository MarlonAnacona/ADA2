def readFile(file):
  with open(file, 'r') as entry:
    total_subjects = int(entry.readline())
    subjects = {}
    requests = {}

    for i in range(0, total_subjects):
      subject = entry.readline()
      subject = subject.split(",")
      subjects[subject[0]] = int(subject[1].strip())

    total_student = int(entry.readline())

    for i in range(0, total_student):
      
      student = entry.readline()
      student = student.split(",")

      new_student = {}
      student_subject = int(student[1].strip())
      
      for j in range (0, student_subject):
        requested_subject = entry.readline()
        requested_subject = requested_subject.split(",")
        new_student[requested_subject[0]] = int(requested_subject[1].strip())

      requests[student[0]] = new_student

    entry.close()
    return total_subjects, total_student, subjects, requests