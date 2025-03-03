from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission,
    ]
    

class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False
    def get_queryset(self, *args, **kwargs):
         user = self.request.user
         lookup_data = {}
         lookup_data[self.user_field] = user
         print(lookup_data)
         qs = super().get_queryset(*args, **kwargs)
         if self.allow_staff_view and user.is_staff:
             return qs
         print(qs)

         return qs.filter(**lookup_data)