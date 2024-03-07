
from rest_framework.renderers import JSONRenderer
from djangorestframework_camel_case.render import CamelCaseJSONRenderer

class CustomResponseRenderer(CamelCaseJSONRenderer):
    def render(
        self,
        data,
        accepted_media_type=None,
        renderer_context=None,    
    ):
        status_code =renderer_context["response"].status_code 
        
        if (200 <= status_code <= 203) or (205 <= status_code < 300):
            message="Successfully returned data."
            show_msg =True
            
            try:
                message =data.pop("message")
                show_msg = data.pop("show_msg")
            except:
                pass
            if len(data) == 1 and type(data) == dict:
                if "data" in data.keys():
                    data = data.pop("data") or None
          
            data = {"data": data or None}
            if show_msg:
                data["message"]=message
        return super().render(data, accepted_media_type, renderer_context)



