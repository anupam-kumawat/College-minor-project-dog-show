from classifier import classifier 
import os.path
 
def classify_images(images_dir, results_dic, model):

    for key in results_dic :
        
        model_label = classifier(os.path.join(images_dir,key),model)
        
        model_label = model_label.lower()
        model_label = model_label.strip()
        
        truth = results_dic[key][0]
        
        if truth in model_label :
            
            results_dic[key].extend([model_label,int(True)])
            
        else :
            
            results_dic[key].extend([model_label,int(False)])
        
        
     