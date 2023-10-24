# Import necessary modules
import csv
import json
import xml.etree.ElementTree as ET

# Define a DataTransformer class for data transformations
class DataTransformer:
    @staticmethod
    def to_json(data):
        """Convert data to JSON format."""
        return json.dumps(data)

    @staticmethod
    def from_json(data):
        """Convert JSON data back to a Python object."""
        return json.loads(data)

# Define the AutoMagicIO class for file input/output operations
class AutoMagicIO:
    def __init__(self, filename):
        """Initialize with the provided filename and initialize data to None."""
        self.filename = filename
        self.data = None

    def read(self):
        """Read data from the specified file format (csv, json, xml)."""
        if self.filename.endswith('.csv'):
            self.data = self._read_csv()
        elif self.filename.endswith('.json'):
            self.data = self._read_json()
        elif self.filename.endswith('.xml'):
            self.data = self._read_xml()

    def _read_csv(self):
        """Read data from a CSV file and return it as a list of dictionaries."""
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def _read_json(self):
        """Read JSON data from a file and return it."""
        with open(self.filename, 'r') as file:
            return json.load(file)

    def _read_xml(self):
        """Read XML data from a file and return it as a dictionary."""
        tree = ET.parse(self.filename)
        root = tree.getroot()
        return self._xml_to_dict(root)

    def _xml_to_dict(self, element):
        """Convert an XML element to a dictionary."""
        if len(element) == 0:
            return element.text
        data = {}
        for child in element:
            if child.tag not in data:
                data[child.tag] = []
            data[child.tag].append(self._xml_to_dict(child))
        return data

    def _dict_to_xml(self, data, element):
        """Convert a dictionary to an XML element."""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list):
                    for item in value:
                        sub_element = ET.SubElement(element, key)
                        self._dict_to_xml(item, sub_element)
                else:
                    sub_element = ET.SubElement(element, key)
                    self._dict_to_xml(value, sub_element)
        else:
            element.text = str(data)

    def write(self, output_filename, format='json'):
        """Write data to a file in the specified format (json, xml)."""
        if format == 'json':
            self._write_json(output_filename)
        elif format == 'xml':
            self._write_xml(output_filename)

    def _write_json(self, output_filename):
        """Write data to a JSON file."""
        with open(output_filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def _write_xml(self, output_filename):
        """Write data to an XML file."""
        root = ET.Element("root")
        self._dict_to_xml(self.data, root)
        tree = ET.ElementTree(root)
        tree.write(output_filename)

    def validate_data(self):
        """Check if data contains required fields (Name, Age, City)."""
        for row in self.data:
            if 'Name' not in row or 'Age' not in row or 'City' not in row:
                return False
        return True

    def sort_data(self, column):
        """Sort data based on the specified column."""
        sorted_data = sorted(self.data, key=lambda row: row.get(column))
        return sorted_data
        
    def aggregate_data(self, column, operation):
        """Perform aggregation operations (sum, average, count) on the specified column."""
        if operation == 'sum':
            result = sum(row.get(column, 0) for row in self.data)
        elif operation == 'average':
            values = [row.get(column, 0) for row in self.data]
            result = sum(values) / len(values)
        elif operation == 'count':
            result = len(self.data)
        else:
            raise ValueError("Unsupported aggregation operation")
        return result

    def filter_data(self, column, condition):
        """Filter data based on a specified condition."""
        filtered_data = [row for row in self.data if row.get(column) == condition]
        return filtered_data

    def transform_data(self, column, transformation):
        """Apply a specified transformation function to the values of the specified column."""
        transformed_data = [{**row, column: transformation(row.get(column))} for row in self.data]
        return transformed_data

    def deduplicate_data(self, column):
        """Remove duplicate records based on the specified column."""
        unique_data = []
        seen_values = set()
        for row in self.data:
            value = row.get(column)
            if value not in seen_values:
                unique_data.append(row)
                seen_values.add(value)
        return unique_data

    def get_data(self):
        """Get the stored data."""
        return self.data


