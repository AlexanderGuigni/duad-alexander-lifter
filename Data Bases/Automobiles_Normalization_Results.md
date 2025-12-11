# Normalización de la Tabla Automobiles - Resultados por Paso

## Tabla Original - Automobiles

| VIN | Make | Model | Year | Color | Owner ID | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|-----|------|-------|------|-------|----------|------------|-------------|-------------------|------------------|
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | POL12345 |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | POL54321 |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | POL67890 |
| 1G1RA6E81FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | POL98765 |

---

## Paso 1: Crear Tabla Brands

### Tabla Brands (Nueva)
| Brand ID | Marca |
|----------|-------|
| 1 | Honda |
| 2 | Chevrolet |

### Tabla Automobiles (Actualizada)
| VIN | Brand ID | Model | Year | Color | Owner ID | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|-----|----------|-------|------|-------|----------|------------|-------------|-------------------|------------------|
| 1HGCM82633A | 1 | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | POL12345 |
| 1HGCM82633A | 1 | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | POL54321 |
| 5J6RM4H79EL | 1 | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | POL67890 |
| 1G1RA6E81FU | 2 | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | POL98765 |

---

## Paso 2: Crear Tabla Models

### Tabla Models (Nueva)
| Model ID | Brand ID | Modelo |
|----------|----------|--------|
| 1 | 1 | Accord |
| 2 | 1 | CR-V |
| 3 | 2 | Volt |

### Tabla Automobiles (Actualizada)
| VIN | Brand ID | Model ID | Year | Color | Owner ID | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|-----|----------|----------|------|-------|----------|------------|-------------|-------------------|------------------|
| 1HGCM82633A | 1 | 1 | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | POL12345 |
| 1HGCM82633A | 1 | 1 | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | POL54321 |
| 5J6RM4H79EL | 1 | 2 | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | POL67890 |
| 1G1RA6E81FU | 2 | 3 | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | POL98765 |

---

## Paso 3: Crear Tabla Colors

### Tabla Colors (Nueva)
| Color ID | Color |
|----------|-------|
| 1 | Silver |
| 2 | Blue |
| 3 | Red |

### Tabla Automobiles (Actualizada)
| VIN | Brand ID | Model ID | Year | Color ID | Owner ID | Owner Name | Owner Phone | Insurance Company | Insurance Policy |
|-----|----------|----------|------|----------|----------|------------|-------------|-------------------|------------------|
| 1HGCM82633A | 1 | 1 | 2003 | 1 | 101 | Alice | 123-456-7890 | ABC Insurance | POL12345 |
| 1HGCM82633A | 1 | 1 | 2003 | 1 | 102 | Bob | 987-654-3210 | XYZ Insurance | POL54321 |
| 5J6RM4H79EL | 1 | 2 | 2014 | 2 | 103 | Claire | 555-123-4567 | DEF Insurance | POL67890 |
| 1G1RA6E81FU | 2 | 3 | 2015 | 3 | 104 | Dave | 111-222-3333 | GHI Insurance | POL98765 |

---

## Paso 4: Crear Tabla Owners

### Tabla Owners (Nueva)
| Owner ID | Owner Name | Owner Phone |
|----------|------------|-------------|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

### Tabla Automobiles (Actualizada)
| VIN | Brand ID | Model ID | Year | Color ID | Owner ID | Insurance Company | Insurance Policy |
|-----|----------|----------|------|----------|----------|-------------------|------------------|
| 1HGCM82633A | 1 | 1 | 2003 | 1 | 101 | ABC Insurance | POL12345 |
| 1HGCM82633A | 1 | 1 | 2003 | 1 | 102 | XYZ Insurance | POL54321 |
| 5J6RM4H79EL | 1 | 2 | 2014 | 2 | 103 | DEF Insurance | POL67890 |
| 1G1RA6E81FU | 2 | 3 | 2015 | 3 | 104 | GHI Insurance | POL98765 |

---

## Paso 5: Crear Tabla Insurances

### Tabla Insurances (Nueva)
| Insurance ID | Insurance Company |
|--------------|-------------------|
| 1 | ABC Insurance |
| 2 | XYZ Insurance |
| 3 | DEF Insurance |
| 4 | GHI Insurance |

### Tabla Automobiles (Actualizada)
| VIN | Brand ID | Model ID | Year | Color ID | Owner ID | Insurance ID | Insurance Policy |
|-----|----------|----------|------|----------|----------|--------------|------------------|
| 1HGCM82633A | 1 | 1 | 2003 | 1 | 101 | 1 | POL12345 |
| 1HGCM82633A | 1 | 1 | 2003 | 1 | 102 | 2 | POL54321 |
| 5J6RM4H79EL | 1 | 2 | 2014 | 2 | 103 | 3 | POL67890 |
| 1G1RA6E81FU | 2 | 3 | 2015 | 3 | 104 | 4 | POL98765 |

---

## Paso 6: Crear Primary Key y Tabla AutomobileOwners (Relación Muchos a Muchos)

### Observación Importante:
El VIN no puede ser primary key porque se repite en varios registros. Un mismo automóvil puede tener varios dueños, creando una relación muchos a muchos que requiere una tabla intermedia.

### Tabla AutomobileOwners (Nueva)
| ID | Car ID | Owner ID | Insurance ID | Insurance Policy |
|--------------------|--------|----------|--------------|------------------|
| 1 | 1 | 101 | 1 | POL12345 |
| 2 | 1 | 102 | 2 | POL54321 |
| 3 | 2 | 103 | 3 | POL67890 |
| 4 | 3 | 104 | 4 | POL98765 |

### Tabla Automobiles (Final)
| Car ID | VIN | Brand ID | Model ID | Year | Color ID |
|--------|-----|----------|----------|------|----------|
| 1 | 1HGCM82633A | 1 | 1 | 2003 | 1 | 1 |
| 2 | 5J6RM4H79EL | 1 | 2 | 2014 | 2 | 3 |
| 3 | 1G1RA6E81FU | 2 | 3 | 2015 | 3 | 4 |

---

## Resultado Final - Todas las Tablas Normalizadas

### 1. Tabla Automobiles
| Car ID | VIN | Brand ID | Model ID | Year | Color ID |
|--------|-----|----------|----------|------|----------|
| 1 | 1HGCM82633A | 1 | 1 | 2003 | 1 | 1 |
| 2 | 5J6RM4H79EL | 1 | 2 | 2014 | 2 | 3 |
| 3 | 1G1RA6E81FU | 2 | 3 | 2015 | 3 | 4 |

### 2. Tabla Brands
| Brand ID | Marca |
|----------|-------|
| 1 | Honda |
| 2 | Chevrolet |

### 3. Tabla Models
| Model ID | Brand ID | Modelo |
|----------|----------|--------|
| 1 | 1 | Accord |
| 2 | 1 | CR-V |
| 3 | 2 | Volt |

### 4. Tabla Colors
| Color ID | Color |
|----------|-------|
| 1 | Silver |
| 2 | Blue |
| 3 | Red |

### 5. Tabla Owners
| Owner ID | Owner Name | Owner Phone |
|----------|------------|-------------|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

### 6. Tabla Insurances
| Insurance ID | Insurance Company |
|--------------|-------------------|
| 1 | ABC Insurance |
| 2 | XYZ Insurance |
| 3 | DEF Insurance |
| 4 | GHI Insurance |

### 7. Tabla AutomobileOwners
| ID | Car ID | Owner ID | Insurance ID | Insurance Policy |
|--------------------|--------|----------|--------------|------------------|
| 1 | 1 | 101 | 1 | POL12345 |
| 2 | 1 | 102 | 2 | POL54321 |
| 3 | 2 | 103 | 3 | POL67890 |
| 4 | 3 | 104 | 4 | POL98765 |

---

## Relaciones


1. **Relaciones Jerárquicas Establecidas**: 
   - Models → Brands (muchos a uno): Cada modelo pertenece a una marca específica
   - Automobiles → Models (muchos a uno): Varios automóviles pueden ser del mismo modelo
   - Automobiles → Colors, Owners, Insurances (muchos a uno)

2. **Relación Muchos a Muchos**:
   - Se creó tabla AutomobileOwners para manejar la relación entre autos y propietarios
   - Un automóvil puede tener varios dueños
   - Un dueño puede tener varios automóviles
   - Cada combinación auto-dueño tiene su propia póliza de seguro
