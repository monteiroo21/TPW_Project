from app.models import *

def creategroups():
    Group(
        name="BMW Group",
        email="info@bmw.pt",
        country="Germany",
        website="https://www.bmwgroup.com/en.html",
        headquarters="static/imgs/bmw-headquarter.png"
    ).save()
    
    Group(
        name="Volkswagen Group",
        email="vw@volkswagen.de",
        country="Germany",
        website="https://www.volkswagen-group.com/en",
        headquarters="static/imgs/volkswagen-headquarter.png"
    ).save()
    
    Group(
        name="Mercedes-Benz Group",
        email="me-connect.prt@cac.mercedes-benz.com",
        country="Germany",
        website="https://group.mercedes-benz.com/en/",
        headquarters="static/imgs/mercedes-headquarter.png"
    ).save()
    
    Group(
        name="Toyota Motor Corporation Group",
        email="servicocliente@toyota-fs.com",
        country="Japan",
        website="https://global.toyota/en/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Tata Motors Group",
        email="cac@tatamotors.com",
        country="India",
        website="https://www.tatamotors.com/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Aston Martin",
        email="dan.connell@astonmartin.com",
        country="United Kingdom",
        website="https://www.astonmartin.com/en",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Ferrari",
        email="customercare@ferraristore.com",
        country="Italy",
        website="https://www.ferrari.com/en-PT",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Stellantis Group",
        email="jorge.magalhaes@stellantis.com",
        country="Netherlands",
        website="https://www.stellantis.com/en"
    ).save()
    
    Group(
        name="Tesla",
        email="eupress@tesla.com",
        country="United States of America",
        website="https://www.tesla.com/pt_pt",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="McLaren",
        email="guest.relations@mclaren.com",
        country="United Kingdom",
        website="https://www.mclaren.com/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Piaggio Group",
        email="geral@cmachado.pt",
        country="Italy",
        website="https://www.piaggio.com/pt_PT/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Polaris Group",
        email="privacy@polaris.com",
        country="United States",
        website="https://www.polarisportugal.com/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Pierer Group",
        email="privacy@piererindustrie.com",
        country="Austria",
        website="https://www.pierermobility.com/en",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Eicher Motors Group",
        email="info@eichermotors.com",
        country="India",
        website="https://eicher.in/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Harley-Davidson",
        email="privacy@harley-davidson.com",
        country="United States",
        website="https://www.harley-davidson.com/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Triumph",
        email="info@triumphmotorcycles.com",
        country="United Kingdom",
        website="https://www.triumphmotorcycles.com/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="MV Agusta",
        email="info@mvagusta.com",
        country="Italy",
        website="https://www.mvagusta.com/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    

    Group(
        name="TVS Motor Company",
        email="info@tvsmotor.com",
        country="Chennai",
        website="https://www.tvsmotor.com/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Norton Motorcycles Group",
        email="customer.data@nortonmotorcycles.com",
        country="United Kingdom",
        website="https://nortonmotorcycles.com/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()
    
    Group(
        name="Bimota",
        email="info@bimotaportugal.pt",
        country="Italy",
        website="https://bimotaportugal.pt/",
        headquarters="static/imgs/toyota-headquarter.png"
    ).save()


def createBrandMota():
    Brand(
    name="Ducati",
    email="privacy@ducati.com",
    country="Italy",
    website="https://www.ducati.com/",
    cellPhone="+5113870967",
    group=Group.objects.get(name__icontains='Volk'),
    description="",
    logo="static/imgs/Ducati_red_logo.png",
    ).save()
    Brand(
    name="Harley-Davidson",
    email="DataPrivacy@Harley-Davidson.com",
    country="United States",
    website="https://investor.harley-davidson.com/",
    cellPhone="+137053208",
    group=Group.objects.get(name__icontains='Harley-Davidson'),
    description="",
    logo="static/imgs/Harley-Davidson.png",
    ).save()

    Brand(
    name="BMW Motorrad",
    email="info@bmwMotorrad.pt",
    country="Germany",
    website="https://www.bmw-motorrad.pt/pt/home.html#/filter-todos",
    cellPhone="808200807",
    group=Group.objects.get(name__icontains='BMW'),
    description="",
    logo="static/imgs/BMW-Logo-1963.png",
    ).save()

    Brand(
    name="Triumph",
    email="info@triumphmotorcycles.com",
    country="united kingdom",
    website="https://www.triumphmotorcycles.com/",
    cellPhone="+447700900123",
    group=Group.objects.get(name__icontains='Triumph'),
    description="",
    logo="static/imgs/Triumph.png",
    ).save()

    Brand(
    name="MV Agusta",
    email="info@mvagusta.co",
    country="Italy",
    website="https://www.mvagusta.com/pt/pt",
    cellPhone="12345678765432",
    group=Group.objects.get(name__icontains='MV Agusta'),
    description="",
    logo="static/imgs/MV_Agusta_Logo.png",
    ).save()

    Brand(
    name="Indian Motorcycle",
    email="privacy@polaris.com",
    country="United States",
    website="https://www.indianmotorcycle.pt/",
    cellPhone="23456543216",
    group=Group.objects.get(name__icontains='Polaris'),
    description="",
    logo="static/imgs/Indian_Motorcycle_logo.png",
    ).save()

    Brand(
    name="Aprilia",
    email="geral@apriliapt.com",
    country="Italy",
    website="https://www.aprilia.com/pt_PT/",
    cellPhone="219609110",
    group=Group.objects.get(name__icontains='Piaggio'),
    description="",
    logo="static/imgs/Aprilia_Racing_NERO+ROSSO_Regist.png",
    ).save()

    Brand(
    name=" Moto Guzzi",
    email="geral@cmachado.pt",
    country="Italy",
    website="https://www.motoguzzi.com/pt_PT/",
    cellPhone="219709311",
    group=Group.objects.get(name__icontains='Piaggio'),
    description="",
    logo="static/imgs/moto-guzzi-logo-2007-present-scaled.png",
    ).save()


def createBrandCarro():
    # Criação de McLaren
    Brand(
    name="McLaren",
    email="guest.relations@mclaren.com",
    country="United Kingdom",
    website="https://www.mclaren.com/",
    cellPhone="+4407387548",
    group=Group.objects.get(name__icontains='McLaren'),
    description="McLaren is a British luxury automotive manufacturer celebrated for its high-performance supercars, cutting-edge technology, and motorsport heritage. Founded in 1963 by racing driver Bruce McLaren, the brand first gained prominence in Formula 1, where it became one of the most successful teams in motorsport history. McLaren Automotive, the company’s road car division launched in 2010, continues to leverage this expertise to create world-class sports cars and supercars, including models like the 720S, GT, Artura, and limited-edition hypercars such as the P1, Speedtail, and Elva.\n\nMcLaren cars are known for their lightweight, aerodynamic designs, often featuring a carbon-fiber monocoque chassis that enhances performance and handling. Equipped with twin-turbocharged V8 engines, as well as hybrid powertrains in select models, McLaren vehicles offer a thrilling blend of speed, agility, and precise control. The brand’s interiors are crafted with a driver-first approach, using premium materials and minimalist design elements to create an immersive, race-inspired driving experience.\n\nWith a commitment to innovation and technology, McLaren continuously introduces features that enhance performance and efficiency, such as active aerodynamics and cutting-edge suspension systems. Known for its distinct papaya orange racing color and iconic dihedral doors, McLaren appeals to automotive enthusiasts who seek a vehicle that combines track-level performance with refined luxury and engineering precision. Driven by a passion for speed and innovation, McLaren remains a symbol of British engineering excellence and is highly regarded among supercar aficionados.",
    logo="static/imgs/mcl-removebg-preview.png",
).save()

# Criação de Bugatti
    Brand(
    name="Bugatti",
    email="nicole.auger@bugatti.com",
    country="France",
    website="https://www.bugatti.com/",
    cellPhone="+491512521371",
    group=Group.objects.get(name__icontains='Volkswagen Group'),
    description="Bugatti is a French luxury automotive brand known for producing some of the world’s most exclusive, high-performance hypercars. Founded in 1909 by Italian-born Ettore Bugatti, the brand quickly earned a reputation for precision engineering, advanced technology, and artistic design, with an emphasis on speed and luxury. Today, Bugatti is renowned for setting speed records and pushing the boundaries of automotive engineering, creating iconic models like the Veyron, Chiron, and, more recently, the Centodieci, Bolide, and Mistral.\n\nBugatti cars are meticulously handcrafted, featuring powerful quad-turbocharged W16 engines, advanced aerodynamics, and a refined yet aggressive design. The brand’s hypercars are known for their ability to reach extraordinary speeds — with some models exceeding 300 mph — while offering a smooth, controlled driving experience. Interiors are crafted from the highest-quality materials, such as fine leathers, carbon fiber, and aluminum, combining comfort with an unmistakably luxurious feel.\n\nWith its signature horseshoe grille and sleek lines, Bugatti’s design is instantly recognizable, symbolizing exclusivity, heritage, and performance. Now part of Bugatti Rimac, the brand continues to innovate and experiment with hybrid and electric technologies, aiming to preserve its legacy as the epitome of luxury and performance for a discerning clientele who seek rarity, craftsmanship, and extreme capability. Bugatti’s vehicles are prized by collectors and enthusiasts worldwide, representing the pinnacle of automotive achievement.",
    logo="static/imgs/Bugatti_logo.png",
).save()
# Criação de Tesla
    Brand(
    name="Tesla",
    email="eupress@tesla.com",
    country="United States of America",
    website="https://www.tesla.com/pt_pt",
    cellPhone="+8777983752",
    group=Group.objects.get(name__icontains='Tesla'),
    description="Tesla is an American electric vehicle (EV) and clean energy company known for its groundbreaking innovation, advanced technology, and commitment to sustainability. Founded in 2003 by Martin Eberhard and Marc Tarpenning, with Elon Musk joining shortly thereafter, Tesla has transformed the automotive industry by making EVs mainstream and pushing boundaries in electric range, performance, and autonomous driving capabilities. The brand’s lineup includes popular models such as the Model S sedan, Model 3 compact sedan, Model X SUV, and Model Y crossover, each designed to provide high performance, impressive range, and advanced technological features.\n\nTesla vehicles are equipped with minimalist, high-tech interiors dominated by a central touchscreen that controls most of the vehicle’s functions, including navigation, entertainment, and climate. Tesla’s Autopilot and Full Self-Driving (FSD) features offer advanced driver-assistance capabilities, positioning Tesla at the forefront of autonomous vehicle technology. The brand is also known for over-the-air software updates that continually improve vehicle performance and add new features, providing a unique experience in the automotive industry.\n\nTesla’s commitment to sustainability extends beyond its vehicles, with products like the Tesla Powerwall and Solar Roof aiming to create a full ecosystem of clean energy solutions. The brand’s focus on innovation, sustainability, and technological advancement appeals to drivers looking for an eco-friendly, performance-oriented vehicle with cutting-edge features, reshaping the future of transportation and energy usage.",
    logo="static/imgs/Tesla_logo.png",
).save()

# Criação de Maserati
    Brand(
    name="Maserati",
    email="info@maserati.com",
    country="Italia",
    website="https://www.maserati.com/pt/pt",
    cellPhone="+390244412899",
    group=Group.objects.get(name__icontains='Stellantis Group'),
    description="Maserati is an Italian luxury automobile manufacturer celebrated for its unique combination of Italian style, performance, and elegance. Founded in 1914 by the Maserati brothers, the brand has a rich racing heritage and a reputation for producing sophisticated, high-performance vehicles that blend luxury with a touch of sportiness. Maserati’s lineup includes models like the Ghibli and Quattroporte sedans, the Levante SUV, and the MC20 supercar, each offering a refined driving experience with Italian flair.\n\nMaserati vehicles are distinguished by their luxurious interiors and high-quality materials, featuring a driver-focused cockpit and a balance of modern technology with classic design elements. Known for their powerful engines and distinct exhaust notes, Maserati cars deliver a spirited performance, often powered by Ferrari-engineered V6 and V8 engines that offer an exhilarating and unmistakable sound.\n\nThe brand’s trident logo, inspired by the Neptune Fountain in Bologna, symbolizes strength and vigor, aligning with Maserati’s commitment to performance and prestige. Now under Stellantis, Maserati is expanding its portfolio to include hybrid and electric models, such as the Grecale and the all-electric Folgore series, reflecting the brand's dedication to the future of sustainable luxury. Maserati continues to appeal to drivers who appreciate Italian craftsmanship, a unique driving experience, and an elegant yet athletic design that stands out in the luxury automotive world.",
    logo="static/imgs/maseratilogo.png",
).save()

# Criação de Lamborghini
    Brand(
    name="Lamborghini",
    email="info@lamborghini.com",
    country="Italia",
    website="https://www.lamborghini.com/en-en",
    cellPhone="+390519597282",
    group=Group.objects.get(name__icontains='Volkswagen Group'),
    description="Lamborghini is a legendary Italian luxury sports car manufacturer known for its bold designs, exceptional performance, and distinctive, aggressive styling. Founded in 1963 by Ferruccio Lamborghini, the brand was initially created to rival Ferrari and quickly gained fame for its powerful engines, groundbreaking designs, and daring aesthetics. Lamborghini’s lineup includes models like the Aventador, Huracán, and the high-performance Urus SUV, each embodying the brand’s ethos of delivering thrilling power and head-turning style.\n\nLamborghini cars are defined by their sharp, angular lines, low-slung profiles, and signature scissor doors, particularly on models like the Aventador. The interiors are crafted with a luxurious yet race-inspired focus, incorporating high-quality materials such as Alcantara and carbon fiber, along with advanced infotainment systems that keep the driver connected. Lamborghini is known for its high-revving V10 and V12 engines, which provide unmistakable roars and exceptional acceleration, offering an intense and exhilarating driving experience.\n\nOwned by the Volkswagen Group under Audi, Lamborghini continues to innovate, integrating hybrid and electric technologies while preserving its tradition of uncompromising performance and style. The brand’s logo, a raging bull, reflects Lamborghini’s spirit of power, aggressiveness, and a strong personality, appealing to those who seek an unmistakable blend of luxury and performance wrapped in a dramatic and distinctive design.",
    logo="static/imgs/Lamborghini-Logo.png",
).save()

# Criação de Ferrari
    Brand(
    name="Ferrari",
    email="customercare@ferraristore.com",
    country="Italia",
    website="https://www.ferrari.com/en-PT",
    cellPhone="+390536949111",
    group=Group.objects.get(name__icontains='Ferrari'),
    description="Ferrari is an iconic Italian luxury sports car manufacturer known worldwide for its exceptional performance, design, and motorsport legacy. Founded in 1939 by Enzo Ferrari, the brand has become synonymous with speed, precision engineering, and Italian craftsmanship. Ferrari’s models, such as the 488 GTB, F8 Tributo, Portofino, and the flagship LaFerrari, are characterized by their distinctive styling, powerful engines, and aerodynamic designs, delivering exhilarating driving experiences both on the road and on the racetrack.\n\nFerrari’s vehicles are meticulously crafted with a focus on both aesthetics and functionality, featuring lightweight materials, sophisticated aerodynamics, and advanced engineering that optimize performance. The interiors of Ferrari cars are tailored for drivers, incorporating high-end materials like carbon fiber, leather, and Alcantara, with a minimalist layout that places essential controls within easy reach. Known for its V8 and V12 engines, Ferrari has a long tradition of creating high-revving, naturally aspirated engines, although recent models are incorporating turbocharging and hybrid technology to enhance performance and efficiency.\n\nFerrari’s deep roots in motorsports, particularly Formula 1, play a crucial role in its engineering advancements, often inspiring innovations in its road cars. The brand is also distinguished by its prancing horse emblem, symbolizing passion, luxury, and exclusivity. Reserved for those who seek unparalleled performance and timeless design, Ferrari remains a dream car for enthusiasts worldwide, delivering vehicles that embody the spirit of speed and Italian craftsmanship.",
    logo="static/imgs/Ferrari-Emblem.png",
).save()
# Aston Martin
    Brand(
    name="Aston Martin",
    email="dan.connell@astonmartin.com",
    country="United Kingdom",
    website="https://www.astonmartin.com/en",
    cellPhone="+44170751291",
    group=Group.objects.get(name__icontains='Aston Martin'),
    description="Aston Martin is a prestigious British luxury sports car manufacturer celebrated for its timeless design, refined performance, and association with elegance and exclusivity. Founded in 1913 by Lionel Martin and Robert Bamford, Aston Martin gained global recognition as a brand symbolizing British luxury and high-performance craftsmanship. The company’s iconic models, such as the DB series (DB5, DB11), Vantage, and flagship DBS, combine powerful engines with sleek, aerodynamic design, capturing the essence of both performance and sophistication. Known for its association with James Bond films, particularly the DB5, Aston Martin has established a strong cultural presence and a reputation for blending luxury with high-speed performance. The brand's vehicles are crafted with precision, featuring premium materials, hand-finished interiors, and a driver-centric layout that emphasizes comfort and style. Each Aston Martin model balances cutting-edge engineering with a sense of heritage and tradition, resulting in cars that deliver both thrilling performance and refined luxury. Aston Martin also offers personalization options, allowing clients to tailor details to their tastes, reinforcing its exclusivity and appeal among discerning drivers. With a commitment to innovation and sustainability, Aston Martin has expanded into hybrid and electric technology, aiming to preserve its luxury and performance legacy while embracing modern demands.",
    logo="static/imgs/aston-martin-logo.png"
).save()

# Range Land Rover
    Brand(
    name="Range Land Rover",
    email="cs_landrover@cetelem.pt",
    country="United Kingdom",
    website="https://www.landrover.pt/range-rover/range-rover-sport/index.html?utm_source=googlepmax&utm_medium=CXNW&utm_campaign=pt_nv_rr_rrs_all_suv_my24_pt_gmc1065_thk_trf_googlepmax_pm_2410_googlepmax_mul_inte",
    cellPhone="+351217246717",
    group=Group.objects.get(name__icontains='Tata Motors'),
    description="Land Rover, and its luxury division Range Rover, are iconic British brands known for producing some of the world’s most prestigious and capable luxury SUVs. Land Rover was founded in 1948, initially creating rugged, utilitarian vehicles designed for off-road use. Range Rover, introduced as a luxury line within Land Rover in 1970, redefined the market by combining off-road prowess with refined luxury, setting the standard for premium SUVs. Range Rover’s lineup includes the flagship Range Rover, as well as the Range Rover Sport, Range Rover Velar, and the compact Range Rover Evoque. These vehicles are known for their blend of robust off-road capabilities, advanced technology, and opulent interiors, featuring high-quality materials, plush seating, and state-of-the-art infotainment. Range Rover’s design is both modern and timeless, with a distinctive floating roof, clamshell hood, and sophisticated lines that have become instantly recognizable. With features like Terrain Response, adjustable air suspension, and powerful engines, Range Rovers handle a variety of terrains with ease while providing a smooth, comfortable ride on highways. Now under Jaguar Land Rover, owned by Tata Motors, Range Rover continues to push the boundaries of luxury and utility, appealing to those who seek a refined yet versatile vehicle that performs equally well in urban environments and rugged landscapes.",
    logo="static/imgs/Land-Rover-Range-Rover-Logo.png"
).save()

# Jaguar
    Brand(
    name="Jaguar",
    email="info@infojaguar.pt",
    country="United Kingdom",
    website="https://www.jaguarportugal.pt/index.html",
    cellPhone="+4401926641",
    group=Group.objects.get(name__icontains='Tata Motors'),
    description="Jaguar is a British luxury car brand renowned for its blend of elegance, performance, and iconic design. Founded in 1922, Jaguar began as a manufacturer of motorcycle sidecars before transitioning into the automotive industry, where it became known for producing sports cars and luxury sedans with a distinctive style. Jaguar models, such as the F-Type sports car, XE sedan, and F-Pace SUV, are celebrated for their sleek lines, powerful engines, and agile handling, capturing the essence of both luxury and performance. Jaguar is recognized for its craftsmanship and luxurious interiors, featuring premium materials, cutting-edge technology, and a driver-centric layout that provides comfort and sophistication. The brand has also taken steps towards sustainability and innovation with its all-electric I-PACE, one of the world’s first all-electric luxury SUVs, reflecting Jaguar’s commitment to the future of electric mobility. With a legacy that includes notable models like the E-Type, often hailed as one of the most beautiful cars ever made, Jaguar combines British refinement with a sporty edge, appealing to those who seek a dynamic driving experience with a touch of elegance. Now part of Jaguar Land Rover under Tata Motors, Jaguar continues to innovate while honoring its heritage, offering a range of vehicles that embody both luxury and exhilarating performance.",
    logo="static/imgs/Jaguar-Logo.png"
).save()

# Lexus
    Brand(
    name="Lexus",
    email="apoio.tecnico.lexus@lexus.pt",
    country="Japan",
    website="https://www.lexus.pt/novos/lbx/reserva-online?utm_medium=search&utm_source=google&utm_campaign=caetsu_lex_lbx_per_always-on_launch_11.23_pt_lp_autnv_21469-pt-per&utm_content=text_product_pros_kw&utm_t",
    cellPhone="+441737500024",
    group=Group.objects.get(name__icontains='Toyota'),
    description="Lexus is the luxury vehicle division of Toyota, known for its high-quality craftsmanship, innovative technology, and smooth, quiet performance. Founded in 1989, Lexus quickly gained a reputation for exceptional reliability, luxury, and refinement, competing with established European luxury brands. The brand's lineup includes elegant sedans like the ES and LS, high-performance F series models, and popular SUVs such as the RX and NX. Lexus has also embraced hybrid technology, offering hybrid versions of many models, like the RX Hybrid and ES Hybrid, showcasing its commitment to sustainability without compromising luxury. Lexus vehicles are distinguished by their meticulous attention to detail, combining premium materials and comfort-focused interiors with advanced features and driver-assistance systems. Lexus also introduced the 'Spindle Grille,' a signature design element that lends a distinctive and recognizable look to its cars. Known for delivering a comfortable, refined ride, Lexus prioritizes a quiet and smooth driving experience, appealing to those who value reliability, innovation, and a balance of performance and luxury. Blending Japanese craftsmanship with advanced technology, Lexus continues to grow its global presence by delivering high-end vehicles that emphasize quality, durability, and understated elegance, making it a preferred choice for those seeking luxury with a focus on reliability and innovation.",
    logo="static/imgs/lexuslog.png"
).save()

# Porsche
    Brand(
    name="Porsche",
    email="contact@porsche.pt",
    country="Germany",
    website="https://www.porsche.com/portugal/",
    cellPhone="+800911356",
    group=Group.objects.get(name__icontains='Volkswagen'),
    description="Porsche is a prestigious German automobile manufacturer known for producing high-performance sports cars, luxury vehicles, and SUVs that combine innovation, speed, and timeless design. Founded in 1931 by Ferdinand Porsche, the brand is globally recognized for its engineering excellence, precision, and dedication to motorsports heritage. The Porsche 911, one of the brand's most iconic models, has become synonymous with high-performance and agility, setting standards in the sports car category for over half a century. Porsche’s lineup includes a range of vehicles that appeal to performance enthusiasts and luxury seekers alike, from the Boxster and Cayman to the Cayenne and Macan SUVs, blending power with practicality. Porsche has also been a pioneer in hybrid and electric technology with models like the Panamera Hybrid and the fully electric Taycan, demonstrating its commitment to sustainability while retaining the brand’s performance ethos. Porsche’s interiors are crafted with a focus on both driver ergonomics and luxury, featuring premium materials, advanced infotainment systems, and a cockpit-like design that enhances the driving experience. Known for its rear-engine layout, meticulous craftsmanship, and engineering innovation, Porsche continues to attract drivers who appreciate a blend of luxury and performance and a rich motorsport legacy, delivering cars that excel both on the track and the road.",
    logo="static/imgs/Porsche-Logo.png"
).save()

# Audi
    Brand(
    name="Audi",
    email="apoio.clientes@siva.pt",
    country="Germany",
    website="https://www.audi.pt/",
    cellPhone="+800308030",
    group=Group.objects.get(name__icontains='Volkswagen'),
    description="Audi is a German luxury automobile brand known for its modern design, advanced technology, and superior engineering, with a brand philosophy captured by its slogan, 'Vorsprung durch Technik' (Progress through Technology). Founded in 1909 and now part of the Volkswagen Group, Audi has developed a reputation for producing vehicles that blend performance with refinement, featuring advanced engineering, sophisticated design, and all-wheel-drive systems like its renowned Quattro technology. Audi’s lineup spans a variety of vehicles, from sleek sedans like the A4 and A8 to high-performance RS models and popular SUVs like the Q series. Audi has also been at the forefront of electric vehicle innovation with its e-tron series, making strides in sustainable luxury with models like the Q8",
    logo="static/imgs/audilogo.png"
).save()
    
# Criação de BMW
    Brand(
    name="BMW",
    email="info@bmw.pt",
    country="Germany",
    website="https://www.bmw.pt/pt/index.html?clc=4g0aa010H1d01&&tl=sea-gl-PT_BMW_NC_BRAND%20PURE_POR_BND_ALO_%20_PERF_%20_SEAADW-mix-miy-.-sech-BRA_BND_BRAND%20PURE_MULTI_NONE-.-e-bmw-.-.&gad_source=1&gclid=Cj0KC",
    cellPhone="+4987170217001",
    group=Group.objects.get(name__icontains='BMW Group'),
    description="BMW (Bayerische Motoren Werke), founded in 1916 in Germany, is a prestigious automotive brand known for producing high-performance luxury vehicles that emphasize driving dynamics, innovation, and engineering precision. Originally an aircraft engine manufacturer, BMW has evolved into one of the world’s leading luxury car brands, with its 'Ultimate Driving Machine' motto reflecting its dedication to crafting vehicles with exceptional handling, power, and driver engagement.\n\nBMW's lineup includes a wide range of vehicles, from sporty sedans like the 3 Series to luxury SUVs in the X lineup, high-performance M models, and forward-thinking electric vehicles (EVs) in the i series. The brand's interiors blend premium materials and sophisticated technology, offering drivers a modern, connected, and comfortable experience. Known for innovations in both internal combustion and electric engines, BMW also emphasizes sustainability and is committed to expanding its EV lineup with models like the iX and i4.\n\nBMW's iconic kidney grille and distinct design language make it instantly recognizable, appealing to drivers who value a balance of luxury, sportiness, and cutting-edge tech. Through its meticulous engineering, BMW continues to be a global leader in automotive performance, style, and innovation.",
    logo="static/imgs/BMW-Logo-1963.png",
).save()

# Criação de Mercedes-Benz
    Brand(
    name="Mercedes-Benz",
    email="me-connect.prt@cac.mercedes-benz.com",
    country="Germany",
    website="https://www.mercedes-benz.pt/",
    cellPhone="+497111701",
    group=Group.objects.get(name__icontains='Mercedes-Benz Group'),
    description="Mercedes-Benz, often simply known as Mercedes, is a globally recognized German luxury automobile brand synonymous with quality engineering, innovation, and elegance. Founded in 1926, the brand has a rich history of automotive advancement and has been a pioneer in safety features, performance, and design. Mercedes-Benz offers a diverse range of vehicles, from luxurious sedans like the S-Class to high-performance AMG models, cutting-edge electric vehicles (EVs) in the EQ lineup, and robust SUVs such as the G-Class.\n\nRenowned for its innovation, Mercedes consistently integrates the latest technology into its vehicles, including advanced driver-assistance systems, premium infotainment, and connectivity features. The brand is also known for its refined interiors, which feature high-quality materials and meticulous craftsmanship, aiming to provide both driver and passengers with a comfortable, immersive experience. As a luxury automotive leader, Mercedes-Benz continues to shape the industry by emphasizing performance, luxury, and sustainability, appealing to a broad range of consumers who prioritize elegance, innovation, and status in their driving experience.",
    logo="static/imgs/Mercedes-Logo.png",
).save()

# Criação de Bentley
    Brand(
    name="Bentley",
    email="service@bentley.com",
    country="United Kingdom",
    website="https://www.bentleymotors.com/en.html",
    cellPhone="+4401270653",
    group=Group.objects.get(name__icontains='Volkswagen Group'),
    description="Bentley is a prestigious British luxury automobile manufacturer renowned for its blend of opulence, performance, and heritage. Founded in 1919 by W.O. Bentley, the brand initially gained fame for producing high-performance cars that dominated early motorsport events, notably the 24 Hours of Le Mans. Bentley's models, such as the Continental GT, Flying Spur, and Bentayga SUV, showcase the brand's commitment to refined luxury, cutting-edge technology, and impressive power.\n\nBentley's interiors are crafted with attention to detail, using premium materials like fine leathers, woods, and metals, often customizable to suit individual preferences. The brand has a legacy of merging British craftsmanship with powerful engineering, resulting in vehicles that offer a dynamic driving experience without compromising comfort. Owned by the Volkswagen Group since 1998, Bentley continues to stand as a symbol of distinguished style, merging classic luxury with modern innovation to appeal to drivers who seek both performance and exclusivity.",
    logo="static/imgs/bentley-logo-white.png",
).save()

# Criação de Rolls-Royce
    Brand(
    name="Rolls-Royce",
    email="enquiries@rolls-roycemotorcars.com",
    country="United Kingdom",
    website="https://www.rolls-roycemotorcars.com/en_GB/home.html",
    cellPhone="4401243525700",
    group=Group.objects.get(name__icontains='BMW Group'),
    description="Rolls-Royce is a renowned British luxury automobile brand recognized for its meticulous craftsmanship, opulence, and exclusivity. Founded in 1904 by Charles Rolls and Henry Royce, the company quickly gained a reputation for engineering excellence and precision. Its models, including the Phantom, Ghost, and Wraith, are often seen as symbols of wealth, status, and sophistication, featuring hand-crafted interiors, high-quality materials, and powerful yet smooth engines that provide a remarkably quiet and refined driving experience.\n\nThe brand has a legacy of blending traditional elegance with cutting-edge technology, maintaining a strong focus on bespoke services where each vehicle is tailored to the specific tastes and desires of the client. Rolls-Royce cars are known for their iconic 'Spirit of Ecstasy' hood ornament, which embodies the brand’s dedication to artistry and luxury. Owned by BMW since 1998, Rolls-Royce continues to set high standards in the automotive industry, with vehicles that epitomize luxury and timeless design.",
    logo="static/imgs/rollsroyce-logo-white.png",
).save()


def createMotas():
    # car_model = CarModel(brand=brand, name="Generic Car", base_price=20000, specifications="Standard car", releaseYear=2023).save()
    # car = Car.objects.create(model=car_model, year=2023, new=True, kilometers=0, price=21000)
    print(Brand.objects.get(name__icontains='Ducati'))
    moto_model = CarModel(brand=Brand.objects.get(name__icontains='Ducati'),
    name="SCRAMBLER DUCATI 10°anniversario RIZOMA EDITION",
    base_price=13000,
    specifications="4.3″ TFT color display, ride by wire, full LED lighting system, USB socket under the seat, variable section low handlebar, black exhaust manifold and silencer, Ducati Performance LED turn indicators*, sporty tail, bar-end rearview mirrors, dedicated seat, dedicated livery, Rizoma billet aluminium componentry (clutch and front brake levers, clutch and front brake master cylinder caps, fuel tank cap, passenger footpegs), Rizoma billet aluminium componentry in Metal Rose finishing (windscreen, timing belt covers, frame covers, engine inspection covers, rider footpegs)",
    releaseYear=2014)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=2024, new=True,
    kilometers=0, price=16000,
    image="static\imgs\motos\Scrambler-Rizoma-MY25-Model-Blocks-3-4-630x390.png"
    ).save()

    moto_model = CarModel(brand=Brand.objects.get(name__icontains='Ducati'),
    name="Multistrada V4",
    base_price=20680,
    specifications="The new Multistrada V4 MY2025 combines an optimised aerodynamic design for greater protection, fuel-saving technology, and a heightened anti-squat effect for more stable riding. With new riding modes and increased passenger comfort, this motorcycle is ready to redefine every journey",
    releaseYear=2020)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=2021, new=False, kilometers=12000, price=17800,
    image="static\imgs\motos\Multistrada-V4-MY25-Model-Blocks-3-4-630x390.png").save()


    moto_model = CarModel(brand=Brand.objects.get(name__icontains='BMW Motorr'),
    name="F 900 XR",
    base_price=14597.98,
    specifications="A XR representa a conjugação perfeita entre carácter desportivo e aptidão para longas viagens: adrenalina dia após dia, curva após curva.\n Com a nova F 900 XR, desfrutas das curvas do princípio ao fim, quilómetro após quilómetro. O seu apelativo design é um reflexo das prestações em estado puro. Além disso, a posição de condução descontraída e direita, bem como a proteção aerodinâmica e as condições meteorológicas, indicam que és tu quem decide quando termina a viagem.",
    releaseYear=2023)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=2024, new=True,
    kilometers=0, price=14597.98,
    image="static\imgs\motos\Fx.png"
    ).save()


    moto_model = CarModel(brand=Brand.objects.get(
        name__icontains='BMW Motorr'),
    name="C 400 X",
    base_price=8826.36,
    specifications="O design revela bem a agilidade da C 400 X. Ruas estreitas, tráfego intenso? As carenagens em forma de V transmitem o dinamismo e agilidade em cada linha, refletindo a imagem de leveza e ligeireza desta Scooter. Os genes vigorosos da GS estão bem evidentes: proporções altas, para-lamas da roda dianteira sugestivo, farol assimétrico de grande dimensão, com tecnologia LED integral e ainda com a opcional luz diurna LED em formato de Y na posição horizontal.",
    releaseYear=2018)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=2023, new=True,
    kilometers=0, price=8826.36,
    image="static\imgs\motos\C400.png"
    ).save()


    moto_model = CarModel(brand=Brand.objects.get(
        name__icontains='Triumph'),
    name="TF 450-RC",
    base_price=10995.00,
    specifications="All-new, Triumph’s first 450cc competition powertrain is compact, mass-optimized and built to take the holeshot. Engineering, design, and equipment working in harmony for class-leading power, control, and flexibility. The TF 450-RC is ready to compete at the highest level.",
    releaseYear=2018)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=2024, new=True,
    kilometers=0, price=10995.00,
    image="static\imgs\motos\TF450.png"
    ).save()


    moto_model = CarModel(brand=Brand.objects.get(name__icontains='Triumph'),
    name="ROCKET 3 STORM R",
    base_price=24995.00,
    specifications="With interchangeable R and GT foot controls, rider and passenger seats for tailored ergonomics, plug and play technology for greater convenience, styling parts to customize the look, and luggage solutions for longer rides, there are more than 50 genuine Triumph accessories available to create your perfect Rocket",
    releaseYear=2018)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=2024, new=True,
    kilometers=0, price=24995.00,
    image="static\imgs\motos\R3.png"
    ).save()


    moto_model = CarModel(brand=Brand.objects.get(name__icontains='MV Agusta'),
    name="F3",
    base_price=17.490,
    specifications="A R leva todas as características da F3 ao extremo com linhas desenhadas para proporcionar o máximo desempenho e projetadas para o futuro. O estilo e o desempenho atingem a sua derradeira expressão no contraste entre a carenagem vermelha e os componentes todos pretos.",
    releaseYear=2018)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=2024, new=True,
    kilometers=0, price=17.490,
    image="static\imgs\motos\F3.png"
    ).save()


    moto_model = CarModel(brand=Brand.objects.get(name__icontains='MV Agusta'),
    name="SuperVeloce",
    base_price=22975,
    specifications="",
    releaseYear=2020)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=2024, new=True,
    kilometers=0, price=22975,
    image="static\imgs\motos\superV.png"
    ).save()


    moto_model = CarModel(brand=Brand.objects.get(name__icontains='Indian'),
    name="Indian Springfield",
    base_price=30290,
    specifications="",
    releaseYear=2018)
    moto_model.save()
    Moto.objects.create(model=moto_model, year=30290, new=True,
    kilometers=0, price=16000,
    image="static\imgs\motos\springfield-black-titanium.png"
    ).save()


    # Aprilia Motos
    moto_model_aprilia_1 = CarModel(
        brand=Brand.objects.get(name__icontains='Aprilia'),
        name="Aprilia RS 660",
        base_price=10300,
        specifications="Sport bike with a parallel-twin engine, 100 hp, lightweight chassis.",
        releaseYear=2020
    )
    moto_model_aprilia_1.save()
    Moto.objects.create(
        model=moto_model_aprilia_1,
        year=2020,
        new=True,
        kilometers=0,
        price=10300,
        image="static/imgs/motos/aprilia_rs660.png"
    ).save()

    moto_model_aprilia_2 = CarModel(
        brand=Brand.objects.get(name__icontains='Aprilia'),
        name="Aprilia Tuono 1100",
        base_price=15500,
        specifications="Naked bike with 175 hp, advanced electronics, and adjustable suspension.",
        releaseYear=2021
    )
    moto_model_aprilia_2.save()
    Moto.objects.create(
        model=moto_model_aprilia_2,
        year=2021,
        new=True,
        kilometers=0,
        price=15500,
        image="static/imgs/motos/aprilia_tuono1100.png"
    ).save()

    # Moto Guzzi Motos
    moto_model_guzzi_1 = CarModel(
        brand=Brand.objects.get(name__icontains='Moto Guzzi'),
        name="Moto Guzzi V85 TT",
        base_price=12500,
        specifications="Adventure bike with 80 hp, capable off-road and comfortable touring.",
        releaseYear=2020
    )
    moto_model_guzzi_1.save()
    Moto.objects.create(
        model=moto_model_guzzi_1,
        year=2020,
        new=True,
        kilometers=0,
        price=12500,
        image="static/imgs/motos/moto_guzzi_v85tt.png"
    ).save()

    moto_model_guzzi_2 = CarModel(
        brand=Brand.objects.get(name__icontains='Moto Guzzi'),
        name="Moto Guzzi California Touring 1400",
        base_price=19000,
        specifications="Cruiser with 96 hp, classic design, and great touring comfort.",
        releaseYear=2017
    )
    moto_model_guzzi_2.save()
    Moto.objects.create(
        model=moto_model_guzzi_2,
        year=2017,
        new=False,
        kilometers=12000,
        price=18000,
        image="static/imgs/motos/moto_guzzi_california1400.png"
    ).save()
