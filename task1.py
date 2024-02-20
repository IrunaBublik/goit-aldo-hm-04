def get_cats_info(path):
    dictionary_cats= []
    try:

        with open(path, 'r',encoding='utf-8') as file:
            for line in file.readlines():
                line = line.strip().split(',')
                dictionary_cats.append({"id":line[0], "name":line[1], "age":(line[2])})
            
   
    except FileNotFoundError: 
        print("Не вдалося знайти файл.")
    return dictionary_cats
            
     
dictionary_cats=get_cats_info("cat_info.txt") 
print(dictionary_cats)

