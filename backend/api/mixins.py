from .permissions import IsStaffEditorPermissions
from rest_framework import permissions


class StaffEditorMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
