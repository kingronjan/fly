$.ajaxSetup({
            data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
        });