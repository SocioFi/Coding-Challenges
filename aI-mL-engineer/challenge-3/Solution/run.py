import logging
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QualityControlAgentML:
    def __init__(self, model=None):
        """
        Initialize the QualityControlAgent with a pre-trained model.
        :param model: Pre-trained scikit-learn model (e.g., DecisionTreeClassifier).
        """
        if model is None:
            self.model = self.train_model()
        else:
            self.model = model
    
    def train_model(self):
        """
        Train a decision tree model on synthetic data for demonstration.
        In a real-world scenario, you would replace this with real historical batch data.
        :return: Trained DecisionTreeClassifier model.
        """
        # Synthetic data: [length, width, sleeve_length, defect_rate]
        X = np.array([
            [25.1, 16.0, 22.0, 0.01],
            [24.5, 16.2, 21.9, 0.02],
            [25.3, 15.8, 22.1, 0.03],
            [26.0, 16.5, 22.5, 0.06],
            [24.8, 15.9, 21.8, 0.04]
        ])
        # Labels: 0 = approve, 1 = reject, 2 = escalate
        y = np.array([0, 0, 1, 2, 1])
        
        # Train a decision tree classifier
        clf = DecisionTreeClassifier()
        clf.fit(X, y)
        
        return clf
    
    def make_decision(self, batch_data):
        """
        Make a decision on whether to approve, reject, or escalate the batch using ML.
        
        :param batch_data: Dictionary containing 'measurements', 'defect_rate', and 'batch_size'.
        :return: A decision string ('approve', 'reject', or 'escalate') and an explanation.
        """
        features = np.array([
            batch_data['measurements']['length'],
            batch_data['measurements']['width'],
            batch_data['measurements']['sleeve_length'],
            batch_data['defect_rate']
        ]).reshape(1, -1)
        
        # Predict decision
        decision_code = self.model.predict(features)[0]
        decision_map = {0: 'approve', 1: 'reject', 2: 'escalate'}
        decision = decision_map[decision_code]
        
        # Explanation can be extended based on model output or rules
        explanation = f"Decision based on machine learning model: {decision}."
        
        # Log the decision
        logging.info(f"Decision: {decision}, Reason: {explanation}")
        
        return decision, explanation

# Example usage
batch_data = {
    'measurements': {
        'length': 25.2,
        'width': 15.8,
        'sleeve_length': 22.1
    },
    'defect_rate': 0.02,
    'batch_size': 1000
}

agent_ml = QualityControlAgentML()
decision, explanation = agent_ml.make_decision(batch_data)
print(f"Decision: {decision}, Explanation: {explanation}")
