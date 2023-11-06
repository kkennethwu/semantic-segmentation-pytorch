import os
import cv2
import json

def odgt(img_path):
    seg_path = img_path.replace('images','annotations')
    seg_path = seg_path.replace('.jpg','.png')
    
    if os.path.exists(seg_path):
        img = cv2.imread(img_path)
        h, w, _ = img.shape

        odgt_dic = {}
        odgt_dic["fpath_img"] = img_path
        odgt_dic["fpath_segm"] = seg_path
        odgt_dic["width"] = h
        odgt_dic["height"] = w
        return odgt_dic
    else:
        # print('the corresponded annotation does not exist')
        # print(img_path)
        return None


if __name__ == "__main__":
    # modes = ['train','val']
    # saves = ['dataset2_training.odgt', 'dataset2_validation.odgt'] # customized
    save = 'collected_data_floor1.odgt'
    
    dir_path = f"../../hw1/data_collection/first_floor/rgb/"
    img_list = os.listdir(dir_path)
    img_list.sort()
    img_list = [os.path.join(dir_path, img) for img in img_list]

    with open(f'data/{save}', mode='wt', encoding='utf-8') as myodgt:
        for i, img in enumerate(img_list):
            a_odgt = odgt(img)
            if a_odgt is not None:
                myodgt.write(f'{json.dumps(a_odgt)}\n')