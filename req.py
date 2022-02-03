import requests
import json
import pprint


url = requests.get("https://api.merakilearn.org/courses")
data=url.json()
# print(data)

with open ("course.json","w") as file:
   json.dump(data,file,indent=2)

with open("course.json","r") as file:
   data1=json.load(file)



s=1
for j in data1:
   print(s,j["name"],j["id"])
   s=s+1


user_input=int(input("which course you want:"))-1

print(data1[user_input]["name"],":",data1[user_input]["id"])
api1=requests.get("https://api.merakilearn.org/courses/"+data1[user_input]["id"]+"/exercises")
data2=api1.json()
# pprint.pprint(data2)
with open("inside_course.json","w") as file_1:
   json.dump(data2,file_1,indent=2)

with open("inside_course.json","r") as file_1:
   data2=json.load(file_1)

x=1
y=1
lis1=[]
lis2=[]
for i in data2["course"]["exercises"]:
   if i["parent_exercise_id"]==None:
      print(x,i["name"])
      print(" ","1",i["slug"])
      lis1.append(i)
      lis2.append(i)
      x+=1
   elif i["id"]==i["parent_exercise_id"]:
      print(x,i["name"])
      lis2.append(i)
      x+=1
   elif i["id"]!=i["parent_exercise_id"]:
      print(" ",y,i["name"])
      y+=1 
      lis1.append(i)

with open ("exercise_diff.json","w") as file_2:
   json.dump(lis1,file_2,indent=2)
with open ("exercise_same.json","w") as file_3:
   json.dump(lis2,file_3,indent=2)




user_input_1=int(input("choose a course:"))



































































































































































# pprint.pprint(data3)


# x=1
# for x in range(len(data3["course"]["exercises"])):
#    print(x+1,data3["course"]["exercises"][x]["name"])
#    x+=1


# n=0
# temp_lis=[]
# lis=[]
# # while n<len(data2["course"]["exercises"]):
# for n in range(len(data2["course"]["exercises"])):
#    exercises_id=(data2["course"]["exercises"][n]["id"])
#    exercises_parent_id=(data2["course"]["exercises"][n]["parent_exercise_id"])

#    if exercises_id!=exercises_parent_id:
#       temp_lis.append(data2["course"]["exercises"][n])
#       print(n["name"])
      
#    if exercises_id==exercises_parent_id :
#       lis.append(data2["course"]["exercises"][n])
#    if exercises_parent_id==None:
#       # temp_lis.append(data2["course"]["exercises"][n])
#       lis.append(data2["course"]["exercises"][n])
#    n+=1  
# with open("exercises_diff.json","w") as file_3:
#    json.dump(temp_lis,file_3,indent=2)
# with open("exercises_same.json","w") as file_4:
#    json.dump(lis,file_4,indent=2)



# with open("exercises_diff.json","r") as file_3:
#    data3=json.load(file_3)
# with open("exercises_same.json","r") as file_4:
#    data4=json.load(file_4)




# n=1
# for x in data4 :
#    print(n,x["name"],"MAIN")
#    if x["parent_exercise_id"] in data3:
#       for y in data3:
#          print(y["name"],"SUB")
         
#    n+=1









































# temp_dic={}
# n=0
# while n<len(data3["course"]["exercises"]):
#    exercises_id=(data3["course"]["exercises"][n]["id"])
#    exercises_parent_id=(data3["course"]["exercises"][n]["parent_exercise_id"])
#    temp_dic[exercises_id]=exercises_parent_id
#    n+=1
# # print(temp_dic)
# dic_same={}
# dic_diff={}
# for k,v in temp_dic.items():  
#    if k==v or v==None :
#       dic_same[k]=v     
#    if k!=v:
#       dic_diff[k]=v    
# # print("dic_same:",dic_same)
# # print("dic_diff:",dic_diff)
# with open("ID_parent_Id_same.json","w") as file_2:
#    json.dump(dic_same,file_2,indent=2)
# with open("ID_parent_Id_diff.json","w") as file_3:
#    json.dump(dic_diff,file_3,indent=2)   

















# user_input_2=int(input("enter a indexing number:"))-1

# excersices_id=(data3["course"]["exercises"][user_input_2]["id"])
# exercises_parent_id=(data3["course"]["exercises"][user_input_2]["parent_exercise_id"])
# if excersices_id!=exercises_parent_id or exercises_parent_id==None:
#    with open("excercises_diff.json","w") as file_3:
#       json.dump(excersices_id,file_3,indent=2)
#    with open("excercises_diff.json","w") as file_3:
#       json.dump(exercises_parent_id,file_3,indent=2)
# elif excersices_id==exercises_parent_id or exercises_parent_id==None:
#    with open("excercises_same.json","w") as file_4:
#       json.dump(excersices_id,file_4,indent=2)
#       json.dump(exercises_parent_id,file_4,indent=2)






































# Input=input("enter previous or next to navigate:")
# if Input=="previous":
#    print(main_data[no-1]["name"],":",main_data[no]["id"])
# elif Input=="next":
#    print(main_data[no+1]["name"],":",main_data[no]["id"])


         