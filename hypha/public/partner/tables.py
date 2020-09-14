import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from .models import Investment


class InvestmentTable(tables.Table):
    """Table for listing investments."""
    partner = tables.Column(verbose_name='Partner name', linkify=True)
    name = tables.Column(verbose_name='Investment')
    year = tables.Column(verbose_name='Year')
    status = tables.Column(accessor='partner__status', verbose_name='Status')
    amount_committed = tables.Column(verbose_name='Amount committed (US$)')

    class Meta:
        model = Investment
        order_by = ('-updated_at',)
        fields = ('partner', 'name', 'year', 'status', 'amount_committed')
        template_name = 'partner/table.html'
        attrs = {'class': 'all-investments-table'}
        empty_text = _('No investments available')