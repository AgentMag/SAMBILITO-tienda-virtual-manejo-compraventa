def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return {"total_carrito": total}

from .models import Categoria

def categorias_context(request):
    categoria_id = request.GET.get('categoria')
    return {
        'categorias': Categoria.objects.all(),
        'categoria_seleccionada': categoria_id
    }