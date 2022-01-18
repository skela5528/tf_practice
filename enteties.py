from numbers import Number
from typing import Tuple

Point = Tuple[Number, Number]


class Box:
    def __init__(self, left: float, top: float, width: float, height: float):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    @classmethod
    def from_json(cls, box_json: dict) -> 'Box':
        box_params = box_json['x'], box_json['y'], box_json['width'], box_json['height']
        assert len(box_params) == 4
        return Box(*box_params)

    def get_points_representation(self) -> Tuple[Point, Point]:
        left_top = int(self.left), int(self.top)
        right = round(self.left + self.width / 2)
        bottom = round(self.top + self.height / 2)
        right_bottom = int(right), int(bottom)
        return left_top, right_bottom
