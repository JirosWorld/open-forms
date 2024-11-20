from django.urls import path

from .views import (
    CaseTypesListView,
    CatalogueListView,
    InformatieObjectTypenListView,
    ProductsListView,
)

app_name = "zgw_apis"

urlpatterns = [
    path("catalogues", CatalogueListView.as_view(), name="catalogue-list"),
    path("case-types", CaseTypesListView.as_view(), name="case-type-list"),
    path("products", ProductsListView.as_view(), name="product-list"),
    path(
        "informatieobjecttypen",
        InformatieObjectTypenListView.as_view(),
        name="iotypen-list",
    ),
]
