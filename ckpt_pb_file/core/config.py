from easydict import EasyDict as edict

__C = edict()

cfg = __C

__C.YOLO = edict()

__C.YOLO.CLASSES = "./core/coco.names"
__C.YOLO.ANCHORS = "./core/coco_anchors.txt"
__C.YOLO.MOVING_AVE_DECAY = 0.9995
__C.YOLO.STRIDES = [8, 16, 32]
__C.YOLO.ANCHOR_PER_SCALE = 3
__C.YOLO.IOU_LOSS_THRESH = 0.5
__C.YOLO.UPSAMPLE_METHOD = "resize"
__C.YOLO.ORIGINAL_WEIGHT = "../saved_model/model.ckpt"
__C.YOLO.DEMO_WEIGHT = "../saved_model_demo/model.ckpt"
