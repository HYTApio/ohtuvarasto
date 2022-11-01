import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_korjaa_uuden_varaston_tilavuuden(self):
        self.assertAlmostEqual(Varasto(-10).tilavuus, 0.0)

    def test_korjaa_uuden_varaston_saldon(self):
        self.assertAlmostEqual(Varasto(10, -10).saldo, 0.0)
    
    def test_ylimääräinen_saldo_pois(self):
        self.assertAlmostEqual(Varasto(10, 20).saldo, 10)

    def test_lisays_ei_vahenna_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-1)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_ei_lisaa_enemman_tilavuus(self):
        self.varasto.lisaa_varastoon(12)
        # hukkaan menee 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ota_ei_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-2)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ota_ei_ota_enemman_kuin_voi(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(10)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 9)
    
    def test_print(self):
        self.assertEqual(print(self.varasto), None)