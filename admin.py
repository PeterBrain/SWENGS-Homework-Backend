from django.contrib import admin
from . import models


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Employee, EmployeeAdmin)
