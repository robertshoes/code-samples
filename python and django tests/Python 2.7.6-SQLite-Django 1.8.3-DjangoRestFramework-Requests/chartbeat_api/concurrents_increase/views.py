from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from concurrents_increase.models import Page, Domain
from concurrents_increase.serializers import PageSerializer, DomainSerializer, PageSerializerIncrease




@csrf_exempt
@api_view(['GET', 'POST'])
def create_domain(request):
    """
    Show all domains created and save new ones
    """
    if request.method == 'GET':
        # Retrieves all the existing domains
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Handles the creation of a new domain or host
        serializer = DomainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def concurrent_visitors_by_domain(request):
    """
    Will get the visitors by hostname
    Statistics about each visited page
    Also, if the change parameter is passed with True
    will show the difference between new visitors and previous
    visitors.
    """
    if request.method == 'GET':
        hostname = request.GET.get('host')
        change = request.GET.get('change')
        if hostname:
            try:
                # Finding the host first before looking for its pages
                host = Domain.objects.filter(domain_name__icontains=hostname)
                if host:
                    # This is to avoid an IndexError exception
                    host = host[0]
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            except Domain.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            try:
                # Get the pages for the hostname
                if change == 'True':
                    page = Page.objects.filter(domain_id=host, change__gt=0).order_by('-change')[:100]
                    # Serialize the data
                    serializer = PageSerializerIncrease(page, many=True)
                else:
                    # This is the normal view of the API.  Showing all the fields
                    # They are ordered by visitors and I retrieve the first hundred
                    # for a particular domain or hostname
                    page = Page.objects.filter(domain_id=host).order_by('-visitors')[:100]
                    # Serialize the data
                    serializer = PageSerializer(page, many=True)
            except Page.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            # Return the response in JSON
            return Response(serializer.data)
        else:
            # no host to look for
            return HttpResponse("Need to pass a host variable like api?host='something.com'")
