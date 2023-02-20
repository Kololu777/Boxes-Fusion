import numpy as np

def xyxy2cxcywh(boxes:np.ndarray)-> np.ndarray:
    assert boxes.shape[-1] == 4 , "The number of dimension must be 4."
    assert len(boxes.shape) == 2, "2d" 
    boxes[:, 2] = boxes[:, 0] - boxes[:, 2]         # width
    boxes[:, 3] = boxes[:, 3] - boxes[:, 1]         # hegiht
    boxes[:, 0] = boxes[:, 0] + (boxes[:, 2] / 2.0) # center_x
    boxes[:, 1] = boxes[:, 1] + (boxes[:, 3] / 2.0) # center_y
    return boxes

def cxcywh2xyxy(boxes:np.ndarray)-> np.ndarray:
    assert boxes.shape[-1] == 4 , "The number of dimension must be 4."
    assert len(boxes.shape) == 2, "2d" 
    boxes[:, 0] = boxes[0] - (boxes[:, 2] / 2.0) # x_min
    boxes[:, 1] = boxes[1] - (boxes[:, 3] / 2.0) # y_min
    boxes[:, 2] = boxes[0] + boxes[:, 2]         # x_max
    boxes[:, 3] = boxes[1] + boxes[:, 3]         # y_max 
    return boxes

def xyxy2n(boxes:np.ndarray, width:float, height:float)-> np.ndarray:
    assert boxes.shape[-1] == 4
    assert len(boxes.shape) == 2
    return xyscaling(boxes, (1/width), (1/height))
    
def cxcywh2n(boxes:np.ndarray, width:float, height:float)->np.ndarray:
    assert boxes.shape[-1] == 4
    assert len(boxes.shape) == 2
    return xyscaling(boxes, (1/width), (1/height))
    
def n2xyxy(boxes:np.ndarray, width:float, height:float)->np.ndarray:
    assert boxes.shape[-1] == 4
    assert len(boxes.shape) == 2
    return xyscaling(boxes, width, height)

def n2cxcy(boxes:np.ndarray, width:float, height:float)->np.ndarray:
    assert boxes.shape[-1] == 4
    assert len(boxes.shape) == 2
    return xyscaling(boxes, width, height)

def xyscaling(boxes:np.ndarray, width_scale:float, height_scale:float)->np.ndarray:
    boxes[:, 0] = boxes[:, 0] * width_scale
    boxes[:, 1] = boxes[:, 1] * height_scale
    boxes[:, 2] = boxes[:, 2] * width_scale
    boxes[:, 3] = boxes[:, 3] * height_scale
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