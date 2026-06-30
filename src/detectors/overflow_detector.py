from src.overflow import (
    generate_overflow_finding
)

from .base_detector import BaseDetector


class OverflowDetector(BaseDetector):

    def analyze(self, code):

        return generate_overflow_finding(code)