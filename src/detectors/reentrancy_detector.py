from src.reentrancy import (
    generate_reentrancy_finding
)

from .base_detector import BaseDetector


class ReentrancyDetector(BaseDetector):

    def analyze(self, code):

        return generate_reentrancy_finding(code)