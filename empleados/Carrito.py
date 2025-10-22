from decimal import Decimal
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, empleado):
        id = str(empleado.id)
        salario = empleado.salario_empleado if hasattr(empleado, 'salario_empleado') else empleado.precio
        if isinstance(salario, Decimal):
            salario = float(salario)

        stock = getattr(empleado, 'edad_empleado', 0)  # ← usamos edad_empleado como stock

        # Validación 1: no permitir agregar si stock es 0
        if stock <= 0:
            raise ValueError("Este producto no tiene stock disponible.")

        # Validación 2: no permitir agregar más que el stock
        cantidad_actual = self.carrito.get(id, {}).get("cantidad", 0)
        if cantidad_actual >= stock:
            raise ValueError("No puedes agregar más unidades que las disponibles en stock.")

        if id not in self.carrito:
            self.carrito[id] = {
                "empleado_id": empleado.id,
                "nombre": empleado.nombre_empleado,
                "precio": salario,
                "acumulado": salario,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] = salario
            self.carrito[id]["acumulado"] += salario

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        precio = producto.salario_empleado if hasattr(producto, 'salario_empleado') else producto.precio
        if isinstance(precio, Decimal):
            precio = float(precio)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):  
        self.session["carrito"] = {}
        self.session.modified = True