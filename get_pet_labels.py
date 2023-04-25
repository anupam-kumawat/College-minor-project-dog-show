from os import listdir


def get_pet_labels(image_dir):
    
   
    
    filename_list = listdir(image_dir)
    
    results_dic = dict()
    
    
    
    for i in range(0,len(filename_list),1):
      
      if(filename_list[i][0] != "."):
        pet_label = ""
        
        low_label = [item.lower() for item in filename_list]
        word_label = [item.split("_") for item in low_label]
            
        for j in range(0,len(word_label[i]),1):
          if(word_label[i][j].isalpha()):
            pet_label += word_label[i][j] + " "
                    
        if filename_list[i] not in results_dic:
          pet_label = pet_label.strip()
          results_dic[filename_list[i]] = [pet_label]
              
        else:
          print("** Warning: Duplicate files exist in directory:",filename_list[i])
                                      
    return results_dic
