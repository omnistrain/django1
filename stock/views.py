from django.shortcuts import render, redirect
from django.http import HttpResponse
from stock.models import Groupe, Formation
from stock.forms import ContactForm, GroupeForm, FormationForm
from django.core.mail import send_mail

# Create your views here.


def groupe_list(request):

    groupes = Groupe.objects.all()

    return render(request, 'stock/groupe_liste.html', {'groupes': groupes})

def groupe_detail(request, id):
    groupe = Groupe.objects.get(id=id)
    return render(request,'stock/groupe_detail.html', {'groupe': groupe})


def formation_list(request):

    formations = Formation.objects.all()

    return render(request, 'stock/formation_liste.html', {'formations': formations})

def formation_detail(request, id):
    formation = Formation.objects.get(id=id)
    return render(request,'stock/formation_detail.html', {'formation': formation})

def contact(request):
    if(request.method == 'POST'):
        form = ContactForm(request.POST)
        if(form.is_valid()):
            send_mail(
                subject=f'Message depuis le Front {form.cleaned_data["name"] or "John Doe"}',
                message = form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['hebrard.freddy@gmail.com']
            )
            return redirect('email-ok')
    else:
        form = ContactForm()
    return render(request, 'stock/contact.html', {'form': form })


def email_ok(request):
    return render(request,'stock/contact_ok.html')

def groupe_add(request):
    if(request.method == 'POST'):
        form = GroupeForm(request.POST)
        if form.is_valid():
            groupe = form.save()

            return redirect('groupe-detail', groupe.id)
    else:
        form = GroupeForm()
    return render(request, 'stock/groupe_add.html', {'form': form})


def formation_add(request):
    if(request.method == 'POST'):
        form = FormationForm(request.POST)
        if form.is_valid():
            formation = form.save()

            return redirect('formation-detail', formation.id)
    else:
        form = FormationForm()
    
    return render(request, 'stock/formation_add.html', {'form': form})


def groupe_update(request, id):
    groupe = Groupe.objects.get(id=id)

    if request.method == 'POST':
        form = GroupeForm(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            return redirect('groupe-detail', id)
    else:
        form = GroupeForm(instance=groupe)
    
    return render(request, 'stock/groupe_update.html',{'form': form})


def groupe_delete(request, id):
    groupe = Groupe.objects.get(id=id)

    if request.method == 'POST':
        groupe.delete()
        return redirect('groupe-list')
 
    
    return render(request, 'stock/groupe_delete.html',{'groupe': groupe})





    return render(request, 'stock/groupe_delete.html',{'groupe': groupe})
