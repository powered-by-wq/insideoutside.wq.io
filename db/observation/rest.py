from wq.db import rest
from .models import Observation


rest.router.register_model(
    Observation,
    fields="__all__",
    locate=True,
    map=[{
        'mode': 'list',
        'autoLayers': True,
        'layers': [],
    }, {
        'mode': 'detail',
        'autoLayers': True,
        'layers': [],
    }, {
        'mode': 'edit',
        'layers': [{
            'type': 'geojson',
            'name': 'Location',
            'url': 'reports/{{id}}.geojson',
        }],
    }],
)
