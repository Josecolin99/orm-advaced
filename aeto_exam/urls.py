# Django
from django.urls import path
from aeto_exam import colin as compare

# Django
from django.urls import path
from aeto_exam.views import enano, siento_que_olvide_a_alguien, zorra, colin

gran_colin = [
    path(
        route="compare/Caso1LibrosConEditorial",
        view=compare.Caso1LibrosConEditorial.as_view(),
    ),
    path(
        route="compare/Caso2CalificacionesConLibro",
        view=compare.Caso2CalificacionesConLibro.as_view(),
    ),
    path(
        route="compare/Caso3AutoresConLibros",
        view=compare.Caso3AutoresConLibros.as_view(),
    ),
    path(
        route="compare/Caso4ValuesEjemplo",
        view=compare.Caso4ValuesEjemplo.as_view(),
    ),
    path(
        route="compare/Caso5OnlyEjemplo",
        view=compare.Caso5OnlyEjemplo.as_view(),
    ),
    path(
        route="compare/Caso6DeferEjemplo",
        view=compare.Caso6DeferEjemplo.as_view(),
    ),
    path(
        route="compare/Caso7AutoresLibrosEditorial",
        view=compare.Caso7AutoresLibrosEditorial.as_view(),
    ),
]


los_demas = [
    # =====================
    # Rutas para enano.py
    # =====================
    path("enano/Caso1LibrosConEditorial", enano.Caso1LibrosConEditorial.as_view()),
    path("enano/Caso2CalificacionesConLibro", enano.Caso2CalificacionesConLibro.as_view()),
    path("enano/Caso3AutoresConLibros", enano.Caso3AutoresConLibros.as_view()),
    path("enano/Caso4ValuesEjemplo", enano.Caso4ValuesEjemplo.as_view()),
    path("enano/Caso5OnlyEjemplo", enano.Caso5OnlyEjemplo.as_view()),
    path("enano/Caso6DeferEjemplo", enano.Caso6DeferEjemplo.as_view()),
    path("enano/Caso7AutoresLibrosEditorial", enano.Caso7AutoresLibrosEditorial.as_view()),

    # ===================================
    # Rutas para siento_que_olvide_a_alguien.py
    # ===================================
    path("alguien/Caso1LibrosConEditorial", siento_que_olvide_a_alguien.Caso1LibrosConEditorial.as_view()),
    path("alguien/Caso2CalificacionesConLibro", siento_que_olvide_a_alguien.Caso2CalificacionesConLibro.as_view()),
    path("alguien/Caso3AutoresConLibros", siento_que_olvide_a_alguien.Caso3AutoresConLibros.as_view()),
    path("alguien/Caso4ValuesEjemplo", siento_que_olvide_a_alguien.Caso4ValuesEjemplo.as_view()),
    path("alguien/Caso5OnlyEjemplo", siento_que_olvide_a_alguien.Caso5OnlyEjemplo.as_view()),
    path("alguien/Caso6DeferEjemplo", siento_que_olvide_a_alguien.Caso6DeferEjemplo.as_view()),
    path("alguien/Caso7AutoresLibrosEditorial", siento_que_olvide_a_alguien.Caso7AutoresLibrosEditorial.as_view()),

    # =====================
    # Rutas para zorra.py
    # =====================
    path("zorra/Caso1LibrosConEditorial", zorra.Caso1LibrosConEditorial.as_view()),
    path("zorra/Caso2CalificacionesConLibro", zorra.Caso2CalificacionesConLibro.as_view()),
    path("zorra/Caso3AutoresConLibros", zorra.Caso3AutoresConLibros.as_view()),
    path("zorra/Caso4ValuesEjemplo", zorra.Caso4ValuesEjemplo.as_view()),
    path("zorra/Caso5OnlyEjemplo", zorra.Caso5OnlyEjemplo.as_view()),
    path("zorra/Caso6DeferEjemplo", zorra.Caso6DeferEjemplo.as_view()),
    path("zorra/Caso7AutoresLibrosEditorial", zorra.Caso7AutoresLibrosEditorial.as_view()),
    
    # =====================
    # Rutas para colin.py
    # =====================
    path("colin/Caso1LibrosConEditorial", colin.Caso1LibrosConEditorial.as_view()),
    path("colin/Caso2CalificacionesConLibro", colin.Caso2CalificacionesConLibro.as_view()),
    path("colin/Caso3AutoresConLibros", colin.Caso3AutoresConLibros.as_view()),
    path("colin/Caso4ValuesEjemplo", colin.Caso4ValuesEjemplo.as_view()),
    path("colin/Caso5OnlyEjemplo", colin.Caso5OnlyEjemplo.as_view()),
    path("colin/Caso6DeferEjemplo", colin.Caso6DeferEjemplo.as_view()),
    path("colin/Caso7AutoresLibrosEditorial", colin.Caso7AutoresLibrosEditorial.as_view()),
]

urlpatterns = []

urlpatterns.extend(gran_colin)
urlpatterns.extend(los_demas)
