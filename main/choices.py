# choices.py

'''
Choices modules.
'''

import datetime

CAR_TYPES = [
    ('Sedan', 'Sedan'),
    ('Coupe', 'Coupe'),
    ('Sportscars', 'Sportscars'),
    ('Station wagon', 'Station wagon'),
    ('Hatchback', 'Hatchback'),
    ('Convertible', 'Convertible'),
    ('SUV', 'Sport-utility vehicle (SUV)'),
    ('Minivan', 'Minivan'),
    ('Pickup truck', 'Pickup truck'),
    ('Jeep', 'Jeep'),
    ('Electric car', 'Electric car'),
    ('CUV', 'CUV/Crossover'),
    ('Spyder', 'Spyder'),
    ('Hot hatch', 'Hot hatch'),
    ('Limousine', 'Limousine'),
    ('UTE', 'UTE'),
    ('Pony car', 'Pony car'),
    ('Sports sedan', 'Sports sedan'),
    ('Military vehicle', 'Military vehicle'),
    ('Dragster', 'Dragster'),
]

EXTERIOR_TYPES = [
    ('Metallic', 'Metallic'),
    ('Pearlescent', 'Pearlescent'),
    ('Matte', 'Matte'),
    ('Glossy', 'Glossy'),
    ('Solid', 'Solid'),
    ('Two-tone', 'Two-tone'),
    ('Chrome', 'Chrome'),
    ('Carbon Fiber', 'Carbon Fiber'),
    ('Vinyl Wrap', 'Vinyl Wrap'),
    ('Custom Paint', 'Custom Paint'),
    ('Convertible Top', 'Convertible Top'),
    ('Soft Top', 'Soft Top'),
    ('Hard Top', 'Hard Top'),
    ('Sunroof', 'Sunroof'),
    ('Panoramic Sunroof', 'Panoramic Sunroof'),
    ('Targa Top', 'Targa Top'),
    ('Widebody Kit', 'Widebody Kit'),
    ('Off-road Kit', 'Off-road Kit'),
    ('Racing Livery', 'Racing Livery'),
]

INTERIOR_TYPES = [
    ('Leather', 'Leather'),
    ('Cloth', 'Cloth'),
    ('Vinyl', 'Vinyl'),
    ('Suede', 'Suede'),
    ('Alcantara', 'Alcantara'),
    ('Wood Trim', 'Wood Trim'),
    ('Carbon Fiber Trim', 'Carbon Fiber Trim'),
    ('Metal Trim', 'Metal Trim'),
    ('Leatherette', 'Leatherette'),
    ('Velour', 'Velour'),
    ('Nappa Leather', 'Nappa Leather'),
    ('Synthetic Leather', 'Synthetic Leather'),
    ('Two-tone Interior', 'Two-tone Interior'),
    ('Quilted Leather', 'Quilted Leather'),
    ('Perforated Leather', 'Perforated Leather'),
    ('Sport Seats', 'Sport Seats'),
    ('Luxury Seats', 'Luxury Seats'),
    ('Bucket Seats', 'Bucket Seats'),
    ('Heated Seats', 'Heated Seats'),
    ('Cooled Seats', 'Cooled Seats'),
    ('Massaging Seats', 'Massaging Seats'),
    ('Ambient Lighting', 'Ambient Lighting'),
    ('Custom Interior', 'Custom Interior'),
]

DRIVE_TYPES = [
    ('FWD', 'Front-Wheel Drive (FWD)'),
    ('RWD', 'Rear-Wheel Drive (RWD)'),
    ('AWD', 'All-Wheel Drive (AWD)'),
    ('4WD', 'Four-Wheel Drive (4WD)'),
    ('Part-Time 4WD', 'Part-Time 4WD'),
    ('Full-Time 4WD', 'Full-Time 4WD'),
    ('4WS', 'Four-Wheel Steering (4WS)'),
    ('Electric', 'Electric Drive'),
    ('Hybrid', 'Hybrid Drive'),
    ('Plug-in Hybrid', 'Plug-in Hybrid Drive'),
]

ENGINE_TYPES = [
    ('Inline-4', 'Inline-4 (I4)'),
    ('V6', 'V6'),
    ('V8', 'V8'),
    ('V10', 'V10'),
    ('V12', 'V12'),
    ('Inline-3', 'Inline-3 (I3)'),
    ('Inline-5', 'Inline-5 (I5)'),
    ('Flat-4', 'Flat-4 (Boxer)'),
    ('Flat-6', 'Flat-6 (Boxer)'),
    ('W12', 'W12'),
    ('Electric', 'Electric'),
    ('Hybrid', 'Hybrid'),
    ('Turbocharged', 'Turbocharged'),
    ('Supercharged', 'Supercharged'),
    ('Diesel', 'Diesel'),
    ('Rotary', 'Rotary (Wankel)'),
    ('Plug-in Hybrid', 'Plug-in Hybrid'),
    ('Hydrogen', 'Hydrogen Fuel Cell'),
    ('Turbo Diesel', 'Turbo Diesel'),
    ('Twin-Turbo', 'Twin-Turbo'),
]

TRANSMISSION_TYPES = [
    ('Manual', 'Manual'),
    ('Automatic', 'Automatic'),
    ('Semi-Automatic', 'Semi-Automatic'),
    ('CVT', 'CVT (Continuously Variable Transmission)'),
    ('Dual-Clutch', 'Dual-Clutch'),
    ('Tiptronic', 'Tiptronic'),
    ('DSG', 'DSG (Direct-Shift Gearbox)'),
    ('AMT', 'AMT (Automated Manual Transmission)'),
    ('4-Speed Automatic', '4-Speed Automatic'),
    ('5-Speed Automatic', '5-Speed Automatic'),
    ('6-Speed Automatic', '6-Speed Automatic'),
    ('7-Speed Automatic', '7-Speed Automatic'),
    ('8-Speed Automatic', '8-Speed Automatic'),
    ('9-Speed Automatic', '9-Speed Automatic'),
    ('10-Speed Automatic', '10-Speed Automatic'),
    ('5-Speed Manual', '5-Speed Manual'),
    ('6-Speed Manual', '6-Speed Manual'),
    ('7-Speed Manual', '7-Speed Manual'),
    ('8-Speed Manual', '8-Speed Manual'),
    ('Electric Single-Speed', 'Electric Single-Speed'),
]

current_year = datetime.date.today().year
YEAR_CHOICES = [(r, r) for r in range(1980, current_year + 1)]