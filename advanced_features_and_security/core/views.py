from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_HTTPS

@require_HTTPS
@permission_required('core.can_view', raise_exception=True)
def protected_view(request):
    return render(request, 'core/protected.html')

@login_required
def profile_view(request):
    return render(request, 'core/profile.html', {'user': request.user})
