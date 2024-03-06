from django.contrib import admin
from .models import SMTP, Bank 


admin.site.register(SMTP)

admin.site.register(Bank)


class ShowWithDeletedAdmin(admin.ModelAdmin):
    """
    Show is_deleted tab too
    """

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.list_display += (
            ["is_deleted"] if not "is_deleted" in self.list_display else []
        )

    def get_queryset(self, request):
        return self.model.objects.with_deleted()
