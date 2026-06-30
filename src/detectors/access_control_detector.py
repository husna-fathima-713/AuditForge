from src.access_control import (
    generate_access_control_finding
)

from .base_detector import BaseDetector


class AccessControlDetector(BaseDetector):

    def analyze(self, code):

        return generate_access_control_finding(code)