# Car Management System

This Django project is a comprehensive car management system that allows users to manage car information, including details, features, and images. The system is designed to handle different aspects of car management, such as the car model, make, features, and associated images.

## Features

- **Car Information**: Store and manage basic car information like model and make.
- **Detailed Car Specifications**: Manage various details about the car, including type, exterior, interior, engine type, transmission, and more.
- **Car Features**: Specify features like AWD/4WD, navigation system, sunroof, heated seats, and much more.
- **Car Images**: Upload and manage multiple images associated with a car.

## Models

### Car

The `Car` model contains basic information about the car:

- `model`: The car's model (e.g., Corolla, Mustang). This field is automatically saved in uppercase.
- `make`: The manufacturer of the car (e.g., Toyota, Ford).

### Detail

The `Detail` model stores detailed specifications of a car:

- `car`: ForeignKey linking to the `Car` model.
- `car_type`: The type of the car (e.g., SUV, Sedan).
- `exterior_type`: The type of exterior finish.
- `vin`: Vehicle Identification Number.
- `miles`: The number of miles driven.
- `interior_type`: The type of interior finish.
- `stock`: The stock number.
- `drive_type`: The drive type (e.g., AWD, FWD).
- `engine_type`: The engine type (e.g., V6, Electric).
- `transmission_type`: The transmission type (e.g., Automatic, Manual).
- `color`: The color of the car.
- `mpg`: Miles per gallon.
- `price`: The price of the car.
- `description`: A detailed description of the car.
- `year`: The manufacturing year.

### Features

The `Features` model stores various features available in a car:

- `car`: ForeignKey linking to the `Car` model.
- Boolean fields for each feature, such as `awd_4wd`, `navigation_system`, `leather_seats`, `sunroof_moonroof`, etc.

### Image

The `Image` model manages images associated with a car:

- `detail`: ForeignKey linking to the `Detail` model.
- `image`: ImageField for uploading images, stored in the `cars/` directory.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/diyorbekqodirboyev863/auto-hub.git
   cd auto-hub
   ```

2. **Install Dependencies**:
   Ensure you have Python and Django installed. You can use `pipenv` to manage your virtual environment.
   ```bash
   pipenv install
   ```

3. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser** (Optional):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate to the admin panel to add or manage cars, details, features, and images.
- Customize and extend the project as needed for your specific requirements.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
