# Variables locales que no quiero incorporar en main.py

PAISES_COSTEROS = {
    "Chile", "Perú", "Ecuador", "Colombia", "Venezuela",
    "Argentina", "Uruguay", "Brasil", "Guyana", "Surinam",
    "Panamá", "Costa Rica", "Nicaragua", "Honduras", "Holanda", "El Salvador",
    "Guatemala", "México", "Canadá", "Estados Unidos",
    "Cuba", "Haití", "República Dominicana", "Jamaica",

    "España", "Francia", "Portugal", "Italia", "Grecia",
    "Alemania", "Bélgica", "Países Bajos", "Noruega", "Suecia",
    "Finlandia", "Polonia", "Croacia", "Albania", "Turquía",

    "Egipto", "Marruecos", "Argelia", "Túnez", "Libia",
    "Sudáfrica", "Namibia", "Angola", "Kenia", "Tanzania",

    "China", "Japón", "Corea del Sur", "India", "Pakistán",
    "Bangladesh", "Tailandia", "Vietnam", "Malasia",
    "Indonesia", "Australia", "Nueva Zelanda"
}

CIUDADES_COSTERAS_POR_PAIS= {
    # --- AMÉRICA ---
    "Chile": ["Valparaíso", "San Antonio", "Iquique"],
    "Perú": ["Callao", "Mollendo", "Paita"],
    "Ecuador": ["Guayaquil", "Manta", "Esmeraldas"],
    "Colombia": ["Cartagena", "Barranquilla", "Santa Marta"],
    "Venezuela": ["La Guaira", "Puerto Cabello", "Maracaibo"],
    "Argentina": ["Buenos Aires", "Mar del Plata", "Bahía Blanca"],
    "Uruguay": ["Montevideo", "Punta del Este", "Colonia del Sacramento"],
    "Brasil": ["Río de Janeiro", "Santos", "Salvador"],
    "Guyana": ["Georgetown", "New Amsterdam", "Corriverton"],
    "Surinam": ["Paramaribo", "Nieuw Nickerie", "Totness"],
    "Panamá": ["Ciudad de Panamá", "Colón", "Balboa"],
    "Costa Rica": ["Limón", "Puntarenas", "Caldera"],
    "Nicaragua": ["Corinto", "Bluefields", "Puerto Sandino"],
    "Honduras": ["Puerto Cortés", "La Ceiba", "Tela"],
    "El Salvador": ["Acajutla", "La Unión", "La Libertad"],
    "Guatemala": ["Puerto Barrios", "Puerto Quetzal", "Champerico"],
    "México": ["Veracruz", "Manzanillo", "Lázaro Cárdenas"],
    "Canadá": ["Vancouver", "Halifax", "Montreal"],
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Miami"],
    "Cuba": ["La Habana", "Santiago de Cuba", "Matanzas"],
    "Haití": ["Puerto Príncipe", "Cap-Haïtien", "Jacmel"],
    "República Dominicana": ["Santo Domingo", "Puerto Plata", "La Romana"],
    "Jamaica": ["Kingston", "Montego Bay", "Ocho Ríos"],

    # --- EUROPA ---
    "España": ["Barcelona", "Valencia", "Algeciras"],
    "Francia": ["Marsella", "Le Havre", "Niza"],
    "Portugal": ["Lisboa", "Oporto", "Sines"],
    "Italia": ["Génova", "Nápoles", "Trieste"],
    "Grecia": ["El Pireo", "Tesalónica", "Patras"],
    "Alemania": ["Hamburgo", "Bremerhaven", "Rostock"],
    "Bélgica": ["Amberes", "Zeebrugge", "Gante"],
    "Holanda": ["Róterdam", "Ámsterdam", "Vlissingen"], # Nota: Mantenemos Holanda y Países Bajos por compatibilidad
    "Países Bajos": ["Róterdam", "Ámsterdam", "Vlissingen"],
    "Noruega": ["Oslo", "Bergen", "Stavanger"],
    "Suecia": ["Gotemburgo", "Estocolmo", "Malmö"],
    "Finlandia": ["Helsinki", "Turku", "Kotka"],
    "Polonia": ["Gdansk", "Gdynia", "Szczecin"],
    "Croacia": ["Rijeka", "Split", "Dubrovnik"],
    "Albania": ["Durrës", "Vlorë", "Sarandë"],
    "Turquía": ["Estambul", "Mersin", "Esmirna"],

    # --- ÁFRICA ---
    "Egipto": ["Alejandría", "Puerto Said", "Damietta"],
    "Marruecos": ["Tánger Med", "Casablanca", "Agadir"],
    "Argelia": ["Argel", "Orán", "Skikda"],
    "Túnez": ["Túnez", "Rades", "Sfax"],
    "Libia": ["Trípoli", "Misrata", "Bengasi"],
    "Sudáfrica": ["Durban", "Ciudad del Cabo", "Port Elizabeth"],
    "Namibia": ["Walvis Bay", "Lüderitz", "Swakopmund"],
    "Angola": ["Luanda", "Lobito", "Namibe"],
    "Kenia": ["Mombasa", "Lamu", "Malindi"],
    "Tanzania": ["Dar es Salaam", "Tanga", "Zanzíbar"],

    # --- ASIA / OCEANÍA ---
    "China": ["Shanghái", "Ningbo", "Shenzhen"],
    "Japón": ["Tokio", "Yokohama", "Kobe"],
    "Corea del Sur": ["Busán", "Incheon", "Ulsan"],
    "India": ["Mumbai", "Chennai", "Kolkata"],
    "Pakistán": ["Karachi", "Gwadar", "Port Qasim"],
    "Bangladesh": ["Chittagong", "Mongla", "Payra"],
    "Tailandia": ["Laem Chabang", "Bangkok", "Phuket"],
    "Vietnam": ["Ciudad Ho Chi Minh", "Haiphong", "Da Nang"],
    "Malasia": ["Port Klang", "Tanjung Pelepas", "Penang"],
    "Indonesia": ["Yakarta", "Surabaya", "Belawan"],
    "Australia": ["Sídney", "Melbourne", "Fremantle"],
    "Nueva Zelanda": ["Auckland", "Tauranga", "Lyttelton"]
}

# Nombre: (Peso en kg, Precio en dolares, Requiere frío en bool)
BASE_DATOS_ALIMENTOS = {
    # Frutas y Verduras (Frescos)
    "Manzana Roja": (0.20, 0.50, False),
    "Plátano Cavendish": (0.18, 0.30, False),
    "Uvas (Caja)": (0.50, 2.50, True),
    "Fresas (Paquete)": (0.40, 3.00, True),
    "Lechuga Romana": (0.30, 1.20, True),
    "Tomate Larga Vida": (0.15, 0.40, False),
    "Zanahoria (Bolsa)": (1.00, 1.50, True),
    "Papas (Malla)": (2.50, 4.00, False),
    "Cebolla Morada": (0.20, 0.60, False),
    "Espinaca (Bolsa)": (0.35, 2.00, True),
    "Aguacate Hass": (0.25, 1.80, False),
    "Limón Sutil": (0.10, 0.25, False),
    "Sandía Entera": (5.00, 6.00, False),
    "Piña Miel": (1.50, 3.50, False),
    "Champiñones (Bandeja)": (0.25, 2.20, True),

    # Carnes y Pescados (Requieren mucho frío)
    "Filete de Salmón": (1.00, 15.00, True),
    "Pechuga de Pollo": (0.80, 8.50, True),
    "Carne Molida": (0.50, 6.00, True),
    "Lomo Vetado": (1.20, 18.00, True),
    "Chuletas de Cerdo": (1.00, 9.00, True),
    "Camarones Congelados": (0.50, 12.00, True),
    "Tilapia (Filete)": (0.80, 7.00, True),
    "Atún Fresco": (0.40, 14.00, True),
    "Salchichas (Paquete)": (0.45, 3.50, True),
    "Tocino Ahumado": (0.25, 5.00, True),

    # Lácteos y Refrigerados
    "Leche Entera (Litro)": (1.00, 1.20, True),
    "Queso Gouda": (0.30, 4.50, True),
    "Yogurt Griego": (0.15, 1.00, True),
    "Mantequilla con Sal": (0.25, 2.50, True),
    "Crema de Leche": (0.20, 1.80, True),
    "Huevos (Docena)": (0.70, 2.20, True), # A veces se debaten, pero en logística suelen ir frescos
    "Queso Crema": (0.22, 3.00, True),
    "Helado de Vainilla": (1.00, 5.50, True),

    # Abarrotes y Secos (No requieren frío)
    "Arroz Grano Largo": (1.00, 1.50, False),
    "Fideos Espagueti": (0.40, 0.80, False),
    "Aceite de Oliva": (0.90, 8.00, False),
    "Harina de Trigo": (1.00, 1.10, False),
    "Azúcar Blanca": (1.00, 1.20, False),
    "Sal de Mar": (0.50, 0.90, False),
    "Lentejas": (1.00, 2.00, False),
    "Porotos Negros": (1.00, 2.10, False),
    "Café Molido": (0.25, 6.00, False),
    "Té Negro (Caja)": (0.10, 3.00, False),
    "Galletas de Soda": (0.30, 1.50, False),
    "Chocolate Amargo": (0.10, 2.50, False),
    "Miel de Abeja": (0.50, 7.00, False),
    "Mermelada de Fresa": (0.40, 3.20, False),
    "Atún en Lata": (0.17, 1.80, False),
    "Salsa de Tomate": (0.20, 0.90, False),
    "Cereal de Maíz": (0.50, 4.00, False)
}

# Nombre: (Peso en kg, Precio en dolares, Marca)
BASE_DATOS_TECNOLOGIA = {
    # Computación y Laptops
    "MacBook Pro 16": (2.1, 2500, "Apple"),
    "Dell XPS 13": (1.2, 1200, "Dell"),
    "Lenovo ThinkPad X1": (1.1, 1400, "Lenovo"),
    "ASUS ROG Strix": (2.5, 1800, "ASUS"),
    "HP Spectre x360": (1.3, 1300, "HP"),
    "Acer Predator Helios": (2.8, 1600, "Acer"),
    "Microsoft Surface Pro": (0.9, 1000, "Microsoft"),
    "iMac 24": (4.5, 1500, "Apple"),
    "Mac Mini": (1.2, 700, "Apple"),
    "Monitor Curvo 34'": (8.0, 500, "Samsung"),

    # Telefonía y Tablets
    "iPhone 15 Pro Max": (0.22, 1200, "Apple"),
    "Samsung Galaxy S24 Ultra": (0.23, 1300, "Samsung"),
    "Google Pixel 8 Pro": (0.21, 1000, "Google"),
    "Xiaomi 13T Pro": (0.20, 700, "Xiaomi"),
    "iPad Pro 12.9": (0.68, 1100, "Apple"),
    "Galaxy Tab S9 Ultra": (0.73, 1000, "Samsung"),
    "Kindle Paperwhite": (0.20, 150, "Amazon"),
    "Apple Watch Ultra 2": (0.06, 800, "Apple"),
    "Galaxy Watch 6": (0.05, 350, "Samsung"),
    "Garmin Fenix 7": (0.08, 700, "Garmin"),

    # Audio y Video
    "Sony Bravia OLED 65'": (24.0, 2200, "Sony"),
    "LG C3 OLED 55'": (18.0, 1500, "LG"),
    "Samsung QLED 75'": (35.0, 1800, "Samsung"),
    "JBL PartyBox 310": (17.4, 500, "JBL"),
    "Sonos Arc Soundbar": (6.2, 900, "Sonos"),
    "Sony WH-1000XM5": (0.25, 400, "Sony"),
    "AirPods Max": (0.38, 550, "Apple"),
    "Bose QuietComfort 45": (0.24, 330, "Bose"),
    "Proyector Epson 4K": (4.1, 900, "Epson"),
    "GoPro Hero 12": (0.15, 400, "GoPro"),

    # Gaming y Consolas
    "PlayStation 5 Slim": (3.2, 500, "Sony"),
    "Xbox Series X": (4.4, 500, "Microsoft"),
    "Nintendo Switch OLED": (0.42, 350, "Nintendo"),
    "Steam Deck OLED": (0.64, 550, "Valve"),
    "Meta Quest 3": (0.50, 500, "Meta"),
    "Tarjeta Gráfica RTX 4090": (2.2, 1600, "NVIDIA"),
    "Silla Gamer Titan": (28.0, 450, "Secretlab"),
    "Volante Logitech G29": (5.3, 300, "Logitech"),
    "Teclado Mecánico K95": (1.3, 200, "Corsair"),
    "Mouse G502 Hero": (0.12, 50, "Logitech"),

    # Hogar Inteligente y Electrodomésticos Tech
    "Refrigerador Smart Hub": (110.0, 2500, "Samsung"),
    "Lavadora Frontal AI": (75.0, 900, "LG"),
    "Dyson V15 Detect": (3.1, 750, "Dyson"),
    "Robot Aspiradora Roomba": (3.5, 600, "iRobot"),
    "Purificador de Aire": (4.8, 250, "Xiaomi"),
    "Cafetera Nespresso": (3.0, 200, "Nespresso"),
    "Air Fryer XXL": (6.5, 180, "Philips"),
    "Termostato Nest": (0.3, 130, "Google"),
    "Cerradura Inteligente": (1.5, 250, "Yale"),
    "Router Starlink V2": (4.2, 600, "SpaceX")
}

BASE_DATOS_VEHICULOS = {
    # Autos Compactos y Sedanes
    "Corolla": (1350, 22000, "Toyota", 2024),
    "Civic": (1300, 24000, "Honda", 2023),
    "Mazda 3": (1320, 23000, "Mazda", 2024),
    "Golf GTI": (1400, 32000, "Volkswagen", 2023),
    "Sentra": (1380, 21000, "Nissan", 2022),
    "Elantra": (1290, 20500, "Hyundai", 2024),
    "Rio": (1100, 16000, "Kia", 2023),
    "Onix": (1050, 15000, "Chevrolet", 2024),
    "Yaris": (1080, 18000, "Toyota", 2023),
    "Impreza": (1450, 25000, "Subaru", 2022),

    # SUVs y Familiares
    "RAV4": (1600, 30000, "Toyota", 2024),
    "CR-V": (1550, 31000, "Honda", 2023),
    "Tucson": (1500, 29000, "Hyundai", 2024),
    "Sportage": (1580, 28500, "Kia", 2023),
    "CX-5": (1650, 32000, "Mazda", 2022),
    "Qashqai": (1450, 27000, "Nissan", 2024),
    "Forester": (1680, 33000, "Subaru", 2023),
    "Tiguan": (1700, 34000, "Volkswagen", 2022),
    "Explorer": (2020, 45000, "Ford", 2023),
    "Grand Cherokee": (2100, 50000, "Jeep", 2024),

    # Camionetas (Pickups)
    "Hilux": (2100, 40000, "Toyota", 2023),
    "Ranger": (2200, 39000, "Ford", 2024),
    "L200": (1950, 36000, "Mitsubishi", 2023),
    "F-150 Raptor": (2600, 75000, "Ford", 2024),
    "Silverado 1500": (2400, 55000, "Chevrolet", 2023),
    "Amarok": (2250, 42000, "Volkswagen", 2022),
    "Navara": (2050, 38000, "Nissan", 2023),
    "Ram 1500": (2500, 60000, "Ram", 2024),
    "Cybertruck": (3000, 80000, "Tesla", 2024),
    "BT-50": (2000, 37000, "Mazda", 2023),

    # Deportivos y Lujo
    "911 Carrera": (1500, 120000, "Porsche", 2024),
    "Mustang GT": (1750, 55000, "Ford", 2024),
    "Camaro SS": (1700, 52000, "Chevrolet", 2023),
    "Corvette C8": (1600, 70000, "Chevrolet", 2024),
    "Model S Plaid": (2160, 90000, "Tesla", 2023),
    "Taycan": (2300, 100000, "Porsche", 2023),
    "Serie 3": (1580, 45000, "BMW", 2024),
    "Clase C": (1650, 48000, "Mercedes-Benz", 2023),
    "A4": (1550, 44000, "Audi", 2022),
    "Huracán": (1420, 250000, "Lamborghini", 2023),

    # Motos
    "Ninja 400": (168, 6000, "Kawasaki", 2023),
    "MT-07": (184, 8000, "Yamaha", 2024),
    "R1250 GS": (249, 20000, "BMW", 2023),
    "Duke 390": (150, 6500, "KTM", 2024),
    "CBR600RR": (190, 12000, "Honda", 2023),
    "Iron 883": (256, 11000, "Harley-Davidson", 2022),
    "Vespa Primavera": (120, 4500, "Piaggio", 2024),
    "Africa Twin": (230, 15000, "Honda", 2023),
    "Panigale V4": (198, 25000, "Ducati", 2024),
    "Scrambler": (185, 10500, "Triumph", 2023)
}