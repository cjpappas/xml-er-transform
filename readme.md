# XML ER Logical Transform

This project attempts to perform the logical transformation (ref needed) on EER diagrams stored as XML files.

## Setup

- [Python 3](https://www.python.org/downloads/)

## Running

To perform the logical transformation, first ensure that your XML file follows [specification](docs/xml_spec.md). Currently only the first step in the [logical_transformation] is supported. You can run the script on the file:

```bash
python3 main.py <path_to_xml_file>
```
