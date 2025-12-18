# Normalización de la Tabla Ordenes - Resultados por Paso (Análisis Corregido)

## Tabla Original - Ordenes

| Order ID | Customer Name | Customer Phone | Address | Item ID | Item Name | Price | Quantity | Special Request | Delivery Time |
|----------|---------------|----------------|---------|---------|-----------|--------|----------|-----------------|---------------|
| 001 | Alice | 123-456-7890 | 123 Main St | 101 | Cheeseburger | $8 | 2 | No onions | 6:00 PM |
| 001 | Alice | 123-456-7890 | 123 Main St | 102 | Fries | $3 | 1 | Extra ketchup | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 103 | Pizza | $12 | 1 | Extra cheese | 7:30 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 104 | Fries | $2 | 2 | None | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 105 | Salad | $6 | 1 | No croutons | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water | $1 | 1 | None | 5:00 PM |

---

## Paso 1: Separar Orders y OrderItems (Solucionar problema de Primary Key)

### Tabla Orders (Nueva)
| Order ID | Customer Name | Customer Phone | Address | Delivery Time |
|----------|---------------|----------------|---------|---------------|
| 001 | Alice | 123-456-7890 | 123 Main St | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 5:00 PM |

### Tabla OrderItems (Nueva)
| Item ID | Order ID | Item Name | Price | Quantity | Special Request |
|---------|----------|-----------|--------|----------|------------------|
| 101 | 001 | Cheeseburger | $8 | 2 | No onions |
| 102 | 001 | Fries | $3 | 1 | Extra ketchup |
| 103 | 002 | Pizza | $12 | 1 | Extra cheese |
| 104 | 002 | Fries | $2 | 2 | None |
| 105 | 003 | Salad | $6 | 1 | No croutons |
| 106 | 004 | Water | $1 | 1 | None |

---

## Paso 2: Crear Tabla Customers

### Tabla Customers (Nueva)
| Customer ID | Customer Name | Customer Phone |
|-------------|---------------|----------------|
| 1 | Alice | 123-456-7890 |
| 2 | Bob | 987-654-3210 |
| 3 | Claire | 555-123-4567 |

### Tabla Orders (Actualizada)
| Order ID | Customer ID | Address | Delivery Time |
|----------|-------------|---------|---------------|
| 001 | 1 | 123 Main St | 6:00 PM |
| 002 | 2 | 456 Elm St | 7:30 PM |
| 003 | 3 | 789 Oak St | 12:00 PM |
| 004 | 3 | 464 Georgia St | 5:00 PM |

### Tabla OrderItems (Sin cambios)
| Item ID | Order ID | Item Name | Price | Quantity | Special Request |
|---------|----------|-----------|--------|----------|------------------|
| 101 | 001 | Cheeseburger | $8 | 2 | No onions |
| 102 | 001 | Fries | $3 | 1 | Extra ketchup |
| 103 | 002 | Pizza | $12 | 1 | Extra cheese |
| 104 | 002 | Fries | $2 | 2 | None |
| 105 | 003 | Salad | $6 | 1 | No croutons |
| 106 | 004 | Water | $1 | 1 | None |

---

## Paso 3: Crear Tabla Addresses

### Tabla Addresses (Nueva)
| Address ID | Customer ID | Address |
|------------|-------------|---------|
| 1 | 1 | 123 Main St |
| 2 | 2 | 456 Elm St |
| 3 | 3 | 789 Oak St |
| 4 | 3 | 464 Georgia St |

### Tabla Orders (Actualizada)
| Order ID | Customer ID | Address ID | Delivery Time |
|----------|-------------|------------|---------------|
| 001 | 1 | 1 | 6:00 PM |
| 002 | 2 | 2 | 7:30 PM |
| 003 | 3 | 3 | 12:00 PM |
| 004 | 3 | 4 | 5:00 PM |

### Tabla OrderItems (Sin Cambios)
| Item ID | Order ID | Item Name | Price | Quantity | Special Request |
|---------|----------|-----------|--------|----------|------------------|
| 101 | 001 | Cheeseburger | $8 | 2 | No onions |
| 102 | 001 | Fries | $3 | 1 | Extra ketchup |
| 103 | 002 | Pizza | $12 | 1 | Extra cheese |
| 104 | 002 | Fries | $2 | 2 | None |
| 105 | 003 | Salad | $6 | 1 | No croutons |
| 106 | 004 | Water | $1 | 1 | None |

---

## Paso 4: Crear Tabla Products

### Tabla Products (Nueva)
| Product ID | Item Name | Price |
|------------|-----------|--------|
| 1 | Cheeseburger | $8 |
| 2 | Fries | $2 |
| 3 | Pizza | $12 |
| 4 | Salad | $6 |
| 5 | Water | $1 |
| 6 | Fries | $3 |

### Tabla OrderItems (Actualizada)
| Item ID | Order ID | Product ID | Quantity | Special Request |
|---------|----------|------------|----------|------------------|
| 101 | 001 | 1 | 2 | No onions |
| 102 | 001 | 6 | 1 | Extra ketchup |
| 104 | 002 | 3 | 1 | Extra cheese |
| 105 | 002 | 2 | 2 | None |
| 106 | 003 | 4 | 1 | No croutons |
| 107 | 004 | 5 | 1 | None |

---

## Paso 5: Ajustar Precios y Extras (Manejo de Special Requests como productos adicionales)

### Tabla Products (Actualizada)
| Product ID | Item Name | Price |
|------------|-----------|--------|
| 1 | Cheeseburger | $8 |
| 2 | Fries | $2 |
| 3 | Pizza | $12 |
| 4 | Salad | $6 |
| 5 | Water | $1 |
| 6 | Extra Ketchup | $1 |

### Tabla OrderItems (Actualizada)
| Item ID | Order ID | Product ID | Quantity | Special Request |
|---------|----------|------------|----------|------------------|
| 101 | 001 | 1 | 2 | No onions |
| 102 | 001 | 2 | 1 | Extra ketchup |
| 103 | 001 | 6 | 1 | None |
| 104 | 002 | 3 | 1 | Extra cheese |
| 105 | 002 | 2 | 2 | None |
| 106 | 003 | 4 | 1 | No croutons |
| 107 | 004 | 5 | 1 | None |

### Observación Importante:
Se detectó que "Fries" tiene precios diferentes ($2 y $3) debido a que una orden incluye "Extra Ketchup". En lugar de tener productos con precios variables, se creó un producto separado "Extra Ketchup" con precio de $1, normalizando así el precio base de "Fries" a $2.
---

## Resultado Final - Todas las Tablas Normalizadas

### 1. Tabla Orders
| Order ID | Customer ID | Address ID | Delivery Time |
|----------|-------------|------------|---------------|
| 001 | 1 | 1 | 6:00 PM |
| 002 | 2 | 2 | 7:30 PM |
| 003 | 3 | 3 | 12:00 PM |
| 004 | 3 | 4 | 5:00 PM |

### 2. Tabla Customers
| Customer ID | Customer Name | Customer Phone |
|-------------|---------------|----------------|
| 1 | Alice | 123-456-7890 |
| 2 | Bob | 987-654-3210 |
| 3 | Claire | 555-123-4567 |

### 3. Tabla Addresses
| Address ID | Customer ID | Address |
|------------|-------------|---------|
| 1 | 1 | 123 Main St |
| 2 | 2 | 456 Elm St |
| 3 | 3 | 789 Oak St |
| 4 | 3 | 464 Georgia St |

### 4. Tabla Products
| Product ID | Item Name | Price |
|------------|-----------|--------|
| 1 | Cheeseburger | $8 |
| 2 | Fries | $2 |
| 3 | Pizza | $12 |
| 4 | Salad | $6 |
| 5 | Water | $1 |
| 6 | Extra Ketchup | $1 |

### 5. Tabla OrderItems
| Item ID | Order ID | Product ID | Quantity | Special Request |
|---------|----------|------------|----------|------------------|
| 101 | 001 | 1 | 2 | No onions |
| 102 | 001 | 2 | 1 | None |
| 103 | 001 | 6 | 1 | None |
| 104 | 002 | 3 | 1 | Extra cheese |
| 105 | 002 | 2 | 2 | None |
| 106 | 003 | 4 | 1 | No croutons |
| 107 | 004 | 5 | 1 | None |

---

## Relaciones Claras

   - Orders → Customers (muchos a uno)
   - Orders → Addresses (muchos a uno) 
   - Addresses → Customers (muchos a uno)
   - OrderItems → Orders (muchos a uno)
   - OrderItems → Products (muchos a uno)
