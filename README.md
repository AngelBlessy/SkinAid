# SkinAid+ : Skin Cancer Detection System

[![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-MobileNet-orange.svg)](https://pytorch.org/)

> **Empowering early diagnosis with cutting-edge technology**

SkinAid+ is an AI-powered skin cancer detection and consultation system designed to help individuals and healthcare providers identify potential skin abnormalities early. Using advanced deep learning techniques and integrated telemedicine features, the system bridges the gap between diagnosis and medical consultation.

## 🌟 Features

### 🔬 **AI-Powered Detection**
- **MobileNet-based Classification**: Efficient skin lesion analysis optimized for mobile devices
- **Binary Classification**: Distinguishes between benign and malignant lesions
- **Subtype Identification**: Classifies specific cancer types (Melanoma, Basal Cell Carcinoma, etc.)
- **High Accuracy**: Trained on extensive dermatological datasets for reliable results

### 📱 **Seamless User Experience**
- **Image Upload**: Easy skin lesion image submission
- **Real-time Analysis**: Fast processing with instant results
- **Mobile Optimized**: Responsive design for all devices
- **Multilingual Support**: Google Translate API integration for global accessibility

### 🏥 **Integrated Healthcare**
- **Doctor Consultation**: Direct appointment booking with dermatologists
- **Specialist Profiles**: Detailed information about available doctors
- **Appointment Management**: Schedule, view, and track consultations
- **Medical History**: Secure patient record management

### 💳 **Secure Payments**
- **Razorpay Integration**: Safe and secure payment processing
- **Multiple Payment Options**: Credit/debit cards, UPI, and more
- **Transaction History**: Complete payment tracking
- **Refund Support**: Easy cancellation and refund processing

## 🚀 Quick Start

### Prerequisites

```bash
# System Requirements
- Python 3.8+
- Node.js 14+
- MySQL 8.0+
- Minimum 2GB RAM
- 30GB+ storage space
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/skinaid-plus.git
cd skinaid-plus
```

2. **Set up Python environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure database**
```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE skinaid_db;
```

4. **Environment variables**
```bash
# Create .env file
cp .env.example .env
# Add your API keys and database credentials
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Start the development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   ML Model      │
│  (HTML/CSS/JS)  │◄──►│    (Django)     │◄──►│  (MobileNet)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Google Trans   │    │     MySQL       │    │   Payment API   │
│      API        │    │   Database      │    │   (Razorpay)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📊 Technology Stack

### **Backend**
- **Framework**: Django 4.2+
- **Database**: MySQL 8.0
- **ORM**: Django ORM
- **API**: Django REST Framework

### **Frontend**
- **Languages**: HTML5, CSS3, JavaScript ES6+
- **Styling**: Responsive CSS with media queries
- **UI/UX**: Modern, accessible design

### **Machine Learning**
- **Framework**: PyTorch
- **Model**: MobileNet V2 (Transfer Learning)
- **Image Processing**: OpenCV, PIL
- **Data Augmentation**: Albumentations

### **Integrations**
- **Payment**: Razorpay API
- **Translation**: Google Translate API
- **Authentication**: Django Auth System

## 📱 Screenshots

### Landing Page
![Landing Page](docs/screenshots/landing_page.png)

### Detection Interface
![Detection Screen](docs/screenshots/detection_screen.png)

### Doctor Consultation
![Doctor Profiles](docs/screenshots/doctor_profiles.png)

### Appointment Booking
![Appointment Booking](docs/screenshots/appointment_booking.png)

## 🧪 Testing

### Running Tests
```bash
# Unit tests
python manage.py test

# ML model testing
python test_model.py
```

## 📈 Performance

- **Model Accuracy**: 92%+ on validation dataset
- **Response Time**: <5 seconds for image analysis
- **Mobile Optimization**: Works efficiently on low-end devices
- **Scalability**: Designed for high concurrent users

## 🔒 Security Features

- **Data Encryption**: All sensitive data encrypted at rest and in transit
- **Authentication**: Secure user authentication and authorization
- **Payment Security**: PCI DSS compliant payment processing
- **Privacy**: HIPAA-compliant medical data handling
- **Input Validation**: Comprehensive form and file validation

## 📁 Project Structure

```
skinaid-plus/
├── backend/
│   ├── skinaid/
│   │   ├── models/          # Database models
│   │   ├── views/           # API views
│   │   ├── serializers/     # DRF serializers
│   │   └── utils/           # Utility functions
│   ├── ml_model/
│   │   ├── mobilenet_model.py
│   │   ├── preprocessing.py
│   │   └── inference.py
│   └── manage.py
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
├── tests/
├── docs/
├── requirements.txt
└── README.md
```

## 🎯 Future Roadmap

### Phase 1 (Current)
- [x] Basic skin cancer detection
- [x] Appointment booking system
- [x] Payment integration
- [x] Multilingual support

### Phase 2 (Planned)
- [ ] Real-time video consultations
- [ ] Wearable device integration
- [ ] Advanced AI models (Vision Transformers)
- [ ] Blockchain-based medical records

### Phase 3 (Future)
- [ ] IoT integration for continuous monitoring
- [ ] AR/VR consultation experiences
- [ ] Global healthcare network expansion

<!-- ## 👥 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details. -->

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

<!-- ## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->

## 📞 Support

- **Email**: ablessy84@gmail.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/skinaid-plus/issues)

## 🙏 Acknowledgments

- **CHRIST (Deemed to be University)** - Academic support and guidance
- **Dr. Sivabalan R** - Project supervision and mentorship
- **HAM10000 Dataset** - Training data for machine learning model
- **ISIC Archive** - Additional dermatological image datasets

<!-- ## 📊 Statistics

- **Lines of Code**: 15,000+
- **Test Coverage**: 85%+
- **Supported Languages**: 50+
- **Model Training Data**: 10,000+ images
- **Performance**: <5s response time -->

---

### 🔬 Research Paper
This project is part of academic research conducted at CHRIST (Deemed to be University), Department of Computer Science, under the guidance of Dr. Sivabalan R.

**Citation:**
```
Blessy, A., Bino, A., & K, B. (2025). SkinAid+: Skin Cancer Detection System. 
Final Year Project Report, CHRIST (Deemed to be University), Bangalore.
```

---

**Made with ❤️ by Angel Blessy, Anna Bino, and Bhavani K**
