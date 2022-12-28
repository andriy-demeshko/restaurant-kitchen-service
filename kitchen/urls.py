from django.urls import path
from kitchen.views import (
    index,
    DishListView,
    DishDetailView,
    # DishCreateView,
    # DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    # CookCreateView,
    # CookExperienceUpdateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    # toggle_assign_to_car,
)


urlpatterns = [
    path("", index, name="index"),

    path("dishes-types/", DishTypeListView.as_view(), name="dish-type-list"),
    # path(
    #     "manufacturers/create/",
    #     ManufacturerCreateView.as_view(),
    #     name="manufacturer-create",
    # ),
    # path(
    #     "manufacturers/<int:pk>/update/",
    #     ManufacturerUpdateView.as_view(),
    #     name="manufacturer-update",
    # ),
    # path(
    #     "manufacturers/<int:pk>/delete/",
    #     ManufacturerDeleteView.as_view(),
    #     name="manufacturer-delete",
    # ),

    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    # path("cars/create/", CarCreateView.as_view(), name="car-create"),
    # path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    # path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    # path("cars/<int:pk>/toggle-assign/", toggle_assign_to_car, name="toggle-car-assign"),

    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    # path("drivers/create/", DriverCreateView.as_view(), name="driver-create"),
    # path(
    #     "drivers/<int:pk>/update/",
    #     DriverLicenseUpdateView.as_view(),
    #     name="driver-update",
    # ),
    # path("drivers/<int:pk>/delete/", DriverDeleteView.as_view(), name="driver-delete"),
]

app_name = "kitchen"
