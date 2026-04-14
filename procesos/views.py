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
    movimiento_planta = [
        {"movimiento": "ENTRADA POR PROCESO"},
        {"movimiento": "SALIDA PARA"},
        {"movimiento": "SALIDA PARA"},
        {"movimiento": "SALIDA PARA"}
    ]
    return render(request, 'process/production_order_product.html', {
        'operaciones': operaciones,
        'filas': filas,
        'movimiento_planta': movimiento_planta
    })

def production_report(request):
    control_material = [
        {"material": "Leche", "cantidad": 100, "unidad": "litros"},
        {"material": "Azúcar", "cantidad": 50, "unidad": "kg"},
        {"material": "Gelatina", "cantidad": 20, "unidad": "kg"},
    ]
    return render(request, 'process/production_report.html', {
        'control_material': control_material
    })
