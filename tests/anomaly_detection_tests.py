import unittest
from detection import AnomalyDetector

class TestAnomalyDetection(unittest.TestCase):
    def test_basic_detection(self):
        detector = AnomalyDetector(window_size=5)
        data = [10, 12, 13, 15, 50]  # Anomaly at the last point
        results = [detector.detect(x) for x in data]
        self.assertTrue(results[-1], "Anomaly should have been detected")

if __name__ == "__main__":
    unittest.main()
