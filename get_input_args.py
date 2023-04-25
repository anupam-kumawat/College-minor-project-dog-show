import argparse

 
def get_input_args():
   

    parser = argparse.ArgumentParser()
    
    
    parser.add_argument('--dir',type=str,default='pet_images/',help='path to folder of images')
    parser.add_argument('--arch',default='vgg', help='Pre-trained model to be used')
    parser.add_argument('--dogfile',default='dognames.txt', help='file conataining all the dog names')
    
  
    return parser.parse_args()
