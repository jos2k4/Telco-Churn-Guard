import subprocess


process1 = subprocess.Popen(["python", "churn.py"])
process2 = subprocess.Popen(["python", "lost_revenue.py"])
process3 = subprocess.Popen(["python", "tech_support.py"])

process1.wait()
process2.wait()
process3.wait()