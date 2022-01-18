import json
import os
from typing import Dict, List

import yaml

from enteties import Box

CONFIG_PATH = 'config.yaml'


def get_config(config_path: str = CONFIG_PATH) -> dict:
    with open(config_path) as stream:
        config = yaml.safe_load(stream)
    return config


def decode_image_name(image_id: str, img_ext: str = 'jpg') -> str:
    video, img = image_id.split('-')
    image_name = f'video_{video}{os.path.sep}{img}.{img_ext}'
    return image_name


def encode_image_name():
    ...


def read_gt(gt_path: str) -> Dict[str, List[Box]]:
    gt = dict()
    with open(gt_path) as stream:
        next(stream)
        for line in stream.readlines():
            line_data = line.strip().split(',')
            image_name = decode_image_name(line_data[4])
            try:
                annotations_start = line.index('"[{')
                annotations = line[annotations_start:]
                annotations = annotations.replace('"', '').strip()
                annotations = annotations.replace('\'', '"')
                annotations = json.loads(annotations)
            except ValueError:
                annotations = []

            boxes = [Box.from_json(a) for a in annotations]
            gt[image_name] = boxes
    return gt
