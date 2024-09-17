from django.shortcuts import render,redirect
from .models import Client
from django.shortcuts import get_object_or_404
import datetime


def client_list(request):
    clients = Client.objects.all()
    query = request.GET.get('q')
    if query:
        clients = clients.filter(client_name__icontains=query)  # Search feature
    return render(request, 'client_list.html', {'clients': clients})


def view_client(request, id):
    client = get_object_or_404(Client, id=id)
    return render(request, 'view_client.html', {'client': client})



def add_client(request):
    if request.method == 'POST':
        client_id=request.POST['client_id']
        client_name=request.POST['client_name']
        contact_info=request.POST['contact_info']
        received_date=request.POST['received_date']
        try:
            received_date = datetime.datetime.strptime(received_date, '%Y-%m-%d').date()
        except ValueError:
            # Handle invalid date format
            return render(request, 'error_page.html', {'error': 'Invalid date format'})
        inventory_received=request.POST['inventory_received']
        reported_issues=request.POST['reported_issues'] 
        client_notes=request.POST['client_notes']
        assigned_technician=request.POST['assigned_technician']
        estimated_amount=request.POST['estimated_amount']
        deadline=request.POST['deadline']   
        status=request.POST['status']

        clients=Client.objects.create(
            client_id=client_id,
            client_name=client_name,
            contact_info=contact_info,
            received_date=received_date,
            inventory_received=inventory_received,
            reported_issues=reported_issues,
            client_notes=client_notes,
            assigned_technician=assigned_technician,
            estimated_amount=estimated_amount,
            deadline=deadline,
            status=status
        )
        clients.save()
        return redirect('client_list')

    return render(request, 'add_client.html')

def edit_client(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == 'POST':
        client_name=request.POST.get('client_name')
        contact_info=request.POST.get('contact_info')
        received_date=request.POST.get('received_date')
        try:
            received_date = datetime.datetime.strptime(received_date, '%Y-%m-%d').date()
        except ValueError:
            # Handle invalid date format
            return render(request, 'error_page.html', {'error': 'Invalid date format'})
        inventory_received=request.POST.get('inventory_received')
        reported_issues=request.POST.get('reported_issues')
        client_notes=request.POST.get('client_notes')
        assigned_technician=request.POST.get('assigned_technician')
        estimated_amount=request.POST.get('estimated_amount')
        deadline=request.POST.get('deadline')   
        status=request.POST.get('status')

        Client.objects.filter(id=id).update(
            client_name=client_name,
            contact_info=contact_info,
            received_date=received_date,
            inventory_received=inventory_received,
            reported_issues=reported_issues,
            client_notes=client_notes,
            assigned_technician=assigned_technician,
            estimated_amount=estimated_amount,
            deadline=deadline,
            status=status)

        
        return redirect('client_list')

    return render(request, 'edit_client.html', {'client': client,
        'received_date':client.received_date.strftime('%Y-%m-%d'),'deadline': client.deadline.strftime('%Y-%m-%d')})

def delete_client(request, id):
    client = get_object_or_404(Client, id=id)

    if request.method == 'POST':
        client.delete()
        return redirect('client_list')

    return render(request, 'delete_client.html', {'client': client})
# Create your views here.
