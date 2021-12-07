import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        address_components, address_type = self.parse(request.query_params['request'])
        return Response({'input_string': request.query_params['request'], 'address_components': address_components, 'address_type': address_type})

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        try:
            parsed = usaddress.tag(address)
            address_components = parsed[0]
            address_type = parsed[1]
            return address_components, address_type
        except usaddress.RepeatedLabelError:
            raise ParseError("Repeated Label Error", 400)
            # return "ERROR", "Repeated Label Error"
        except:
            raise ParseError("Unknown Error", 400)
            # return "ERROR", "Unknown"
