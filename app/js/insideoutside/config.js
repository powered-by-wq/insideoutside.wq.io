define(["data/config", "data/templates", "data/version", "module"],
function(config, templates, version, module) {

var overrides = module.config();

config.router = {
    'base_url': ''
};

config.template = {
    'templates': templates,
    'defaults': {
        'version': version,
        'date': function() {
            var date = new Date();
            return (
                date.getFullYear() + '-' +
                (date.getMonth() < 9 ? '0' : '') +
                (date.getMonth() + 1) + '-' +
                (date.getDate() <= 9 ? '0' : '') +
                date.getDate()
	    );
        },
        'is_gps': function() {
            return this.name == 'gps';
        }
    }
};

config.store = {
    'service': config.router.base_url,
    'defaults': {'format': 'json'}
};

config.map = {
    'bounds': [[44.7, -93.6], [45.2, -92.8]]
};

config.outbox = {};

config.transitions = {
    'default': "slide",
    'save': "flip"
};

for (var key in overrides) {
    config[key] = overrides[key];
}

return config;

});
