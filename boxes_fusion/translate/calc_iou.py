import numpy as np

def calc_iou(dets:np.ndarray, boxes:np.ndarray):
    """
    dets: xyxy (1, 4)
    boxes: xyxy(N, 4)
    """
    x_min = np.maximum(dets[0], boxes[:, 0])
    y_min = np.maximum(dets[1], boxes[:, 1])
    x_max = np.minimum(dets[2], boxes[:, 2])
    y_max = np.minimum(dets[3], boxes[:, 3])
    
    w = np.maximum(0.0, x_max - x_min)
    h = np.maximum(0.0, y_max - y_min)
    # a ^ b / a v b = inter / area_a + area_b - inter
    
    inter_area = w * h
    area_dets = calc_area(dets)
    area_boxes = calc_area(boxes)
    iou = inter_area / (area_dets + area_boxes - inter_area)
    return iou
    
def calc_area(boxes:np.ndarray):
    result_boxes = boxes.copy()
    result_boxes[:, 0] = np.min(boxes[:, [0, 2]], axis=1)
    result_boxes[:, 1] = np.min(boxes[:, [1, 3]], axis=1)
    result_boxes[:, 2] = np.max(boxes[:, [0, 2]], axis=1)
    result_boxes[:, 3] = np.max(boxes[:, [1, 3]], axis=1)
    
    area = (result_boxes[:, 2] - result_boxes[:, 0]) * \
           (result_boxes[:, 3] - result_boxes[:, 1])
    return area

    
if __name__ == "__main__":
    dets_list = [
        [0.00, 0.41, 0.81, 0.92]
    ]
    
    boxes_list = [
    [0.00, 0.51, 0.81, 0.91],
    [0.10, 0.31, 0.71, 0.61],
    [0.01, 0.32, 0.83, 0.93],
    [0.02, 0.53, 0.11, 0.94],
    [0.03, 0.24, 0.12, 0.35],
    ]
    a = np.array(dets_list)
    b = np.array(boxes_list)
    print(calc_iou(a, b))