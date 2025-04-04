## 🔄 Cambios realizados

###1. **Transformación a POO**:
   - Convertí las funciones procedurales en una clase `CalculadoraMCD`
   - Encapsulé la lógica relacionada en métodos de clase

###2. **Implementación de Getters/Setters**:
   - Añadí propiedades `@property` para `a` y `b`
   - Implementé setters con validación integrada (`@a.setter`, `@b.setter`)

###3. **Mejoras en validación**:
   - Integré la función `validar_numero` como método de clase
   - La validación ahora se ejecuta automáticamente al asignar valores

###4. **Nuevo método interactivo**:
   - Añadí `solicitar_numeros()` para entrada de usuario amigable

###5. **Manejo de estado**:
   - Los números ahora son atributos de clase (`self._a`, `self._b`)
   - El cálculo mantiene estado entre operaciones
