# Model_storage_transformatio
checkpoint and weights and pb，reciprocal transformation



darknet下yolo_v3版本weights转化成ckpt、pb格式：

# Model_storage_transformatio主目录下进行
yolov3.weights转ckpt的cmd命令：
python convert_weights.py --class_names coco.names --data_format NHWC --weights_file yolov3.weights

yolov3.weights转ckpt的cmd命令：
python convert_weights_pb.py --class_names coco.names --data_format NHWC --weights_file yolov3.weights



tensorflow用的yolo_v3版本中需要checkpoint（再次）及pb格式：
# Model_storage_transformatio\ckpt_pb_file目录下进行
前提：运行convert_weight.py，生成demo版本的ckpt
ckpt转pb的cmd命令：
利用tensorflow版本下的进行转换ckpt（demo版本）
执行freeze_graph.py(目录下)

