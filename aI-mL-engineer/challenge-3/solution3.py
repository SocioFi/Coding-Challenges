class QualityControlAgent:
    def __init__(self, measurement_thresholds, defect_rate_threshold):
        """
        Initializes the quality control agent with given thresholds.

        Parameters:
        - measurement_thresholds: Dict specifying the acceptable measurement range for each dimension
        - defect_rate_threshold: Maximum acceptable defect rate
        """
        self.measurement_thresholds = measurement_thresholds
        self.defect_rate_threshold = defect_rate_threshold
        self.log = []

    def evaluate_batch(self, batch_data):
        """
        Evaluates the quality of a garment batch based on input data.

        Parameters:
        - batch_data: Dict containing batch measurements, defect rate, and batch size

        Returns:
        - Decision: 'Approve', 'Reject', or 'Escalate'
        """
        measurements = batch_data['measurements']
        defect_rate = batch_data['defect_rate']
        decision = None

        # Check measurement thresholds
        for measurement, value in measurements.items():
            if measurement not in self.measurement_thresholds:
                continue  # Skip if no threshold is defined for this measurement

            min_val, max_val = self.measurement_thresholds[measurement]
            if not (min_val <= value <= max_val):
                decision = 'Reject'
                self._log_decision(decision, f"{measurement} out of range: {value} not in ({min_val}, {max_val})")
                return decision

        # Check defect rate
        if defect_rate > self.defect_rate_threshold:
            decision = 'Escalate'
            self._log_decision(decision, f"Defect rate too high: {defect_rate} > {self.defect_rate_threshold}")
            return decision

        # If all checks passed
        decision = 'Approve'
        self._log_decision(decision, "All measurements within acceptable range and defect rate acceptable.")
        return decision

    def _log_decision(self, decision, reason):
        """
        Logs the decision and its reason.

        Parameters:
        - decision: The decision made ('Approve', 'Reject', 'Escalate')
        - reason: Reason for the decision
        """
        self.log.append({
            'decision': decision,
            'reason': reason
        })

    def print_log(self):
        """Prints the decision log."""
        for entry in self.log:
            print(f"Decision: {entry['decision']} | Reason: {entry['reason']}")


# Define acceptable thresholds for measurements
measurement_thresholds = {
    'length': (24.0, 26.0),  # Min and Max acceptable length
    'width': (15.0, 16.0),   # Min and Max acceptable width
    'sleeve_length': (21.0, 23.0)  # Min and Max acceptable sleeve length
}

# Define maximum acceptable defect rate
defect_rate_threshold = 0.01  # 1%

# Create an instance of the QualityControlAgent
qc_agent = QualityControlAgent(measurement_thresholds, defect_rate_threshold)

# Sample input data for a batch
batch_data = {
    'measurements': {
        'length': 25.2,
        'width': 15.8,
        'sleeve_length': 22.1
    },
    'defect_rate': 0.02,
    'batch_size': 1000
}

# Evaluate the batch
decision = qc_agent.evaluate_batch(batch_data)
print(f"Batch Decision: {decision}")

# Print the log of decisions
qc_agent.print_log()
