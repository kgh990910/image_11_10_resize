from PIL import Image
import os

print("Start Making Farmlearning Thumnail")

raw_path = './raw/'
token_list = os.listdir(raw_path)
out_path = './out/'
print("Total File : " + str(len(token_list)))

if not os.path.exists(out_path):
        os.mkdir(out_path)
        
print("CHECKED OUT DIR")
i = 1
for token in token_list:
    image_path = raw_path + token
    save_path = out_path + token

    image = Image.open(image_path)

    if image.size[0] > image.size[1]:
        tmp_image = Image.new("RGB", (image.size[0], int(image.size[0]/11*10)), (255,255,255))
        tmp_image.paste(image, (0, int((image.size[0]-image.size[1])/22*10)))
    else :
        tmp_image = Image.new("RGB", (image.size[1], int(image.size[1]/11*10)), (255,255,255))
        tmp_image.paste(image, (int((image.size[1]-image.size[0])/2)), 0)
    print("Processing : " + str(i) + "/" + str(len(token_list)))

    i+=1

    tmp_image.save(save_path)
    
print("Done")
