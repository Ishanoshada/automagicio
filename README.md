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
> Reads data from the specified file format (CSV, JSON, or XML) and automatically detects the format.

### Writing Data

You can save your processed data using the `write` method, specifying the output filename and format ('json' or 'xml').

```python
auto_io.write('output.json', format='json')
```
> Writes data to a file in the specified format.

### Data Validation

You can check if your data contains required fields using the `validate_data` method.

```python
valid = auto_io.validate_data()
```
> Checks if data contains required fields (Name, Age, City).

### Sorting Data

To sort your data based on a specific column, use the `sort_data` method.

```python
sorted_data = auto_io.sort_data('Name')
```
> Sorts data based on the specified column.

### Aggregating Data

You can perform aggregation operations (sum, average, count) on a specific column.

```python
sum_result = auto_io.aggregate_data('Age', 'sum')
average_result = auto_io.aggregate_data('Age', 'average')
count_result = auto_io.aggregate_data('Age', 'count')
```
> Performs aggregation operations on the specified column.

### Filtering Data

Filter data based on a specific condition.

```python
filtered_data = auto_io.filter_data('City', 'New York')
```
> Filters data based on the specified condition.

### Transforming Data

Apply a specified transformation function to the values of a specific column.

```python
def transform_age(age):
    return int(age) + 5

transformed_data = auto_io.transform_data('Age', transform_age)
```
> Applies a specified transformation function to the values of the specified column.

### Deduplicating Data

Remove duplicate records based on a specified column.

```python
unique_data = auto_io.deduplicate_data('Name')
```
> Removes duplicate records based on the specified column.

### Getting Data

Retrieve the stored data.

```python
data = auto_io.get_data()
```
> Gets the stored data.

**Repository Views** ![Views](https://profile-counter.glitch.me/automagicio/count.svg)

## Contributors

- [Ishan Oshada](https://github.com/ishanoshada)

## Version

1.0.0

