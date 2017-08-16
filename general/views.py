from django.shortcuts import render, redirect
from django.db import transaction, IntegrityError

# Create your views here.


# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.models import User, Group

from general.forms import *
from .models import * 



def menu_principal(request):
	return render(request, 'menu_principal.html', {})


def solicitud_1(request):
	form = SolicitudForm()

	return render(request, 'solicitud_1.html', {'form': form} )



def solicitud_2(request):
	form = SolicitudForm()

	return render(request, 'solicitud_2.html', {'form': form} )


def solicitud_3(request):
	form = SolicitudForm()

	return render(request, 'solicitud_3.html', {'form': form} )	


def solicitud_4(request):
	form = SolicitudForm()

	return render(request, 'solicitud_4.html', {'form': form} )	



def solicitud_5(request):
	form = SolicitudForm()

	return render(request, 'solicitud_5.html', {'form': form} )	


# ingresar dependientes
def solicitud_6(request):
	form = DependienteForm()

	return render(request, 'solicitud_6.html', {'form': form} )	

def solicitud_7(request):
	form = ReferenciaForm()

	return render(request, 'solicitud_7.html', {'form': form} )	


def solicitud_8(request):
	form = SolicitudForm()

	return render(request, 'solicitud_8.html', {'form': form} )


def solicitud_9(request):
	form = BeneficiarioForm()

	return render(request, 'solicitud_9.html', {'form': form} )		


