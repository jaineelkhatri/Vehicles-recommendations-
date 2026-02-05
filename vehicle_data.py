# Vehicle Database
# Format: List of dictionaries with vehicle details

vehicles = [
    # ==========================
    # LOW BUDGET (< 10 Lakhs / < 1.5 Lakhs for Bikes)
    # ==========================
    
    # --- CARS ---
    {
        "name": "Maruti Suzuki Swift",
        "type": "car",
        "budget_range": "low",
        "fuel": "petrol",
        "mileage": "22 kmpl",
        "usage": "city",
        "price": "₹6.00 Lakh",
        "features": "Sporty design, good mileage, easy maintenance",
        "description": "A perfect city hatchback that is fun to drive and easy on the pocket."
    },
    {
        "name": "Maruti Alto K10",
        "type": "car",
        "budget_range": "low",
        "fuel": "petrol",
        "mileage": "24 kmpl",
        "usage": "city",
        "price": "₹3.99 Lakh",
        "features": "Compact size, high efficiency, perfect first car",
        "description": "The quintessential entry-level car for Indian families."
    },
    {
        "name": "Renault Kwid",
        "type": "car",
        "budget_range": "low",
        "fuel": "petrol",
        "mileage": "22 kmpl",
        "usage": "city",
        "price": "₹4.70 Lakh",
        "features": "SUV-inspired styling, digital cluster, touchscreen",
        "description": "A stylish small car that stands out in the crowd."
    },
    {
        "name": "Tata Tiago",
        "type": "car",
        "budget_range": "low",
        "fuel": "petrol", # Also comes in CNG
        "mileage": "20 kmpl",
        "usage": "city",
        "price": "₹5.60 Lakh",
        "features": "4-star safety, solid build quality, good music system",
        "description": "One of the safest hatchbacks in its segment."
    },
    {
        "name": "Maruti WagonR",
        "type": "car",
        "budget_range": "low",
        "fuel": "cng", # Highlight CNG option
        "mileage": "34 km/kg", 
        "usage": "city",
        "price": "₹6.45 Lakh",
        "features": "Tall-boy design, immense headroom, CNG efficiency",
        "description": "The most practical city car with huge space."
    },

    # --- BIKES ---
    {
        "name": "Hero Splendor Plus",
        "type": "bike",
        "budget_range": "low",
        "fuel": "petrol",
        "mileage": "65 kmpl",
        "usage": "city",
        "price": "₹75,000",
        "features": "High reliability, excellent mileage, low service cost",
        "description": "India's best-selling commuter bike known for its efficiency."
    },
    {
        "name": "Honda Activa 6G",
        "type": "bike", # Scooter
        "budget_range": "low",
        "fuel": "petrol",
        "mileage": "45 kmpl",
        "usage": "city",
        "price": "₹78,000",
        "features": "Metal body, reliable engine, push start",
        "description": "The undisputed king of scooters in India."
    },
     {
        "name": "TVS Jupiter",
        "type": "bike",
        "budget_range": "low",
        "fuel": "petrol",
        "mileage": "50 kmpl",
        "usage": "city",
        "price": "₹76,000",
        "features": "Large under-seat storage, external fuel fill, comfortable ride",
        "description": "A feature-packed scooter offering great value."
    },
     {
        "name": "Bajaj Pulsar 150",
        "type": "bike",
        "budget_range": "low",
        "fuel": "petrol",
        "mileage": "48 kmpl",
        "usage": "city",
        "price": "₹1.10 Lakh",
        "features": "Punchy pickup, muscular looks, tried and tested engine",
        "description": "The bike that defined the sports-commuter segment."
    },


    # ==========================
    # MEDIUM BUDGET (10L - 25L / 1.5L - 4L for Bikes)
    # ==========================

    # --- SUVS & CARS ---
    {
        "name": "Tata Nexon",
        "type": "suv",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "17 kmpl",
        "usage": "family",
        "price": "₹8.00 Lakh",
        "features": "5-star safety rating, spacious interior, robust build",
        "description": "One of the safest compact SUVs in India, great for small families."
    },
    {
        "name": "Hyundai Creta",
        "type": "suv",
        "budget_range": "medium",
        "fuel": "diesel",
        "mileage": "18 kmpl",
        "usage": "family",
        "price": "₹11.00 Lakh",
        "features": "Premium interiors, panoramic sunroof, comfortable ride",
        "description": "A dominant player in the SUV market offering a premium feel."
    },
    {
        "name": "Kia Seltos",
        "type": "suv",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "16 kmpl",
        "usage": "highway",
        "price": "₹10.90 Lakh",
        "features": "Tech-loaded cabin, Bose speakers, aggressive styling",
        "description": "A sporty and tech-savvy SUV for the modern family."
    },
    {
        "name": "Mahindra Thar",
        "type": "suv",
        "budget_range": "medium",
        "fuel": "diesel",
        "mileage": "15 kmpl",
        "usage": "highway",
        "price": "₹15.00 Lakh",
        "features": "4x4 capability, rugged look, convertible top",
        "description": "An iconic off-roader that makes a statement wherever it goes."
    },
    {
        "name": "Honda City",
        "type": "car",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "18 kmpl",
        "usage": "city",
        "price": "₹11.80 Lakh",
        "features": "Best-in-class rear seat comfort, smooth CVT, refined engine",
        "description": "The benchmark sedan for comfort and reliability."
    },
    {
        "name": "Skoda Slavia",
        "type": "car",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "19 kmpl",
        "usage": "highway",
        "price": "₹11.50 Lakh",
        "features": "Powerful 1.5L TSI engine, solid build, huge boot space",
        "description": "A driver's car with German engineering and safety."
    },
     {
        "name": "Mahindra Scorpio-N",
        "type": "suv",
        "budget_range": "medium",
        "fuel": "diesel",
        "mileage": "14 kmpl",
        "usage": "family",
        "price": "₹13.50 Lakh",
        "features": "Imposing stance, 7-seater, powerful diesel engine",
        "description": "The 'Big Daddy' of SUVs, perfect for large families and rough roads."
    },

    # --- BIKES (Medium) ---
    {
        "name": "Royal Enfield Classic 350",
        "type": "bike",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "35 kmpl",
        "usage": "highway",
        "price": "₹2.20 Lakh",
        "features": "Vintage look, thumping exhaust, stable highway ride",
        "description": "A cult classic that offers a retro charm and comfortable cruising."
    },
    {
        "name": "KTM Duke 390",
        "type": "bike",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "25 kmpl",
        "usage": "highway",
        "price": "₹3.10 Lakh",
        "features": "Aggressive power, sharp handling, advanced tech",
        "description": "A performance beast for those who love speed and corners."
    },
    {
        "name": "Royal Enfield Meteor 350",
        "type": "bike",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "35 kmpl",
        "usage": "highway",
        "price": "₹2.05 Lakh",
        "features": "Cruiser ergonomics, navigation pod, refined engine",
        "description": "Designed for long-distance highway cruising in comfort."
    },
    {
        "name": "Triumph Speed 400",
        "type": "bike",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "29 kmpl",
        "usage": "city",
        "price": "₹2.33 Lakh",
        "features": "Premium finish, responsive engine, agile handling",
        "description": "A modern classic that is easy to ride in the city and fun on highways."
    },
    {
        "name": "Royal Enfield Hunter 350",
        "type": "bike",
        "budget_range": "medium",
        "fuel": "petrol",
        "mileage": "36 kmpl",
        "usage": "city",
        "price": "₹1.70 Lakh",
        "features": "Compact, agile, modern retro styling",
        "description": "The most accessible and city-friendly Royal Enfield."
    },


    # ==========================
    # HIGH BUDGET (> 25 Lakhs / > 4 Lakhs for Bikes)
    # ==========================

    # --- CARS & SUVS ---
    {
        "name": "Toyota Innova Crysta",
        "type": "car",
        "budget_range": "high",
        "fuel": "diesel",
        "mileage": "12 kmpl",
        "usage": "family",
        "price": "₹25.00 Lakh",
        "features": "Unmatched reliability, captain seats, great resale value",
        "description": "The ultimate family mover with legendary reliability."
    },
    {
        "name": "Toyota Fortuner",
        "type": "suv",
        "budget_range": "high",
        "fuel": "diesel",
        "mileage": "10 kmpl",
        "usage": "family",
        "price": "₹33.00 Lakh",
        "features": "Massive road presence, reliability, off-road capable",
        "description": "A status symbol SUV known for its indestructibility."
    },
    {
        "name": "Mahindra XUV700",
        "type": "suv",
        "budget_range": "high",
        "fuel": "petrol",
        "mileage": "13 kmpl",
        "usage": "highway",
        "price": "₹26.00 Lakh (Top Model)",
        "features": "ADAS Level 2, twin-screen cockpit, panoramic skyroof",
        "description": "A tech-laden powerhouse that changed the Indian SUV game."
    },
     {
        "name": "Jeep Compass",
        "type": "suv",
        "budget_range": "high",
        "fuel": "diesel",
        "mileage": "15 kmpl",
        "usage": "highway",
        "price": "₹28.00 Lakh",
        "features": "Premium build, great handling, 4x4 options",
        "description": "A premium compact SUV for those who value driving dynamics."
    },
    {
        "name": "MG Gloster",
        "type": "suv",
        "budget_range": "high",
        "fuel": "diesel",
        "mileage": "12 kmpl",
        "usage": "family",
        "price": "₹38.00 Lakh",
        "features": "Massage seats, ADAS, huge interior space",
        "description": "A massive luxury SUV offering features usually found in cars twice its price."
    },
     {
        "name": "BMW 3 Series Gran Limousine",
        "type": "car",
        "budget_range": "high",
        "fuel": "petrol",
        "mileage": "15 kmpl",
        "usage": "city",
        "price": "₹60.00 Lakh",
        "features": "Extended wheelbase, luxury interiors, engaging drive",
        "description": "The perfect entry into luxury sedans with extra legroom."
    },
    # --- SUPER CARS ---
    {
        "name": "Porsche 911 Carrera",
        "type": "car",
        "budget_range": "high", # Ultra High really
        "fuel": "petrol",
        "mileage": "9 kmpl",
        "usage": "highway",
        "price": "₹1.90 Crore",
        "features": "Iconic design, everyday supercar, precision engineering",
        "description": "The definitive sports car that sets the benchmark for performance."
    },
    {
        "name": "Lamborghini Huracan",
        "type": "car",
        "budget_range": "high",
        "fuel": "petrol",
        "mileage": "6 kmpl",
        "usage": "highway",
        "price": "₹4.00 Crore",
        "features": "V10 symphony, striking design, pure adrenaline",
        "description": "A flamboyant supercar that turns heads and shatters lap times."
    },
     {
        "name": "Ferrari 296 GTB",
        "type": "car",
        "budget_range": "high",
        "fuel": "petrol", # Hybrid technically
        "mileage": "12 kmpl (Hybrid)",
        "usage": "highway",
        "price": "₹5.40 Crore",
        "features": "V6 Hybrid, F1 technology, breathtaking speed",
        "description": "The future of Italian supercars, combining emotion with electrification."
    },

    # --- BIKES (High & Superbikes) ---
     {
        "name": "Kawasaki Ninja 650",
        "type": "bike",
        "budget_range": "high",
        "fuel": "petrol",
        "mileage": "21 kmpl",
        "usage": "highway",
        "price": "₹7.16 Lakh",
        "features": "Twin cylinder power, sport-touring comfort, Japanese reliability",
        "description": "A friendly big bike suitable for touring and weekend rides."
    },
    {
        "name": "Kawasaki Z900",
        "type": "bike",
        "budget_range": "high",
        "fuel": "petrol",
        "mileage": "17 kmpl",
        "usage": "highway",
        "price": "₹9.20 Lakh",
        "features": "Inline-4 sound, massive torque, aggressive looks",
        "description": "A proper superbike experience for the street."
    },
     {
        "name": "Suzuki Hayabusa",
        "type": "bike",
        "budget_range": "high",
        "fuel": "petrol",
        "mileage": "11 kmpl",
        "usage": "highway",
        "price": "₹16.90 Lakh",
        "features": "Legendary speed, aero styling, surprisingly comfortable",
        "description": "The Peregrine Falcon of bikes, built for ultimate velocity."
    },
    {
        "name": "Ducati Panigale V4",
        "type": "bike",
        "budget_range": "high",
        "fuel": "petrol",
        "mileage": "10 kmpl",
        "usage": "highway",
        "price": "₹27.00 Lakh",
        "features": "MotoGP derived tech, stunning Italian design, raw power",
        "description": "The closest you can get to a race bike for the road."
    },


    # ==========================
    # EVs (Across Ranges)
    # ==========================
    {
        "name": "Tata Tiago EV",
        "type": "ev",
        "budget_range": "low", # Borderline medium but cheapest EV
        "fuel": "electric",
        "mileage": "250 km (Range)",
        "usage": "city",
        "price": "₹8.69 Lakh",
        "features": "Silent drive, low running cost, compact size",
        "description": "The most affordable electric car, perfect for city commutes."
    },
    {
        "name": "MG Comet EV",
        "type": "ev",
        "budget_range": "low",
        "fuel": "electric",
        "mileage": "230 km (Range)",
        "usage": "city",
        "price": "₹7.98 Lakh",
        "features": "Ultra compact, futuristic design, very easy to park",
        "description": "A quirky urban mobility solution for crowded cities."
    },
    {
        "name": "Tata Nexon EV",
        "type": "ev",
        "budget_range": "medium",
        "fuel": "electric",
        "mileage": "453 km (Range)",
        "usage": "city",
        "price": "₹14.50 Lakh",
        "features": "Fast charging, brave design, connected car tech",
        "description": "India's best-selling electric SUV offering a good balance of range and price."
    },
    {
        "name": "MG ZS EV",
        "type": "ev",
        "budget_range": "high",
        "fuel": "electric",
        "mileage": "461 km (Range)",
        "usage": "highway",
        "price": "₹23.00 Lakh",
        "features": "Panoramic sunroof, ADAS, premium materials",
        "description": "A refined electric SUV suitable for longer trips."
    },
    {
        "name": "BYD Atto 3",
        "type": "ev",
        "budget_range": "high",
        "fuel": "electric",
        "mileage": "521 km (Range)",
        "usage": "highway",
        "price": "₹33.90 Lakh",
        "features": "Rotating screen, funky interior, blade battery safety",
        "description": "A unique and high-tech EV for those who want to stand out."
    },
    {
        "name": "Kia EV6",
        "type": "ev",
        "budget_range": "high",
        "fuel": "electric",
        "mileage": "708 km (Range)",
        "usage": "highway",
        "price": "₹60.95 Lakh",
        "features": "Supercar acceleration, futuristic looks, ultra-fast charging",
        "description": "A flagship EV that showcases the future of driving."
    },
    {
        "name": "Ather 450X",
        "type": "bike", # EV Scooter
        "budget_range": "medium",
        "fuel": "electric",
        "mileage": "150 km (Range)",
        "usage": "city",
        "price": "₹1.40 Lakh",
        "features": "Touchscreen dashboard, fast charging, quick acceleration",
        "description": "A smart electric scooter with premium features and performance."
    },
    {
        "name": "Ola S1 Pro",
        "type": "bike", # EV Scooter
        "budget_range": "medium",
        "fuel": "electric",
        "mileage": "195 km (Range)",
        "usage": "city",
        "price": "₹1.48 Lakh",
        "features": "Huge range, music system, hyper mode",
        "description": "A high-performance electric scooter with distinct styling."
    }
]
