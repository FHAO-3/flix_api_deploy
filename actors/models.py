from django.db import models

NATIONALITIES_CHOICES = (
    ('BRAZIL', 'Basil'),
    ('USA', 'Estados Unidos'),
    ('UK', 'Reino Unido'),
    ('FR', 'França'),
    ('ES', 'Espanha'),
    ('IT', 'Italia'),
    ('JP', 'Japão'),
    ('CN', 'China'),
    ('KR', 'Corea do Sul'),
    ('IN', 'India'),
    ('DE', 'Alemanha'),
    ('RU', 'Rússia'),
    ('AU', 'Austrália'),
    ('CA', 'Canadá'),
    ('MX', 'México'),
    ('ZA', 'África do Sul'),
    ('AR', 'Argentina'),
    ('EG', 'Egito'),
    ('NG', 'Nigéria'),
    ('SE', 'Suécia'),
    ('NL', 'Países Baixos'),
    ('NO', 'Noruega'),
    ('FI', 'Finlândia'),
    ('DK', 'Dinamarca'),
    ('PL', 'Polônia'),
    ('CH', 'Suíça'),
    ('AT', 'Áustria'),
    ('BE', 'Bélgica'),
    ('PT', 'Portugal'),
    ('GR', 'Grécia'),
    ('HU', 'Hungria'),
    ('CZ', 'República Tcheca'),
    ('IE', 'Irlanda'),
    ('SK', 'Eslováquia'),
    ('SI', 'Eslovênia'),
    ('HR', 'Croácia'),
    ('BG', 'Bulgária'),
    ('RO', 'Romênia'),
    ('LV', 'Letônia'),
    ('LT', 'Lituânia'),
    ('CL', 'Chile'),
    ('CO', 'Colômbia'),
    ('PE', 'Peru'),
    ('VE', 'Venezuela'),
    ('EC', 'Equador'),
    ('BO', 'Bolívia'),
    ('PY', 'Paraguai'),
    ('UY', 'Uruguai'),
    ('SV', 'El Salvador'),
    ('GT', 'Guatemala'),
    ('HN', 'Honduras'),
    ('NI', 'Nicarágua'),
    ('CR', 'Costa Rica'),
    ('PA', 'Panamá'),
    ('CU', 'Cuba'),
    ('DO', 'República Dominicana'),
    ('PR', 'Porto Rico'),
    ('EE', 'Estônia'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    # obrigatorio
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITIES_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
