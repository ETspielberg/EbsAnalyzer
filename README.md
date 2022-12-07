# The EBS Analyzer

## Usage

### Getting it

To download the EbsAnalyzer either fork this repo or install from Pypi using pip:

```pip install EbsAnalyzer```

### Using it

The EBS Analyzer contains two parts: the EbsAnalyzer itself and the EBsProject to simplify the handling of the necessary data. Just import the two classes into your python script:

```from EbsAnalyter import EbsProject, EbsAnalyzer```

#### Generating a new EBS project

An individual project is defined by a project identifier, the amount of money to be spent, the mechanism used to analyze the data and the filename of the Excel-file containing the usage and price data:

```ebs_project = EbsProject(project_id='my_ebs', filename='sample_data.xlsx', limit=10000, mode='price_normalized_percentiles')```

In addition

## License

MIT License

Copyright (c) 2022 EIKE T. SPIELBERG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
