from flask import Flask, render_template, request

app=Flask(__name__, template_folder='templates')

@app.route('/cinepolis', methods=['POST', 'GET'])
def controlCinepolis():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        cantCompradores = int(request.form.get("cantCompradores", 0))  
        cantBoletas = int(request.form.get("cantBoletas", 0)) 
        tarjeta = request.form.get("tarjCineco")
        total = 0
        totalSinTarjeta = 0
        
        print("Nombre:", nombre)
        print("Cantidad de Compradores:", cantCompradores)
        print("Cantidad de Boletas:", cantBoletas)
        print("Tarjeta Cineco:", tarjeta)


        if cantBoletas > (cantCompradores * 7):
            return render_template('cinepolis.html', mensaje="Cada comprador no puede comprar más de 7 boletas")
        
        totalSinDescuentos = cantBoletas * 12
        descuentoCantidad = 0
        descuentoTarjeta = 0
        
        
        if cantBoletas > 5:
            descuentoCantidad = totalSinDescuentos * 0.15
        elif cantBoletas in [3, 4, 5]:
            descuentoCantidad = totalSinDescuentos * 0.10 
        
        totalConDescuentoCantidad = totalSinDescuentos - descuentoCantidad
        
        if tarjeta == "si":
            descuentoTarjeta = totalConDescuentoCantidad * 0.10
            
        totalFinal = totalConDescuentoCantidad - descuentoTarjeta
        
        mensaje = f"Subtotal: ${totalSinDescuentos:.2f}. "
        if descuentoCantidad > 0:
            mensaje += f"Descuento por cantidad de boletos: ${descuentoCantidad:.2f}."
        if descuentoTarjeta > 0:
            mensaje += f"Descuento por tarjeta CINECO: ${descuentoTarjeta:.2f}."
        
        return render_template('cinepolis.html', mensaje=mensaje, total=totalFinal, nombre=nombre)
    return render_template('cinepolis.html', total='')

if __name__ == '__main__':
    app.run(debug=True,  port=3000)