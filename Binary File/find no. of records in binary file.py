import pickle
with open("binary.dat","wb") as f:
    dict1={1:["sam",10000],2:["jam",102000],3:["tim",150000]}
    pickle.dump(dict1,f)
    print("there are :",len(dict.keys()),"records in this data")
