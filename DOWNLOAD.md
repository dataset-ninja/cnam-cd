Dataset **CNAM-CD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/pbddnt3rs2efuuhxwmm2r/cnamcd-DatasetNinja.tar?rlkey=2xhw8ra7z62muo64u8xsba2jz&dl=1)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='CNAM-CD', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://drive.google.com/file/d/1w6tDfE-F4o3Q4KGh1jzzIRpIlIUIXXrx/view?usp=sharing).