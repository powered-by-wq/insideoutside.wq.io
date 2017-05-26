define({
    'run': function($page, routeInfo) {
        if (!window.TensorFlow) {
            return;
        }
        var tf = this.initGraph();
            photos = this.app.plugins.photos;
        if (!photos._b64b) {
            photos._b64b = photos.base64toBlob;
        }
        photos.base64toBlob = function(data) {
            $page.find('#show-results').html("Classifying Image...");
            setTimeout(function() {
                tf.classify(data).then(showResult);
            }, 500);
            return photos._b64b(data);
        }
        function showResult(result) {
            var html = "<table>";
            result.forEach(function(score) {
                html += "<tr><th>" + score.title + "</th><td>" + (Math.round(score.confidence * 1000) / 1000) + "</td></tr>";
            });
            html += "</table>";
            $page.find('#show-results').html(html);
            $page.find('[name=results]').val(JSON.stringify({'result': result, 'model': tf.model.id}));
        }
    },
    'initGraph': function() {
        if (this.graph) {
            return this.graph;
        }
        var name = 'final_model_nsideoutside2';
        var url = 'https://tensorflow.wq.io/media/graphs/' + name + '.zip';
        var opts = {
            'label': name,
            'model_path': url + '#graph.pb',
            'label_path': url + '#labels.txt',
            'input_size': 299,
            'image_mean': 128,
            'image_std': 128,
            'input_name': 'Mul',
            'output_name': 'final_result'
        };
        this.graph = new TensorFlow(name, opts);
        return this.graph;
    }
});
