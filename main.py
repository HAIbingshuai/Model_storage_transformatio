# yolov3.weights转ckpt的cmd命令：
# python convert_weights.py --class_names coco.names --data_format NHWC --weights_file yolov3.weights

# !!!!   生成的ckpt并不能直接用与tensorflow与训练模型和从ckpt转成pb文件（暂时不知为何），需要用tensorflow版本yolo中convert_weight.py(ckpt_pb_file目录下)再次跑起来，生成demo版本的ckpt


# yolov3.weights转ckpt的cmd命令：
# python convert_weights_pb.py --class_names coco.names --data_format NHWC --weights_file yolov3.weights


# ckpt转pb的cmd命令：
# 利用tensorflow版本下的进行转换ckpt（demo版本）执行freeze_graph.py(目录下)
