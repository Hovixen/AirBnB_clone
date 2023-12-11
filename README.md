# AirBnB Clone ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Build Status](https://travis-ci.org/luischaparroc/AirBnB_clone.svg?branch=master)
![HBnB Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrg8gNSYk0nYCCEmHrbv52AbFktwgIuvxkqniGW-rzfg8SfLIfZKScs8yRZA&s)


### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Further Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repo Contents](#FileContents)
- [Installation](#Installation)
- [Usage](#Usage)
- [Built with](#Built-with)
- [Authors](#Authors)

## Description :floppy_disk:
This is the first phase of a four phase project, to create a basic clone of the AirBnB web app. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.


## Environment :video_game:
The console was developed in `Ubuntu 20.04LTS`.

### Further information :bulb:
For further information on python version, and documentation visit [python.org](https://www.python.org/).

## Requirements :card_file_box:
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 20.04LTS or higher, python3 and pep8 style corrector *(pycodestyle)*.

## Repo Contents :card_index_dividers:
This repository constains the following files:

|   `File`   |   `Description`   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |


## Installation :package:
Clone the repository and run the console.py
```
$ git clone https://github.com/------/AirBnB_clone.git
```

## Usage :loudspeaker:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |


## How the console works :gear:

```
➜ $ ./console.py
(hbnb) create Place
5d6cd533-527b-42a5-96f2-0bdad4d67975
(hbnb) all Place
["[Place] (5d6cd533-527b-42a5-96f2-0bdad4d67975) {'id': '5d6cd533-527b-42a5-96f2-0bdad4d67975', 'created_at': datetime.datetime(2023, 12, 11, 14, 46, 23, 260586), 'updated_at': datetime.datetime(2023, 12, 11, 14, 46, 23, 260615)}"]
(hbnb) update Place 5d6cd533-527b-42a5-96f2-0bdad4d67975 Location "Paris"
(hbnb) show Place 5d6cd533-527b-42a5-96f2-0bdad4d67975
[Place] (5d6cd533-527b-42a5-96f2-0bdad4d67975) {'id': '5d6cd533-527b-42a5-96f2-0bdad4d67975', 'created_at': datetime.datetime(2023, 12, 11, 14, 46, 23, 260586), 'updated_at': datetime.datetime(2023, 12, 11, 14, 47, 25, 119209), 'Location': 'Paris'}
(hbnb) destroy Place 5d6cd533-527b-42a5-96f2-0bdad4d67975
(hbnb) show Place 5d6cd533-527b-42a5-96f2-0bdad4d67975
** no instance found **
(hbnb) count Place
0
(hbnb) quit
$
```


```
➜ $ ./console.py
(hbnb) User.destroy(b8f62bb2-2a87-41be-87a6-6c2e3d2fbd9e)
(hbnb)
vagrant@hovixen:~/AirBnB_clone$ ./console.py
(hbnb) User.create()
5e8f367e-2297-45a1-9a3d-4f4b0c3aa716
(hbnb) User.all()
["[User] (5e8f367e-2297-45a1-9a3d-4f4b0c3aa716) {'id': '5e8f367e-2297-45a1-9a3d-4f4b0c3aa716', 'created_at': datetime.datetime(2023, 12, 11, 14, 58, 57, 472550), 'updated_at': datetime.datetime(2023, 12, 11, 14, 58, 57, 472591)}"]
(hbnb) User.update(5e8f367e-2297-45a1-9a3d-4f4b0c3aa716 first_name "Bomma")
(hbnb) User.show(5e8f367e-2297-45a1-9a3d-4f4b0c3aa716)
[User] (5e8f367e-2297-45a1-9a3d-4f4b0c3aa716) {'id': '5e8f367e-2297-45a1-9a3d-4f4b0c3aa716', 'created_at': datetime.datetime(2023, 12, 11, 14, 58, 57, 472550), 'updated_at': datetime.datetime(2023, 12, 11, 15, 0, 14, 872687), 'first_name': 'Bomma'}
(hbnb) User.destroy(5e8f367e-2297-45a1-9a3d-4f4b0c3aa716)
(hbnb) User.all()
[]
(hbnb) User.show(5e8f367e-2297-45a1-9a3d-4f4b0c3aa716)
** no instance found **
(hbnb) quit
➜ $⁜※

```

## Built with :joystick:
`python3 3.8.10`


### Authors :crayon:
* [Doreen Ikilai](https://github.com/Demidorn)
* [Nelson Erijo](https://github.com/Hovixen)
