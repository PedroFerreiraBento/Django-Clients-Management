
from multiprocessing.dummy import current_process
from django.db.models import Count
from django.http import HttpResponse
from django.views.generic import UpdateView, ListView
from django.views.generic.edit import DeleteView
from client.models import Client, RelatedCNPJ, ClientHistory
from client.forms import ClientForm
import datetime
from accounts.views import AuthenticatedView

class ClientDashboardView(ListView, AuthenticatedView):
    model = ClientHistory
    ordering = ['-created_at']
    template_name = "client/client_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_month = datetime.datetime.now().month
        context["client_total"] = []
        context["client_active"] = []
        context["client_inactive"] = []
        for i in range(0,12)[::-1]:
            month_search = current_month - i
            context["client_total"].append(ClientHistory.objects.filter(created_at__month__lte=month_search).values("client_id", "active").annotate(dcount=Count("client_id")).count())
            context["client_active"].append(ClientHistory.objects.filter(created_at__month__lte=month_search, active=True).values("client_id", "active").annotate(dcount=Count("client_id")).count())
            context["client_inactive"].append(ClientHistory.objects.filter(created_at__month__lte=month_search, active=False).values("client_id", "active").annotate(dcount=Count("client_id")).count())
        print(context)
        return context


class ClientListView(ListView, AuthenticatedView):
    model = Client
    ordering = ['created_at']
    paginate_by = 10
    

class ClientDeleteView(DeleteView, AuthenticatedView):
    model = Client
    success_url = "/client/list"
    template_name = "client/client_confirm_delete.html"


class ClientUpdateView(UpdateView, AuthenticatedView):
    model = Client
    template_name_suffix = '_update_form'
    success_url = "/client/list"
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context["client"].__dict__)
        context['related_cnpj'] = RelatedCNPJ.objects.filter(client=self.kwargs["pk"])
        return context