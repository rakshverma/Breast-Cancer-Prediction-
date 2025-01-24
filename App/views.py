from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import numpy as np
import json

with open('myapp/model_params.json', 'r') as f:
    weights_biases = json.load(f)
with open('myapp/scaler_params.json', 'r') as f:
    scaler_params = json.load(f)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

class SimpleNeuralNetwork:
    def __init__(self, weights_biases):
        self.weights_biases = weights_biases
    
    def predict(self, X):
        current_input = X
        for layer in self.weights_biases:
            weights = np.array(layer['weights'])
            biases = np.array(layer['biases'])
            z = np.dot(current_input, weights) + biases
            current_input = sigmoid(z) if layer == self.weights_biases[-1] else relu(z)
        return current_input

class SimpleScaler:
    def __init__(self, mean, scale):
        self.mean = np.array(mean)
        self.scale = np.array(scale)
    
    def transform(self, X):
        return (X - self.mean) / self.scale

# Initialize model and scaler
model = SimpleNeuralNetwork(weights_biases)
scaler = SimpleScaler(scaler_params['mean'], scaler_params['scale'])

@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html')

@csrf_protect
def predict(request):
    if request.method == 'POST':
        features = [
            float(request.POST.get('radius_mean')),
            float(request.POST.get('texture_mean')),
            float(request.POST.get('perimeter_mean')),
            float(request.POST.get('area_mean')),
            float(request.POST.get('smoothness_mean')),
            float(request.POST.get('compactness_mean')),
            float(request.POST.get('concavity_mean')),
            float(request.POST.get('concave_points_mean')),
            float(request.POST.get('symmetry_mean')),
            float(request.POST.get('fractal_dimension_mean')),
            float(request.POST.get('radius_se')),
            float(request.POST.get('texture_se')),
            float(request.POST.get('perimeter_se')),
            float(request.POST.get('area_se')),
            float(request.POST.get('smoothness_se')),
            float(request.POST.get('compactness_se')),
            float(request.POST.get('concavity_se')),
            float(request.POST.get('concave_points_se')),
            float(request.POST.get('symmetry_se')),
            float(request.POST.get('fractal_dimension_se')),
            float(request.POST.get('radius_worst')),
            float(request.POST.get('texture_worst')),
            float(request.POST.get('perimeter_worst')),
            float(request.POST.get('area_worst')),
            float(request.POST.get('smoothness_worst')),
            float(request.POST.get('compactness_worst')),
            float(request.POST.get('concavity_worst')),
            float(request.POST.get('concave_points_worst')),
            float(request.POST.get('symmetry_worst')),
            float(request.POST.get('fractal_dimension_worst'))
        ]
        
        features_array = np.array(features).reshape(1, -1)
        scaled_features = scaler.transform(features_array)
        prediction = model.predict(scaled_features)
        result = "Malignant" if prediction[0] > 0.5 else "Benign"
        
        return render(request, 'myapp/dashboard.html', {'prediction': result})
    
    return render(request, 'myapp/dashboard.html')

def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if User.objects.filter(username=email).exists():
            return render(request, 'myapp/index.html', {'error': 'User already exists!'})
        
        if password == confirm_password:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            login(request, user)
            return redirect('dashboard')
    return redirect('index')

def index(request):
    return render(request, 'myapp/index.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return redirect('index')
