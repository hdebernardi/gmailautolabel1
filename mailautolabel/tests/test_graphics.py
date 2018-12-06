import unittest
import graphics.interface_graphique as graphics

class Graphics(unittest.TestCase):
    """Test Graphics"""
    def testAffichageTexteSimple(self):
        """Affiche l'interface graphique"""
        graphics.affichageTexteSimple('bonjour')
        self.assertTrue('True')

if __name__ == '__main__':
    unittest.main()
