The authors of the **CNAM-CD** dataset recognized the formidable challenges in detecting changes within urban areas, marked by intricate features, rapid alterations, and human-induced interferences from different Chinese new national areas. They observed that the conventional binary change detection (BCD) methods used for urban change detection have limitations as cities become more complex. These BCD techniques often rely on convolutional operations, which struggle to capture comprehensive contextual and semantic information. This is the first version publicly available, where ***A*** is the image at the previous time, ***B*** is the image at the later time and Label is the corresponding label.

To address these issues, the authors introduced SIGNet, a Siamese graph convolutional network designed to enhance the accuracy of urban multi-class change detection (MCD) tasks. The experimental results demonstrated SIGNet's superior performance in capturing contextual relationships and semantic correlations, establishing it as a state-of-the-art solution for MCD tasks.

<img src="https://github.com/supervisely/supervisely/assets/78355358/7c178c9b-cf6f-48d6-91cf-46888ba7fa69" alt="image" width="800">

Recognizing the scarcity of pixel-level datasets in the MCD domain, the authors introduced a new dataset named CNAM-CD, which offers extensive labeling for multi-class change detection. CNAM-CD comprises 2508 pairs of high-resolution images and serves as a valuable resource for evaluating models, particularly when compared to traditional BCD approaches.

The authors highlighted the critical importance of accurately identifying changes in land use and land cover (LULC) within cities, as it plays a pivotal role in various fields, including urban expansion, economic development, and sociology.

For the CNAM-CD dataset, the authors selected 12 State-level New Areas (SLNAs) in China, regions known for their dynamic and rapid changes in the urban environment. These areas were chosen to ensure balanced categories for constructing the dataset, resulting in 2503 pairs of high-resolution images captured between 2013 and 2022.

The authors explained that the dataset was derived from Google Earth level 19 images, offering high resolution and wide coverage of SLNAs.  Due to variations in image appearance, including hue, saturation, contrast, and brightness, between bi-temporal images, the dataset poses a significant challenge for change detection models.

CNAM-CD featured five distinct categories: *bare ground*, *vegetation*, *water ground*, *impervious surfaces* (including buildings, roads, parking lots, and squares), and *other* (comprising clouds, hard shadows, and clutter). These categories align with previous urban-related research.

The dataset's categorical distribution was discussed, highlighting that bare land constituted the largest category of change (34.12% of the change area), while water bodies represented the smallest category (7.83%). To ensure dataset balance, areas with excessive water bodies were excluded from data source selection, and each SLNA selected for the dataset encompassed all categories.
<img src="https://github.com/supervisely/supervisely/assets/78355358/7543e859-d795-427d-97df-1323f0e2acb6" alt="image" width="800">

<img src="https://github.com/supervisely/supervisely/assets/78355358/3791cd72-48c9-49b8-93c8-fde40a939d0c" alt="image" width="800">

