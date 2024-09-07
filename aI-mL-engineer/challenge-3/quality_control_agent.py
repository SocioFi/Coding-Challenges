import logging
from datetime import datetime

logging.basicConfig(
    filename='quality_control.log',  
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class QualityControlAgent:
    def __init__(self, max_defect_rate=0.01, min_length=25.0, max_length=26.0,
                 min_width=15.5, max_width=16.5, min_sleeve_length=21.5, max_sleeve_length=23.0):
        self.max_defect_rate = max_defect_rate
        self.min_length = min_length
        self.max_length = max_length
        self.min_width = min_width
        self.max_width = max_width
        self.min_sleeve_length = min_sleeve_length
        self.max_sleeve_length = max_sleeve_length
        self.log = []

    def _isWithinRange(self, value, min_value, max_value):
        return min_value <= value <= max_value

    def _escalateOrReject(self, attribute_name, value, escalate_margin):
        min_value = getattr(self, f'min_{attribute_name}')
        max_value = getattr(self, f'max_{attribute_name}')

        if self._isWithinRange(value, min_value - escalate_margin, max_value + escalate_margin):
            return 'escalate', f'{attribute_name.capitalize()} need human supervision'
        return 'reject', f'{attribute_name.capitalize()} out of acceptable range'
    
    def checkMeasurements(self, measurements):
        escalate_length_margin = 0.5
        escalate_width_margin = 0.3
        escalate_sleeve_length_margin = 0.5

        if not self._isWithinRange(measurements['length'], self.min_length, self.max_length):
            return self._escalateOrReject('length', measurements['length'], escalate_length_margin)

        if not self._isWithinRange(measurements['width'], self.min_width, self.max_width):
            return self._escalateOrReject('width', measurements['width'], escalate_width_margin)

        if not self._isWithinRange(measurements['sleeve_length'], self.min_sleeve_length, self.max_sleeve_length):
            return self._escalateOrReject('sleeve_length', measurements['sleeve_length'], escalate_sleeve_length_margin)

        return 'approve', 'Measurements are within acceptable range'

    def checkDefectRate(self, defect_rate, batch_size):
        if defect_rate > self.max_defect_rate:
            reason = 'High defect rate with large batch size' if batch_size > 500 else 'High defect rate'
            return False, reason
        return True, 'Defect rate is within acceptable range'
    
    def _logDecision(self, decision, batch_data, reason):
        log_entry = {
            'decision': decision,
            'batch_data': batch_data,
            'reason': reason
        }
        self.log.append(log_entry)
        logging.info(f"Decision: {decision}, Batch Data: {batch_data}, Reason: {reason}")

    def processBatch(self, batch_data):
        measurements = batch_data['measurements']
        defect_rate = batch_data['defect_rate']
        batch_size = batch_data['batch_size']

        measurement_decision, measurement_reason = self.checkMeasurements(measurements)
        if measurement_decision != 'approve':
            self._logDecision(measurement_decision, batch_data, measurement_reason)
            return measurement_decision

        defect_rate_decision, defect_rate_reason = self.checkDefectRate(defect_rate, batch_size)
        if not defect_rate_decision:
            decision = 'escalate' if defect_rate_reason == 'High defect rate with large batch size' else 'reject'
            self._logDecision(decision, batch_data, defect_rate_reason)
            return decision

        self._logDecision('approve', batch_data, 'All parameters within acceptable range')
        return 'approve'

    def getLog(self):
        return self.log


#example data point
batch_data = {
    'measurements': {
        'length': 25.2,
        'width': 15.8,
        'sleeve_length': 22.1
    },
    'defect_rate': 0.02,
    'batch_size': 1000
}

qc_agent = QualityControlAgent()
decision = qc_agent.processBatch(batch_data)
print(f"Decision: {decision}")
print("Log:", qc_agent.getLog())
