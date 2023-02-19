import numpy as np

def xyxy2cxcywh(boxes:np.ndarray)-> np.ndarray:
    assert boxes.shape[-1] == 4 , "The number of dimension must be 4."
    assert len(boxes.shape) == 2, "2d" 
    boxes[:, 2] = boxes[:, 0] - boxes[:, 2]     # width
    boxes[:, 3] = boxes[:, 3] - boxes[:, 1]     # hegiht
    boxes[:, 0] = boxes[:, 0] + (boxes[:, 2] / 2.0) # center_x
    boxes[:, 1] = boxes[:, 1] + (boxes[:, 3] / 2.0) # center_y
    return boxes

def cxcywh2xyxy(boxes:np.ndarray)-> np.ndarray:
    assert boxes.shape[-1] == 4 , "The number of dimension must be 4."
    assert len(boxes.shape) == 2, "2d" 
    boxes[:, 0] = boxes[0] - (boxes[:, 2] / 2.0)
    boxes[:, 1] = boxes[1] - (boxes[:, 3] / 2.0)
    boxes[:, 2] = boxes[0] + boxes[:, 2]
    boxes[:, 3] = boxes[1] + boxes[:, 3]
    return boxes

class BoxTrans:
    def __init__(self, boxes:np.ndarray):
        self.boxes = boxes
        self.boxes_shape = self.boxes.shape
        if len(self.boxes_shape) == 2:
            self.boxes_shape= [1,
                self.boxes_shape[0], 
                self.boxes_shape[1]]
    def _bwh2wh(self):
        return self.boxes.reshape(-1, 4)
    
    def _wh2bwh(self):
        b, w, h = self.boxes_shape
        return self.boxes.reshape(b, w, h)
    
    def trans(self, mode="wh"):
        if mode =="wh":
            self._bwh2wh()