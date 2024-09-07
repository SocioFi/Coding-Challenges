# Quality Control Agent for Garment Production

## Project Overview

This project implements a simple agentic workflow system for quality control in a garment production line. The system classifies the quality of a batch based on garment measurements and defect rates, and decides whether to approve the batch, reject it, or escalate it to a human supervisor.

## Approach and Methodology

The `QualityControlAgent` class is designed to:
1. Take input data about garment measurements and defect rates.
2. Use a rule-based system to classify the quality of a batch.
3. Decide whether to approve the batch, reject it, or escalate it to a human supervisor.
4. Log decisions and the reasons for them.

### Key Components
- **Measurement Check**: Validates garment measurements against defined acceptable ranges.
- **Defect Rate Check**: Assesses the defect rate to determine the batch quality.
- **Decision Logging**: Logs decisions with reasons to a file for audit and review.

## Technologies, Libraries, and Frameworks Used

- **Python**: Programming language used to implement the quality control agent.
- **Logging**: Standard Python library for logging decisions and reasons to a file.

## Instructions for Setting Up the Environment and Running the Code

1. **Clone the Repository**: Clone the project repository to your local machine.
    ```bash
    git clone <https://github.com/sojib96/Coding-Challenges.git>
    cd <aI-mL-engineer>
    cd <challenge-3>
    ```

2. **Install Dependencies**: Ensure you have Python installed. No additional libraries are required for this project beyond the Python standard library.

3. **Run the Code**: Execute the provided script to test the quality control agent.
    ```bash
    python quality_control_agent.py
    ```

## Results

The script processes the input batch data, making decisions based on measurements and defect rates. The output includes:
- A decision to approve, reject, or escalate the batch.
- A log file (`quality_control.log`) detailing decisions and reasons.

### Expected Result
```plaintext
Decision: escalate
Log: [{'decision': 'escalate', 'batch_data': {'measurements': {'length': 25.2, 'width': 15.8, 'sleeve_length': 22.1}, 'defect_rate': 0.02, 'batch_size': 1000}, 'reason': 'High defect rate with large batch size'}]
