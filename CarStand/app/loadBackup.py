from CarStand.app.models import Brand, Group


def loadMota():
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
    email="",
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

    Brand(
    name="KTM",
    email="privacy@ktm.com",
    country="Austrian",
    website="https://www.ktm.com/en-pt.html",
    cellPhone="987654321",
    group=Group.objects.get(name__icontains='Pierer'),
    description="",
    logo="static/imgs/logo-ktm.png",
    ).save()

    Brand(
    name="Husqvarna Motorcycles",
    email="privacy@piererindustrie.com",
    country="Austria",
    website="https://www.husqvarna-motorcycles.com/en-pt.html",
    cellPhone=" +7811215115202",
    group=Group.objects.get(name__icontains='Pierer'),
    description="",
    logo="static/imgs/Husqvarna_Logo.png",
    ).save()

    Brand(
    name="Royal Enfield",
    email="support@royalenfield.com",
    country="England",
    website="https://www.royalenfield.com/pt/pt/home/",
    cellPhone="123456789",
    group=Group.objects.get(name__icontains='Eicher'),
    description="enfield-logo.png",
    logo="static/imgs/enfield-logo.png",
    ).save()

    Brand(
    name="Bimota",
    email="info@bimotaportugal.pt",
    country="Italian",
    website="https://bimotaportugal.pt/",
    cellPhone="+351256000200",
    group=Group.objects.get(name__icontains='Bimota'),
    description="",
    logo="static/imgs/Bimota-Logo.png",
    ).save()

    Brand(
    name=" Norton Motorcycles",
    email="customer.data@nortonmotorcycles.com",
    country="England",
    website="https://nortonmotorcycles.com/",
    cellPhone="+441214203000",
    group=Group.objects.get(name__icontains='TVS'),
    description="",
    logo="static/imgs/Norton-Logo.png",
    ).save()

    Brand(
    name="Vespa",
    email="geral@vespa.pt",
    country="Italy",
    website="https://www.vespa.com/pt_PT/",
    cellPhone="+390587272111",
    group=Group.objects.get(name__icontains='Piaggio'),
    description="",
    logo="static/imgs/Vespa_logo.png",
    ).save()
def creategroups():
    Group(
    name="Piaggio Group",
    email="geral@cmachado.pt",
    country="Italy",
    website="https://www.piaggio.com/pt_PT/"
    ).save()   
    Group(
    name="Polaris Group",
    email="privacy@polaris.com",
    country="United States",
    website="https://www.polarisportugal.com/"
    ).save()
    Group(
    name="Pierer Group",
    email="privacy@piererindustrie.com",
    country="Austria",
    website="https://www.pierermobility.com/en"
    ).save()
    Group(
    name="Eicher Group",
    email="info@eichermotors.com",
    country="India",
    website="https://eicher.in/"
)
    Group(name="Harley-Davidson", email="privacy@harley-davidson.com", country="United States", website="https://www.harley-davidson.com/").save()
    Group(name="Triumph", email="info@triumphmotorcycles.com", country="United Kingdom", website="https://www.triumphmotorcycles.com/").save()
    Group(name="Bimota", email="info@bimotaportugal.pt", country="Italian", website="https://bimotaportugal.pt/").save()
    Group(name="MV Agusta", email="info@mvagusta.com", country="Italy", website="https://www.mvagusta.com/").save()
    Group(name="Royal Enfield Group", email="support@royalenfield.com", country="India", website="https://www.royalenfield.com/").save()
    Group(name="TVS Motor Company", email="info@tvsmotor.com", country="Chennai", website="https://www.tvsmotor.com/").save()
    Group(name="Norton Motorcycles Group", email="customer.data@nortonmotorcycles.com", country="United Kingdom", website="https://nortonmotorcycles.com/").save()
