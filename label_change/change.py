import os

def decoder(datafile_path):
    with open(datafile_path+"classes.txt") as decoder_file:
        decoder_cat = decoder_file.read()
        decoder_cat = decoder_cat.split("\n")
    file = os.listdir(datafile_path)
    try:
        file.remove("classes.txt")
    except:
        return "no classes.txt found"
    for txt in file:
        if ".txt" in txt:
            with open(datafile_path + txt,) as txt_file:
                content = txt_file.read()
                content = content.split("\n")
                #### decoding
                new_content = ""
                for data in content:
                    data = data.split(" ")
                    code = int(float(data[0]))
                    data[0] = decoder_cat[code]
                    #print(data)
                    data = " ".join(data)
                    new_content = new_content + data[0:] +"\n"
                #print (new_content)
            with open(datafile_path+"\\" + txt,"w") as txt_file:
                ####重新寫入decode 後資料
                #print(new_content[:-1])
                txt_file.write(new_content[:-1])
    return "decode mission completed  : "+ datafile_path


def encoder(datafile_path):
    with open(datafile_path+"classes.txt") as decoder_file:
        decoder_cat = decoder_file.read()
        decoder_cat = decoder_cat.split("\n")
    file = os.listdir(datafile_path)
    try:
        file.remove("classes.txt")
    except:
        return "no classes.txt found"
    for txt in file:
        if ".txt" in txt:
            with open(datafile_path + txt,) as txt_file:
                content = txt_file.read()
                content = content.split("\n")
                #### decoding
                new_content = ""
                for data in content:
                    data = data.split(" ")
                    data[0] = str(mainclasses.index(data[0]))
                    #print(data)
                    data = " ".join(data)
                    new_content = new_content + data[0:] +"\n"
                #print (new_content)
            with open(datafile_path+"\\" + txt,"w") as txt_file:
                ####重新寫入decode 後資料
                #print(new_content[:-1])
                txt_file.write(new_content[:-1])
    return "encoded mission completed  : "+ datafile_path


with open('classes.txt','r') as f:
    mainclasses = f.read()
mainclasses = mainclasses.split("\n")
#print(mainclasses)
path = "C:\\Users\\cchhi\\Desktop\\label_change"
path_list = os.listdir(path)
#print(path_list)
path_list = [p for p in path_list if "."not in p]

for my_data in path_list:
    print(decoder(my_data+"\\"))
    print(encoder(my_data+"\\"))

