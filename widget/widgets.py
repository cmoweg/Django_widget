from django import forms


class CounterTextInput(forms.TextInput):
    template_name = "widget/counter_text.html"


from django import forms


# 생략

class starWidget(forms.TextInput):
    input_type = 'rating'
    template_name = "widget/star_rate.html"

    class Media:
        css = {
            'all': [
                'widget/rateit/rateit.css',
            ],
        }
        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
            'widget/rateit/jquery.rateit.min.js',
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs.update({
            'min': 0,
            'max': 5,
            'step': 1,
        })
        return attrs


class AutoCompleteWidget(forms.Select):
    template_name = 'widget/autocomplete_select.html'

    class Media:
        css = {
            'all': [
                "//cdnjs.cloudflare.com/ajax/libs/select2/4.0.8/css/select2.min.css",
            ],
        }
        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
            "//cdnjs.cloudflare.com/ajax/libs/select2/4.0.8/js/select2.min.js",
        ]

    def build_attrs(self, *args, **kwargs):
        context = super().build_attrs(*args, **kwargs)
        context['style'] = 'min-width:200px;'
        return context
