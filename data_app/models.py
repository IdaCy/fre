from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SALUTATION_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr'),
        ('Professor', 'Professor'),
        ('Ms', 'Ms'),
        ('Other', 'Other'),
    ]
    salutation = models.CharField(max_length=20, choices=SALUTATION_CHOICES, blank=True, null=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
        return full_name if full_name else self.username

"""
class DoseType(models.Model):
    dosetype = models.CharField(max_length=100)


class DoseUnit(models.Model):
    dose_units = models.CharField(max_length=50)
    rate = models.FloatField()


class DurationUnits(models.Model):
    duration_units = models.CharField(max_length=50)


class EcosystemTypes(models.Model):
    ecosystems = models.CharField(max_length=100)


class ActivityConcUnit(models.Model):
    activity_units = models.CharField(max_length=50)


class Answers(models.Model):
    simple_answers = models.CharField(max_length=50)


class DoseMethod(models.Model):
    method = models.CharField(max_length=100)


class DoseRateUnit(models.Model):
    dose_units = models.CharField(max_length=50)
    rate = models.FloatField()


class EndpointsUmbrella(models.Model):
    umbrella = models.CharField(max_length=100)


class ExposureSource(models.Model):
    expsource = models.CharField(max_length=100)


class ExposureType(models.Model):
    exp_type = models.CharField(max_length=100)


class ICRP(models.Model):
    icrp_type = models.CharField(max_length=100)


class Language(models.Model):
    language1 = models.CharField(max_length=100)


class MainData(models.Model):
    # reference_id = models.IntegerField()
    radiation_type = models.CharField(max_length=100)
    study_type = models.CharField(max_length=100)
    wildlife_group = models.CharField(max_length=100)
    ecosystems = models.CharField(max_length=100)
    dosetype = models.CharField(max_length=100)
    species_l = models.CharField(max_length=100)
    species_c = models.CharField(max_length=100)
    umbrella_end = models.CharField(max_length=100)
    notes = models.TextField()
    nuclide = models.CharField(max_length=100)
    rbe = models.FloatField()
    rbe_notes = models.TextField()
    date = models.DateField()
    dose_method = models.CharField(max_length=100)
    effect_description = models.TextField()
    null_data = models.BooleanField()
    expsource = models.CharField(max_length=100)
    rep = models.BooleanField()
    mort = models.BooleanField()
    mut = models.BooleanField()
    morb = models.BooleanField()
    adap = models.BooleanField()
    stim = models.BooleanField()
    ecol = models.BooleanField()
    lifestage = models.CharField(max_length=100)
    icrp = models.CharField(max_length=100)
    activity1 = models.FloatField()
    unitsa1 = models.CharField(max_length=50)
    activity2 = models.FloatField()
    unitsa2 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50)
    activity3 = models.FloatField()
    unitsa3 = models.CharField(max_length=50)
    type3 = models.CharField(max_length=50)
    weight1 = models.FloatField()
    weight2 = models.FloatField()
    approval_choices = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    approval_data_status = models.CharField(max_length=20, choices=approval_choices, default='PENDING')

    def __str__(self):
        return f"Main Data {self.id_link}"


class ModificationStatus(models.Model):
    date = models.DateField()
    who = models.CharField(max_length=100)
    notes = models.TextField()


class Organisations(models.Model):
    organisation = models.CharField(max_length=200)


class Effects(models.Model):
    dose = models.FloatField()
    dosed1 = models.CharField(max_length=100)
    dose_rate = models.FloatField()
    unitsd2 = models.CharField(max_length=50)
    duration = models.FloatField()
    duration_units = models.CharField(max_length=50)
    biota_a_conc = models.FloatField()
    ac_units1 = models.CharField(max_length=50)
    ac_value1 = models.FloatField()
    ac_units2 = models.CharField(max_length=50)
    environ_type = models.CharField(max_length=100)
    dose_effect_value = models.FloatField()
    uncertainty = models.FloatField()
    degree3 = models.CharField(max_length=100)
    loedr = models.BooleanField()
    hnedr = models.BooleanField()
    background_dose = models.BooleanField()
    standardised_dose_unit = models.FloatField()
    standardised_dose_rate_unit = models.FloatField()

    def __str__(self):
        return f"Effect {self.id}"


class PubType(models.Model):
    article_type = models.CharField(max_length=100)


class Radionuclide(models.Model):
    nuclide = models.CharField(max_length=100)


class Reference(models.Model):
    author = models.TextField()
    title = models.TextField()
    year = models.CharField(max_length=20)
    journal = models.CharField(max_length=100)
    article_type = models.CharField(max_length=100)
    volume = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50)
    page_numbers = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    translation = models.TextField()
    keyword1 = models.CharField(max_length=100)
    keyword2 = models.CharField(max_length=100)
    keyword3 = models.CharField(max_length=100)
    keyword4 = models.CharField(max_length=100)
    keyword5 = models.CharField(max_length=100)
    keyword6 = models.CharField(max_length=100)
    institute_location = models.CharField(max_length=100)
    contract_name = models.CharField(max_length=100)
    ref_no = models.CharField(max_length=100)
    data_entry = models.CharField(max_length=100)
    date = models.DateField()
    score = models.IntegerField()
    approval_choices = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    approval_data_status = models.CharField(max_length=20, choices=approval_choices, default='PENDING')


class StudyType(models.Model):
    study_type = models.CharField(max_length=100)


class SwitchboardItem(models.Model):
    item_number = models.IntegerField()
    item_text = models.CharField(max_length=100)
    command = models.CharField(max_length=100)
    argument = models.CharField(max_length=100)
    user_types = models.CharField(max_length=100)


class Weight(models.Model):
    weight = models.CharField(max_length=100)


class WildlifeGroup(models.Model):
    wildlife = models.CharField(max_length=100)

"""