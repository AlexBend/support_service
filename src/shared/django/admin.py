from django.contrib.admin import ModelAdmin

# _FIELDS = ["created_at", "updated_at"]


class TimeStampReadonlyAdmin(ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["created_at", "updated_at"]
