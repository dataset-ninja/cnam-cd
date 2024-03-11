**CNAM-CD: A Multi-Class Change Detection Dataset** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the geospatial domain, and in the urban planning industry. 

The dataset consists of 5016 images with 60346 labeled objects belonging to 6 different classes including *background*, *bare ground*, *impervious surface*, and other: *vegetation*, *other*, and *water bodies*.

Images in the CNAM-CD dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 4 (0% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Alternatively, the dataset could be split into 2512 groups set by ***img_id***. Every group has 2 images: ***A*** (before) and ***B*** (after). Ground truth masks assigned to ***B***. The dataset was released in 2023 by the <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">Xinjiang University, China</span>.

<img src="https://github.com/dataset-ninja/cnam-cd/raw/main/visualizations/poster.png">
