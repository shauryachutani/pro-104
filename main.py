import csv
import statistics as st
with open ("data.csv",newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)


height_list =[]

for i in data:
    height = float(i[1])
    height_list.append(height)
    

mean = st.mean(height_list)
median = st.median(height_list)
mode = st.mode(height_list)

print(mean,median,mode)
    