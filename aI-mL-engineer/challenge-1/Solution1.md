# Quality Control Agent for Garment Production Line

## Brief Explanation of Approach
The `QualityControlAgent` class is designed to automate quality control decisions in a garment production line. It takes input data about garment measurements, defect rates, and batch size. The agent uses a rule-based system to decide whether to approve a batch, reject it, or escalate it to a human supervisor. It also logs its decisions along with the reasons.

## Assumptions
- All measurements are in the same unit (e.g., centimeters).
- Defect rate is provided as a fraction (e.g., 0.02 for 2%).
- Threshold values for measurements and defect rates are hardcoded but can be adjusted based on requirements.

## Instructions to Run
1. Install the necessary dependencies using `requirements.txt`.
2. Run the `solution1.py` file to instantiate the `QualityControlAgent` and provide input data.
3. Observe the output decisions and logs in the console.

## List of Dependencies and Versions
- Python 3.7+
- No external libraries are required.

## Requirements
### `requirements.txt`
