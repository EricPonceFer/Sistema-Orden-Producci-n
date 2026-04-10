from django.shortcuts import render

#  Base template call
def index(request):
    return render(request, 'index.html')

# Callout of the production order template for the product

def production_order_product(request):
    operaciones = [
        {"nombre": "Enfundado de flan"},
        {"nombre": "Empaque manual"},
    ]
    filas = range(10)
    return render(request, 'process/production_order_product.html', {
        'operaciones': operaciones,
        'filas': filas,
    })
