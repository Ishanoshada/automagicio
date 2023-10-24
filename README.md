# AutoMagicIO

AutoMagicIO is a versatile Python module designed to streamline input/output operations in Python projects. It provides a set of intuitive interfaces and automated routines to handle common file operations, such as reading, writing, and parsing data from various file formats.

## Installation

You can install AutoMagicIO via pip:

```bash
pip install automagicio
```

## Usage

### Reading Data

To get started with AutoMagicIO, you'll need to create an instance of the `AutoMagicIO` class, providing the filename of the data you want to work with.

```python
from automagicio import AutoMagicIO

auto_io = AutoMagicIO('data.csv')
auto_io.read()
```

This will automatically detect the file format (CSV, JSON, or XML) and load the data into memory.

### Writing Data

You can save your processed data using the `write` method, specifying the output filename and format ('json' or 'xml').

```python
auto_io.write('output.json', format='json')
```

### Data Validation

You can check if your data contains required fields using the `validate_data` method. It returns `True` if the data is valid, and `False` otherwise.

```python
valid = auto_io.validate_data()
```

### Sorting Data

To sort your data based on a specific column, use the `sort_data` method. It returns a sorted list of dictionaries.

```python
sorted_data = auto_io.sort_data('Name')
```

### Aggregating Data

You can perform aggregation operations (sum, average, count) on a specific column.

```python
sum_result = auto_io.aggregate_data('Age', 'sum')
average_result = auto_io.aggregate_data('Age', 'average')
count_result = auto_io.aggregate_data('Age', 'count')
```

### Filtering Data

Filter data based on a specific condition. It returns a list of dictionaries that meet the condition.

```python
filtered_data = auto_io.filter_data('City', 'New York')
```

### Transforming Data

Apply a specified transformation function to the values of a specific column. The function should take the current value of the column as input and return the transformed value.

```python
def transform_age(age):
    return int(age) + 5

transformed_data = auto_io.transform_data('Age', transform_age)
```

### Deduplicating Data

Remove duplicate records based on a specified column. It returns a list of dictionaries without duplicates.

```python
unique_data = auto_io.deduplicate_data('Name')
```

### Getting Data

Retrieve the stored data.

```python
data = auto_io.get_data()
```

## Contributors

- [Ishan Oshada](https://github.com/ishanoshada)

## Version

1.0.0

