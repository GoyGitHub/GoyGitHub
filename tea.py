import os
path = os.getcwd()+ "/my-folder"
if not os.path.exists(path):
    os.makedirs(path)
filename = "/my-text.txt"
with open(path+filename,"a") as file:
    file.write("hELLO WORLD")

filename = "/my-poem.txt"
with open(path+filename, "r")as file:
    data=file.read()
    print(data)