class BaseDetector:

    def analyze(self, code):

        raise NotImplementedError(
            "Detector must implement analyze()"
        )