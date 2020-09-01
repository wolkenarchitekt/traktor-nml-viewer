from django.contrib import admin

app_name = "traktor_nml_viewer"
urlpatterns = []


# # Allow passwordless login to Admin
# class AccessUser(object):
#     has_module_perms = has_perm = __getattr__ = lambda s, *a, **kw: True
#
#
# admin.site.has_permission = lambda r: setattr(r, "user", AccessUser()) or True
