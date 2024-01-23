from rest_framework import viewsets
import os
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
class restView (viewsets.ModelViewSet):
    def downloadCv(request):
        pdf_filename = 'cv-page.pdf'
        pdf_path = os.path.join(settings.BASE_DIR, pdf_filename)

        if os.path.exists(pdf_path):
            with open(pdf_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
                return response
        else:
            return HttpResponse(status=404, content="No existe el archivo PDF 'cv.pdf'")