import torch
import torch.nn as nn

class TransactionRiskModel(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.hidden_layer = nn.Linear(3,4)
        self.relu = nn.ReLU()
        self.output_layer = nn.Linear(4,2)
        
    def forward(self, x):
        x = self.hidden_layer(x)
        x = self.relu(x)
        x = self.output_layer(x)
        return x

model = TransactionRiskModel()

sample_transaction = torch.tensor(
    [500.0, 120.0, 0.0],
    dtype=torch.float32
)

prediction_scores = model(sample_transaction)
print("Prediction scores:")
print(prediction_scores)
print()

print("Output shape:")
print(prediction_scores.shape)
print()

print("Low-risk class score:", prediction_scores[0].item())
print("High-risk class score:", prediction_scores[1].item())
print()

print("\nHidden layer weights:")
print(model.hidden_layer.weight)

print("\nHidden layer biases:")
print(model.hidden_layer.bias)
print()

print("\nHidden layer parameter counts:")
print("Weight count:", model.hidden_layer.weight.numel())
print("Bias count:", model.hidden_layer.bias.numel())

print("\nAll model parameters:")
total_parameters = 0

for parameter in model.parameters():
    parameter_count = parameter.numel()
    total_parameters += parameter_count
    
print("Total trainable parameters:", total_parameters)

print()
loss_function = nn.CrossEntropyLoss()
print("\nLoss function:")
print(loss_function)

print()
target_label = torch.tensor([0])

print("\nTarget label:")
print(target_label)

print()

loss = loss_function(prediction_scores.unsqueeze(0), target_label)
loss.backward()
print("\nCalculated loss:")
print(loss.item())


print("\nOutput layer weight gradients:")
print(model.output_layer.weight.grad)

print("\nOutput layer bias gradients:")
print(model.output_layer.bias.grad)

print("\nHidden layer weight gradients:")
print(model.hidden_layer.weight.grad)

print("\nHidden layer bias gradients:")
print(model.hidden_layer.bias.grad)