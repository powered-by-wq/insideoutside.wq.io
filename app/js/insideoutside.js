requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        'insideoutside': '../insideoutside',
        'data': '../data/'
    }
});

requirejs(['insideoutside/main']);
