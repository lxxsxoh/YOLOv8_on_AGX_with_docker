# YOLOv8_on_AGX_with_docker

1.install
   --------
  <pre>
    t=ultralytics/ultralytics:latest-jetson && sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
  </pre>
  (1) t=ultralytics/ultralytics:latest-jetson: t를 ultralytics~로 지정한다. (image)
  
  (2) sudo docker pull $t: docker에 t라는 image를 pull한다.
  
  (3) sudo docker run -it -ipc=host --runtime=nvidia $t: 컨테이너를 실행한다.

2.5개의 task에 대해 YOLOv8 inference time 측정
-------------------------------------------
   (1) detection
   <pre>
     detection.py > detect.txt
   </pre>

  (2) classify
  <pre>
    classification.py > classify.txt
  </pre>

  (3) segmentation
  <pre>
    segment.py > segment.txt
  </pre> 

  (4) obb
  <pre>
    obb.py > obb.txt
  </pre>

  (5) pose
  <pre>
    pose.py > pose.txt
  </pre>

1000번 반복에 대한 총 inference time
-----------------
![image](https://github.com/lxxsxoh/YOLOv8_on_AGX_with_docker/assets/136955006/e2fa359f-b1d5-4fe6-a752-58159841cd57)


![image](https://github.com/lxxsxoh/YOLOv8_on_AGX_with_docker/assets/136955006/02f89d78-0695-4d3c-9035-4a7ec9be59c3)

  
