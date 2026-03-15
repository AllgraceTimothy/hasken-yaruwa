from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Support, ResourceAllocation, ImpactMetric


def impact_page(request):
    # IMPACT METRICES
    metrics = ImpactMetric.objects.all().order_by("order")

    # TOTAL SUPPORT RECEIVED
    total_support_received = Support.objects.aggregate(
        total=Sum("amount")
    )["total"] or 0


    # TOTAL ALLOCATIONS MADE
    total_allocations = ResourceAllocation.objects.count()


    # TOTAL VALUE DISTRIBUTED
    total_value_distributed = ResourceAllocation.objects.aggregate(
        total=Sum("value")
    )["total"] or 0


    # UNIQUE STUDENTS SUPPORTED
    students_supported = ResourceAllocation.objects.values(
        "student"
    ).distinct().count()


    # RESOURCE DISTRIBUTION BY TYPE
    resource_distribution = ResourceAllocation.objects.values(
        "resource_type"
    ).annotate(
        count=Count("id")
    ).order_by("-count")


    # VALUE DISTRIBUTION BY TYPE
    value_distribution = ResourceAllocation.objects.values(
        "resource_type"
    ).annotate(
        total_value=Sum("value")
    ).order_by("-total_value")


    # MOST RECENT SUPPORT ENTRIES
    recent_support = Support.objects.order_by(
        "-date_received"
    )[:5]


    # MOST RECENT ALLOCATIONS
    recent_allocations = ResourceAllocation.objects.select_related(
        "student",
        "support_source"
    ).order_by("-date_allocated")[:10]


    context = {
        "metrics": metrics,
        "total_support_received": total_support_received,
        "total_allocations": total_allocations,
        "total_value_distributed": total_value_distributed,
        "students_supported": students_supported,
        "resource_distribution": resource_distribution,
        "value_distribution": value_distribution,
        "recent_support": recent_support,
        "recent_allocations": recent_allocations,
    }

    return render(request, "support/impact.html", context)