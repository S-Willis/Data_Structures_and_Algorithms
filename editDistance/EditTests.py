import unittest, editDistance

class EditTests(unittest.TestCase):

    def setUp(self):
        self.sequenceS1 = 'ACCGGTATCCTAGGAC'
        self.sequenceT1 = 'ACCTATCTTAGGAC'
        self.results1   = editDistance.editDistance(self.sequenceS1, self.sequenceT1)

        self.sequenceS2 = 'kitten'
        self.sequenceT2 = 'sitting'
        self.results2   = editDistance.editDistance(self.sequenceS2, self.sequenceT2)

        self.sequenceS3 = 'kite'
        self.sequenceT3 = 'sit'
        self.results3   = editDistance.editDistance(self.sequenceS3, self.sequenceT3)

        self.sequenceS4 = 'ACGT'
        self.sequenceT4 = 'ACGT'
        self.results4   = editDistance.editDistance(self.sequenceS4, self.sequenceT4)




    def test_ansS(self):
        self.assertTrue(self.results1[0] == 'ACCGGTATCCTAGGAC')
        self.assertTrue(self.results2[0] == 'kitten-')
        self.assertTrue(self.results3[0] == 'kite')
        self.assertTrue(self.results4[0] == 'ACGT')

    def test_ansT(self):
        self.assertTrue(self.results1[1] == 'ACC--TATCTTAGGAC')
        self.assertTrue(self.results2[1] == 'sitting')
        self.assertTrue(self.results3[1] == 'sit-')
        self.assertTrue(self.results4[1] == 'ACGT')

    def test_score(self):
        self.assertTrue(self.results1[2] == 3)
        self.assertTrue(self.results2[2] == 3)
        self.assertTrue(self.results3[2] == 2)
        self.assertTrue(self.results4[2] == 0)



if __name__ == '__main__':
    unittest.main()
