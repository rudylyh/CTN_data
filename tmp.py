import os
import cv2
import json
import shutil
import numpy as np

def get_hip_data():
    img_json = json.load(open('/WD1/paii_internship/workspace/cvpr/hip_exp/100train_200test_dataset.json'))
    img_list = img_json['train'] + img_json['test']
    src_dir = img_json['root_dir']
    dst_dir = '/WD1/paii_internship/workspace/cvpr/CTN_data/hip_data'
    for i, img_name in enumerate(img_list):
        print(i, img_name)
        gt_ctr_json = json.load(open(os.path.join(src_dir, img_name, img_name+'_gt.json')))
        gt_ctr = np.asarray(gt_ctr_json['gt_ctr']).astype(np.int)
        ori_img = cv2.imread(os.path.join(src_dir, img_name, img_name+'.png'), 0)
        mask = np.zeros(ori_img.shape, np.uint8)
        mask = cv2.fillPoly(mask, [gt_ctr], 255)
        tmp_dst_dir = os.path.join(dst_dir, img_name)
        os.mkdir(tmp_dst_dir)
        shutil.copyfile(os.path.join(src_dir, img_name, img_name+'_gt.json'), os.path.join(dst_dir, img_name, 'gt_ctr.json'))
        cv2.imwrite(os.path.join(dst_dir, img_name, 'gt_mask.png'), mask)
        # cv2.imshow("img", mask)
        # cv2.waitKey()
        # exit()


def get_knee_data():
    img_json = json.load(open('/WD1/paii_internship/workspace/cvpr/knee_exp/dataset_1102.json'))
    img_list = img_json['train'] + img_json['test']
    src_dir = img_json['root_dir']
    dst_dir = '/WD1/paii_internship/workspace/cvpr/CTN_data/knee_data'
    for i, img_name in enumerate(img_list):
        print(i, img_name)
        mask = cv2.imread(os.path.join(src_dir, img_name, img_name+'_mask.png'), 0)
        mask[mask==1] = 128
        mask[mask==2] = 255
        tmp_dst_dir = os.path.join(dst_dir, img_name)
        os.mkdir(tmp_dst_dir)
        shutil.copyfile(os.path.join(src_dir, img_name, img_name+'_gt.json'), os.path.join(dst_dir, img_name, 'gt_ctr.json'))
        cv2.imwrite(os.path.join(dst_dir, img_name, 'gt_mask.png'), mask)
        # cv2.imshow("img", mask)
        # cv2.waitKey()
        # exit()


if __name__ == '__main__':
    get_knee_data()
