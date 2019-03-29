from django.urls import path

from . import views

urlpatterns = [
    path('portal/home/', views.index, name='home'),
    path('portal/tools/', views.tools, name='tools'),
    path('portal/tools/details/<int:id>', views.details, name="details"),
    path('portal/tools/add/<int:id>', views.add, name="add"),
    path('portal/pipelines/', views.pipelines, name="pipelines"),
    path('portal/pipelines/details/<int:id>', views.pipelineDetails, name="pipeline_details"),
    path('portal/pipelines/create', views.createPipeline, name="create_pipeline"),
    path('portal/tools/private/<int:id>', views.privateDetails, name="private_details"),
    path('portal/refine/findability/<int:id>', views.refineFindability, name="refine_findability"),
    path('portal/refine/accessibility/<int:id>', views.refineAccessibility, name="refine_accessibility"),
    path('portal/refine/interoperability/<int:id>', views.refineInteroperability, name="refine_interoperability")
]
