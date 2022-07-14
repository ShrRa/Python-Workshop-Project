"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Charlie'
    d = Doctor(name=name)

    assert d.name == name

def test_add_observation():
    from inflammation.models import Patient, Observation

    name = 'Charlie'
    p = Patient(name=name)
    obs=p.add_observation(6)
    assert isinstance(obs,Observation)

def test_add_observation_val():
    from inflammation.models import Patient

    name = 'Charlie'
    p = Patient(name=name)
    obs=p.add_observation(6)
    assert obs.value == 6

def test_get_patients_names():
    from inflammation.models import Doctor,Patient,Observation

    name = 'Charlie'
    d = Doctor(name=name)

    name = 'Alice'
    p = Patient(name=name)
    p.add_observation(5)
    d.add_patient(p)
    name = 'Bob'
    p = Patient(name=name)
    p.add_observation(12)
    d.add_patient(p)

    assert d.get_patients_names() == ['Alice', 'Bob']
