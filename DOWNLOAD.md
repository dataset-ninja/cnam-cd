Dataset **CNAM-CD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/C/s/QG/wuEs0NexaMnarOWHdBrOyQHeg2JD6MgjiaAMMMqR0TYHL0q1TG45r5CtLPNjCxkL8Kre62n9HMNFnTOGAGVTHpz2aH16SYW6zMpHUfQXCfmVPondJYbClmRsAevJ.tar)

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