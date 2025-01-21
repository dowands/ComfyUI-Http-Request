
import requests

class SendHttpRequest:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                        "images": ("IMAGE",),
                              "url": ("STRING", {"multiline": False, "default": "https:yourdomain..."}),
                              "data": ("STRING", {"multiline": False, "default": "{json data}"}),
                             },
               
                }

    RETURN_TYPES = ()
    FUNCTION = "do_request"

    OUTPUT_NODE = True

    CATEGORY = "api/image"

    def do_request(self, images, data, url):
        headers = {
            'Content-Type': 'application/json'
        }
        requests.post(url,data=data,headers=headers)
        return {}

NODE_CLASS_MAPPINGS = {
    "Send Http Request": SendHttpRequest,
}