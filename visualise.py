import os.path
from typing import List, Dict

import cv2
import numpy as np

import utils
from enteties import Box


def draw_boxes_on_image(img: np.ndarray, boxes: List[Box], color: tuple = (0, 0, 255)):
    for box in boxes:
        pt1, pt2 = box.get_points_representation()
        cv2.rectangle(img, pt1=pt1, pt2=pt2, color=color, thickness=2)


def process_image(img_path: str, boxes: List[Box]):
    img = cv2.imread(img_path)
    draw_boxes_on_image(img, boxes)


def visualise_gt(gt_dict: Dict[str, List[Box]], images_dir: str, out_dir: str):
    for img_name, boxes in gt_dict.items():
        img_path = os.path.join(images_dir, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue
        draw_boxes_on_image(img, boxes)
        out_path = os.path.join(out_dir, img_name)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        cv2.imwrite(out_path, img)


if __name__ == '__main__':
    config = utils.get_config()
    gt_path = config['DATA']['gt_path']
    images_dir_ = config['DATA']['images_dir']
    out_dir_ = config['DATA']['visualize_dir']

    gt = utils.read_gt(gt_path)
    visualise_gt(gt, images_dir_, out_dir_)
    a = 1
